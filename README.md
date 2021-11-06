# 2021/11/6停更说明
程序仍然可以使用，请自行抓包，并修改[91](https://github.com/Neutron-Bomb/Yooc-Auto-Exam-Bot/blob/master/erohal/yooc.py#L91)/[99](https://github.com/Neutron-Bomb/Yooc-Auto-Exam-Bot/blob/master/erohal/yooc.py#L99)/[113](https://github.com/Neutron-Bomb/Yooc-Auto-Exam-Bot/blob/master/erohal/yooc.py#L113)行处的特征值。本程序永久停更。

# Yooc-Auto-Exam-Bot
自动完成浙理易班考试，实现了自动保存答案，验证码自动识别等操作  

更新：实现了部分课程的自动完成，详见源代码。

# 写在前面
该程序为本人闲暇之作，旨在迅速完成易班考试，但不料该程序竟花费本人近五小时，要只是本人独自享用，对那五小时着实说不过去，遂将源码置于此，供各位观赏，观赏之余呢，也希望各位不忘给颗星星。

# 使用要求
1. Python >= 3.8

# 使用方法
前提条件：易班考试为可查试题答案，如果是禁止查卷，则无法使用本程序。
1. 安装Python,打开powershell输入pip install ddddocr && pip install requests或者pip install -r requirements.txt(后者需切换到requirements.txt所在目录)
2. 登录易班，进入考试界面，将所有考试同时开启，若已完成可忽略
3. 运行程序，输入账号密码，确保账号密码正确，否则会导致死循环，再输入课群组号，浙理为3665127
4. 刷新网页，并依次提交答案

## 还有手把手教学
[点击进入手把手教学](https://github.com/Erohal/Yooc-Auto-Exam-Bot/blob/master/Hand%20By%20Hand.md)
# 注意事项
1. 若存在填空题，程序会输出填空题的所有答案，将其填入题目横线内即可
2. 程序支持直接提交，建议有动手能力的人直接查看源代码
3. 若遇到ddddocr库报错问题，请安装visual redistribution 2019运行库

# 免责声明
1. 由于本程序产生的所有纠纷与本人无关
2. 由于使用本程序导致的一切后果与本人无关

# 最后
本程序遵循MIT协议
