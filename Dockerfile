# 使用官方Python运行时作为父镜像
FROM python:3.9.6-slim AS base
## start builder stage.

# this is the first stage of the build.
# it will install all requirements.
FROM base AS builder
#
# RUN apt-get install -y xvfb gnupg wget curl unzip --no-install-recommends && \
#     wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#     echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
#     apt-get update -y && \
#     apt-get install -y google-chrome-stable && \
#     CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
#     DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
#     wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
#     unzip /chromedriver/chromedriver* -d /chromedriver
#
# # make the chromedriver executable and move it to default selenium path.
# RUN chmod +x /chromedriver/chromedriver
# RUN mv /chromedriver/chromedriver /usr/bin/chromedriver

# 设置工作目录
WORKDIR /app

# 将本地代码复制到容器中
COPY . /app

# 使用pip安装依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

# 定义容器启动时执行的命令
CMD ["python", "./run.py"]