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
SCHOOLS = {
    '自动化所': 'http://www.ia.cas.cn/yjsjy/zs/sszs/index.html',
    '计算所': 'http://www.ict.cas.cn/shye/tzgg/index.html',
    '信工所': 'http://www.iie.cas.cn/yjsjy_101173/yjszxtz/index.html',
    '网络信息中心': 'http://www.cnic.cas.cn/yjsjy/tzgg/index.html',
    '声学所': 'http://www.ioa.cas.cn/yjsjy/zs/zstz/',
    '国科大招生网站': 'http://admission.ucas.ac.cn/',
    '考研帮': 'http://tiaoji.kaoyan.com/beijing/',
}



"""
li_list = soup.find('ul', attrs={'class':'fontlist'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res
"""
RULES = {
    '自动化所': ['ul', 'fontlist', 'find'],       # ['label', 'attrs', 'findall or find or fail']
    '计算所': ['td', 'black_14', 'findAll'],
    '信工所': ['td', 'black_14', 'findAll'],
    '网络信息中心': ['ul', 'list-font margin-top-10 clearfix', 'find'],
    '声学所': ['', '', 'fail'],
    '国科大招生网站': ['ul', 'mp-list', 'find'],
    '考研帮': ['ul', 'list areaZslist', 'find'],
}

# 目标院校
ZDH = 'http://www.ia.cas.cn/yjsjy/zs/sszs/index.html' # 自动化所
JSS = 'http://www.ict.cas.cn/shye/tzgg/index.html' # 计算所
XGS = 'http://www.iie.cas.cn/yjsjy_101173/yjszxtz/index.html' # 信工所
WLXXZX = 'http://www.cnic.cas.cn/yjsjy/tzgg/index.html' # 网络信息中心
SXS = 'http://www.ioa.cas.cn/yjsjy/zs/zstz/' # 声学所
GKD = 'http://admission.ucas.ac.cn/' # 国科大招生网站


# 第三方网站
KYB = 'http://tiaoji.kaoyan.com/beijing/' # 考研帮

INTERVAL = 300 # 默认300s 查询一次接口