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
ZDH = 'http://www.ia.cas.cn/yjsjy/zs/sszs/index.html' # 自动化所
JSS = 'http://www.ict.cas.cn/shye/tzgg/index.html' # 计算所
XGS = 'http://www.iie.cas.cn/yjsjy_101173/yjszxtz/index.html' # 信工所
WLXXZX = 'http://www.cnic.cas.cn/yjsjy/tzgg/index.html' # 网络信息中心

INTERVAL = 300 # 默认300s 查询一次接口