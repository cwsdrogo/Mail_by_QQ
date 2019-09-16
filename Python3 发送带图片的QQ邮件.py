# -*- conding:UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

mail_server = "smtp.qq.com"
port = "465"

sender = "xxx@qq.com"  # 发件人
password = "ikldecfoihumdejc"  # 发件人smtp密码，即授权码
receiver = ["xxx@qq.com"]  # 收信人

# 创建一个"正文+附件"的实例
massage = MIMEMultipart()

massage["From"] = Header("你的挚友", "utf-8")
massage["To"] = Header("岁月静好", "utf-8")
massage["Subject"] = Header("电影天堂", "utf-8")

# 邮件正文内容
mail_msg = """
<p><img src="cid:image1"></p>
"""

# 邮件正文处理部分
massage.attach(MIMEText(mail_msg, "html", "utf-8"))

# 邮件正文嵌入图片
fp = open("/root/movie.png", "rb")
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header("Content-ID", "<image1>")
massage.attach(msgImage)

try:
    mail = smtplib.SMTP_SSL(mail_server, port)  # 连接邮件服务器
    status = mail.login(sender, password)  # 登录
    print(status)
    mail.sendmail(sender, receiver, massage.as_string())  # 发送邮件
    print("邮件发送成功！")
    mail.quit()  # 登出
except Exception as e:
    print(e)
    mail.quit()
    print("邮件发送失败！")
