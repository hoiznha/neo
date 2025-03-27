#!/bin/bash

# daemon stop
./stop_replica.sh

# directory setup
if [ -d /replica/data ]; then
    rm -rf /replica/data
else
    mkdir -pv /replica/data
    mkdir -pv /replica/data/master
    mkdir -pv /replica/data/slave1
    mkdir -pv /replica/data/slave2
    mkdir -pv /replica/data/arbiter

    touch /replica/data/master/master.log
    touch /replica/data/slave1/slave1.log
    touch /replica/data/slave2/slave2.log
    touch /replica/data/arbiter/arbiter.log
fi

/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/master.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/slave1.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/slave2.conf &
/replica/mongodb/bin/mongod --config /work/neo/mongodb/replica/arbiter.conf &
netstat -nltp | grep mongo
sleep 5s

# Replication Init setup
/replica/mongodb/bin/mongo --port 10000 < rs_start