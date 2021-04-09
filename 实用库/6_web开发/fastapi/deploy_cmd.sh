IP=$1
PORT=$2
WORKERS=$3
# 杀死之前的运行的端口号为PORT的python服务
ps -ef | grep $PORT | grep -v grep | awk '{print $2}' | xargs kill -9

# 激活anaconda环境 环境名称 py36
#source source /home/dataexa/anaconda3/bin/activate py36

# run python服务
uvicorn --host $IP --port $PORT --workers $WORKERS fastapi_service:app &
