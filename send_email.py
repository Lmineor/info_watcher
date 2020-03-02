import smtplib
from email.mime.text import MIMEText
from email.header import Header

from config import MAIL_USER, MAIL_PASS, MAIL_HOST, SENDER, RECEIVERS
from Slog import logger

def send_email(contend, froms, to, subject):
    message = MIMEText(contend, 'plain', 'utf-8')
    message['From'] = Header(froms, 'utf-8')
    message['To'] = Header(to, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(MAIL_HOST, 25)    # 25 为 SMTP 端口号
        smtpObj.login(MAIL_USER,MAIL_PASS)  
        smtpObj.sendmail(SENDER, RECEIVERS, message.as_string())
        logger.info("邮件发送成功")
    except smtplib.SMTPException:
        logger.error("Error: 无法发送邮件")


def test():
    contend = 'Python 邮件发送测试....'
    froms = '邮件测试'
    to = '我的163'
    subject = "python SMTP 邮件测试"
    send_email(contend, froms, to, subject)

if '__name__' == '__main__':
    test()