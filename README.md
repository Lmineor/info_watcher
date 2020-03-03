## 主要用于监测目标院校网页是否有新的通知
## 实现方法
- 定时请求目标网页，若有新信息通过邮件的方式通知自己
- 采用增量更新的方法
## 运行
1、新建local_config.py
```py
cd tiaoji_spider
# 第三方 SMTP 服务
MAIL_HOST="smtp.***.com"   #设置发送方服务器
MAIL_USER="xxx@***.com"    #用户名
MAIL_PASS="password"       #口令 
```
2、运行
```py
python run.py
```