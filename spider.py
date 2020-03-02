import requests

from config import SCHOOLS
from send_email import send_email


for school in SCHOOLS:
    print('哈哈哈哈')
    req = requests.get(school)
    req.encoding = 'utf-8'
    print(req.encoding)
    # print(req.text)
# contend = 'Python 邮件发送测试....'
# froms = '邮件测试'
# to = '我的163'
# subject = "python SMTP 邮件测试"
# send_email(contend, froms, to, subject)