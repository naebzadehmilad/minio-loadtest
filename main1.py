from minio import Minio
import random,os
from multiprocessing import Pool
import time
import datetime
start_time = time.time()
import configparser
LOCAL_FILE_PATH = './load.jpg'
ACCESS_KEY = 'admin'
SECRET_KEY = 'FinalFinal!!!!'
API_HOST="192.168.10.93:9000"
TARGET_BUCKET="load"
FILENAME="load.jpg"
cpu=20
#thr=5000
conf= configparser.ConfigParser()
if os.path.exists('config.cfg'):
    print('##config.cfg is exist##.')

else:
    conf.add_section("MINIO_CONFIG")
    conf.set('MINIO_CONFIG', 'LOCAL_FILE_PATH', './300kb.log')
    conf.set('MINIO_CONFIG', 'ACCESS_KEY', 'admin')
    conf.set('MINIO_CONFIG', 'SECRET_KEY', 'FinalFinal!!!!')
    conf.set('MINIO_CONFIG', 'API_HOST', '192.168.10.93:9000')
    conf.set('MINIO_CONFIG', 'TARGET_BUCKET', 'load')
    conf.set('MINIO_CONFIG', 'FILENAME', './300kb.log')
    conf.set('MINIO_CONFIG', 'THR', '1000')

    with open('config.cfg', 'w') as configfile:
        conf.write(configfile)
        configfile.close()
conf.read('config.cfg')

LOCAL_FILE_PATH = conf.get('MINIO_CONFIG', 'LOCAL_FILE_PATH')
ACCESS_KEY = conf.get('MINIO_CONFIG', 'ACCESS_KEY')
SECRET_KEY = conf.get('MINIO_CONFIG', 'SECRET_KEY')
API_HOST= conf.get('MINIO_CONFIG', 'API_HOST')
TARGET_BUCKET= conf.get('MINIO_CONFIG', 'TARGET_BUCKET')
FILENAME= conf.get('MINIO_CONFIG', 'FILENAME')
thr= int(conf.get('MINIO_CONFIG', 'THR'))

MINIO_CLIENT = Minio(API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
def minioupload(identifier):
    hash = random.getrandbits(128)
    hashtxt=str(hash)
    found = MINIO_CLIENT.bucket_exists(TARGET_BUCKET)
    if not found:
        MINIO_CLIENT.make_bucket(TARGET_BUCKET)
    else:
       print("Bucket already exists")
    MINIO_CLIENT.fput_object(TARGET_BUCKET, hashtxt+FILENAME,           LOCAL_FILE_PATH,)
    print("It is successfully uploaded to bucket")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    with Pool(processes=cpu) as pool:
        for result in pool.map(minioupload, range(thr)):
            print(result)
            print("---RESULT--- %s seconds ---" % (time.time() - start_time))
