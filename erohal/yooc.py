# Generate By Erohal At 2021/08/16 11:50
from requests import Session
import ddddocr
import re
import json

class YoocBot:
    def __init__(self,username:str,password:str,groupid:str):
        self.errno = 0

        self.username = username
        self.password = password
        self.groupid  = groupid

        self.urlmap = \
        {
            'login'       : 'https://www.yooc.me/login',
            'login_ajax'  : 'https://www.yooc.me/yiban_account/login_ajax',
            'save_ans'    : 'https://www.yooc.me/group/{}/exam/{}/answer/save',
            'submit_ans'  : 'https://www.yooc.me/group/{}/exam/{}/answer/submit',
            'get_ans'     : 'https://www.yooc.me/mobile/group/{}/exams/{}/subject?view_type=result',
            'captcha_img' : 'https://www.yooc.me/captcha/image/{}/',
            'exam_list_1' : 'https://www.yooc.me/group/{}/exams',
            'exam_list_2' : 'https://www.yooc.me/group/{}/exam/(.*?)/edit',
            'repeat_exam' : 'https://www.yooc.me/group/3665127/exam/214471/examuser//repeat'
        }
        self.session = Session()
        self.csrf_token = self.__get_csrf_token()
        
        while not self.__login():
            pass


    def __get_csrf_token(self):
        return self.session.get(self.urlmap['login']).cookies.get('csrftoken')

    def __get_captcha_key(self):
        res = self.session.get(self.urlmap['login'])
        ret = re.search(self.urlmap['captcha_img'].format('(.*?)'),res.content.decode('utf-8'))
        return ret.group(1)

    def __captcha(self,captcha_key:str):
        ocr = ddddocr.DdddOcr()
        with self.session.get(self.urlmap['captcha_img'].format(captcha_key)) as f:
            res = ocr.classification(f.content)
        return res
    
    def __login(self):
        captcha_key = self.__get_captcha_key()
        data = \
        {
            'email' : self.username,
            'password' : self.password,
            'code' : self.__captcha(captcha_key),
            'captcha_key': captcha_key,
            'remember' : True
        }
        header = {'X-CSRFToken' : self.csrf_token}
        res = self.session.post(self.urlmap['login_ajax'],data,headers=header).content.decode('utf-8')
        res_json = json.loads(res)
        return res_json['success']

    def __save_ans(self,examid:str,ans:str):
        data = \
        {
            'answers' : ans
        }
        header = {'X-CSRFToken' : self.csrf_token}
        res = self.session.post(self.urlmap['save_ans'].format(self.groupid,examid),data,headers=header).content.decode('utf-8')
        return json.loads(res)

    def __submit_ans(self,examid:str,ans:str):
        data = \
        {
            'csrfmiddlewaretoken' : self.csrf_token,
            'answers' : ans,
            'type': 0,
            'auto': 0
        }
        res = self.session.post(self.urlmap['submit_ans'].format(self.groupid,examid),data).content.decode('utf-8')
        return json.loads(res)

    def __generate_answer(self,examid:str):
        res = self.session.get(self.urlmap['get_ans'].format(self.groupid,examid)).content.decode('utf-8')
        data_raw = json.loads(re.search(r'var data=(.*?).filter',res).group(1))
        ret_ans = ''
        for types in data_raw:
            data = types[2]
            if types[0] == '单选题' or types[0] == '一、选择题':
                # ans_map = {'A' : 1,'B' : 2,'C' : 0,'D' : 3}
                for item in data:
                    question_name = re.search(r'data-question-name=\'(.*?)_1\'',item['question']).group(1)
                    question_ans  = re.search(r'<p>正确答案：(.)</p>',item['question']).group(1)
                    question_var  = re.search(r'data-question-value=\'(.)\'>{}.'.format(question_ans),item['question']).group(1)
                    ans_str = '{"' + question_name + '":{"1":["' + str(question_var) + '"]}},'
                    ret_ans += ans_str
            elif types[0] == '多选题':
                for item in data:
                    question_name = re.search(r'data-question-name=\'(.*?)_1\'',item['question']).group(1)
                    question_ans  = re.search(r'<p>正确答案：(.*?)</p>',item['question']).group(1)
                    ans_arr = question_ans.split('、')
                    ans_str = ''
                    for ans in ans_arr:
                        question_var  = re.search(r'data-question-value=\'(.)\'>{}.'.format(ans),item['question']).group(1)
                        temp_str = '"' + question_var + '",'
                        ans_str += temp_str
                    ans_str = ans_str[0:-1]

                    ans_str = '{"' + question_name + '":{"1":[' + ans_str + ']}},'
                    ret_ans += ans_str
            elif types[0] == '判断题':
                for item in data:
                    question_name = re.search(r'data-question-name=\'(.*?)_1\'',item['question']).group(1)
                    question_ans  = re.search(r'<p>正确答案：(.)</p>',item['question']).group(1)
                    question_var  = re.search(r'data-question-value=\'(.)\'>{}.'.format(question_ans),item['question']).group(1)
                    ans_str = '{"' + question_name + '":{"1":["' + str(question_var) + '"]}},'
                    ret_ans += ans_str
            elif types[0] == '填空题':
                pos = 1        
                for item in data:
                    question_ans  = re.search(r'<p>正确答案：(.*?)</p>',item['question']).group(1)
                    print(str(pos) + '. ' + question_ans)
                    pos += 1

        ret_ans = ret_ans[0:-1]
        ret_ans = '[' + ret_ans + ']'
        return ret_ans

    def __repeat_exam(self,examid:str):
        pass

    def __start_exam(self,examid:str):
        pass
    
    def compile_and_submit(self,examid:str):
        ans = self.__generate_answer(examid)
        return self.__submit_ans(examid,ans)

    def compile_and_save(self,examid:str):
        ans = self.__generate_answer(examid)
        return self.__save_ans(examid,ans)
    
    def get_exam_list(self):
        res = self.session.get(self.urlmap['exam_list_1'].format(self.groupid)).content.decode('utf-8')
        res = re.findall(self.urlmap['exam_list_2'].format(self.groupid),res)
        return res
