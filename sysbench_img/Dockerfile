FROM ubuntu:18.04

WORKDIR /sysbench
RUN apt-get update && apt-get install -y sysbench
CMD sysbench --num-threads=64 --test=threads --thread-yields=1000 --thread-locks=8 run
