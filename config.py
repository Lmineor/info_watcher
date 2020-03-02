LOG_FILE = 'app.log'

# 第三方SMTP服务
MAIL_HOST="smtp.XXX.com"  #设置服务器
MAIL_USER="xxx"    #用户名
MAIL_PASS="xxx"   #口令 

try:
    from local_config import *  # locals_config 进行覆盖
except ImportError as e:
    pass

SENDER = MAIL_USER
RECEIVERS = [MAIL_USER]

# 目标院校
SCHOOLS = [
    'http://www.ia.cas.cn/yjsjy/zs/sszs/index.html'
]