# 使用官方Python运行时作为父镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将本地代码复制到容器中
COPY . /app

# 使用pip安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 定义容器启动时执行的命令
CMD ["python", "./run.py"]