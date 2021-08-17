from erohal import yooc

def main():
    print('请登录易班考试，并点击开始考试，然后输入以下内容')
    while True:
        username = input('易班账号:')
        password = input('易班密码:')

        groupid = input('groupid(3665127 For 浙理):')

        yb = yooc.YoocBot(username,password,groupid)
        print('您当前有:',yb.get_exam_list(),'可做')

        for exam in yb.get_exam_list():
            print(exam,':',yb.compile_and_save(exam))
            # 删除上面一行，关闭下一行的注释将会导致直接提交答案
            # print(exam,':',yb.compile_and_submit(exam))
        print('请刷新网站查看并提交')
    
if __name__ == '__main__':
    main()
