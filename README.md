# minio-loadtest
1-- head -c 5MB /dev/urandom > 5mb.log && head -c 3MB /dev/urandom > 3mb.log && head -c 400kb /dev/urandom > 400kb.log

You can change  parameters config.cfg

docker build -f dockerfile -t py1 .

lscpu | egrep 'CPU\(s\)' >>>>>>>>    CPU(s):                          10

    
docker-compose up  --scale load=10
