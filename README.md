# Yooc-Auto-Exam-Bot
自动完成浙理易班考试，实现了自动保存答案，验证码自动识别等操作
# 写在前面
该程序为本人闲暇之作，旨在迅速完成易班考试，但不料该程序竟花费本人近五小时，要只是本人独自享用，对那五小时着实说不过去，遂将源码置于此，供各位观赏，观赏之余呢，也希望各位不忘给颗星星。

# 使用要求
1. Python >= 3.8

# 使用方法
1. 安装Python,打开powershell输入pip install ddddocr 或者 pip install -r requirements.txt
2. 登录易班，进入考试界面，将所有考试同时开启，若已完成可忽略
3. 运行程序，输入账号密码，确保账号密码正确，否则会导致死循环，再输入课群组号，浙理为3665127
4. 刷新网页，并依次提交答案
## 下面是手把手教学
下载Python，[点击下载Python3.9.6](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)，安装时注意勾选Add to PAATH
![install python](https://user-images.githubusercontent.com/53895652/129552654-b17ec7c5-db08-4612-880a-9d69779c719e.png)

打开powershell，不知道什么是powershell？没事，按下win键输入powershell即可
![powershell_1](https://user-images.githubusercontent.com/53895652/129552846-68d04087-c42d-4632-bcff-eb19d3166515.png)
在powershell弹出的框框中输入pip install ddddocr -i https://pypi.tuna.tsinghua.edu.cn/simple 后回车，等待模块安装完成
![powershell_2](https://user-images.githubusercontent.com/53895652/129553029-7e4b23e9-16f1-44bb-88f6-84fa0bf1f9c9.png)
下载本软件，并解压！
![download](https://user-images.githubusercontent.com/53895652/129553218-9d53e6ba-4e0e-46bf-8af5-1085a2381791.png)
还记得刚刚的powershell界面吗，输入python后加一个空格，将解压出来的文件中的main.py拖进去
![powershell_3](https://user-images.githubusercontent.com/53895652/129553475-8bb36d8f-85e6-402b-955e-5d0340b64be6.png)
接着就会变成这样，回车即可
![powershell_4](https://user-images.githubusercontent.com/53895652/129553512-1401d4d2-6158-4367-ab3c-e7d0db2c80bc.png)
去易班把每个想让程序做的考试都开启，若已经完成测试，也可点击重新测试
![yooc_1](https://user-images.githubusercontent.com/53895652/129553711-7276da74-f850-41b8-a53d-5620a0be7cb2.png)
程序中输入指定数据，若考试已完成，则会有如下输出
![powershell_5](https://user-images.githubusercontent.com/53895652/129553973-2a401698-d8c9-4e5a-9524-ad41621c675c.png)
请查看注意事项内容

# 注意事项
1. 若存在填空题，程序会输出填空题的所有答案，将其填入题目横线内即可
2. 程序支持直接提交，建议有动手能力的人直接查看源代码

# 免责声明
1. 由于本程序产生的所有纠纷与本人无关
2. 由于使用本程序导致的一切后果与本人无关

# 最后
本程序遵循MIT协议
