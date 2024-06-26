#!/bin/bash

# 设置默认的环境变量值
DEFAULT_ROLE="master"
DEFAULT_MASTER_IP="127.0.0.1"

# 读取环境变量，或者使用默认值
ROLE=${LOCUST_ROLE:-$DEFAULT_ROLE}
MASTER_IP=${LOCUST_MASTER_IP:-$DEFAULT_MASTER_IP}

# 检查包管理器并安装依赖
if command -v apt-get &> /dev/null; then
    echo "Using apt-get to install dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3-dev gcc
elif command -v yum &> /dev/null; then
    echo "Using yum to install dependencies..."
    sudo yum install -y python3-devel gcc
elif command -v dnf &> /dev/null; then
    echo "Using dnf to install dependencies..."
    sudo dnf install -y python3-devel gcc
elif command -v brew &> /dev/null; then
    echo "Using brew to install dependencies..."
    brew install python gcc
else
    echo "Unsupported package manager. Please install python3-dev and gcc manually."
    exit 1
fi

# 检查 locust 是否安装
if ! command -v locust &> /dev/null; then
    echo "Locust not found, installing locust..."
    pip install locust
    if [ $? -ne 0 ]; then
        echo "Failed to install locust. Exiting."
        exit 1
    fi
fi

# 配置代理
if [ -n "$HTTP_PROXY" ]; then
    export http_proxy=$HTTP_PROXY
fi
if [ -n "$HTTPS_PROXY" ]; then
    export https_proxy=$HTTPS_PROXY
fi

# 检查角色并执行相应的命令
if [ "$ROLE" == "master" ]; then
    echo "Starting Locust as master..."
    locust -f locustfile.py --master
    # 等待 worker 节点启动并连接
    sleep 5
elif [ "$ROLE" == "slave" ]; then
    echo "Starting Locust as worker..."
    echo "Connect to master $MASTER_IP"
    locust -f locustfile.py --worker --master-host=$MASTER_IP
else
    echo "Invalid role specified. Please set LOCUST_ROLE to either 'master' or 'slave'."
    exit 1
fi
