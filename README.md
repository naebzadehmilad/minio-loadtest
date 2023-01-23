# minio-loadtest
You can change  parameters config.cfg

docker build -f dockerfile -t py1 .

lscpu | egrep 'CPU\(s\)'
    CPU(s):                          10
    On-line CPU(s) list:             0-9
    NUMA node0 CPU(s):               0-9
    
docker-compose up  --scale load=10
