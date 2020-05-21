
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


mail_host='smtp.broadmesse.com'
mail_user='salvager.shen@broadmesse.com'
sender_password='Salvager.2010'
sender = 'salvager.shen@broadmesse.com'
receivers = '53927010@qq.com'

message = MIMEText('Python邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
subject = '邮件测试' + send_time
message['Subject'] = subject

try:
    smtp_obj = smtplib.SMTP()
    smtp_obj.connect(mail_host, 25)
    smtp_obj.login(sender, sender_password)
    smtp_obj.sendmail(sender, [receivers], message.as_string())
    print('success!')
except smtplib.SMTPException as e:
    print('failure!')
    print(e)
