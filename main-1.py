from minio import Minio
import random
from multiprocessing import Pool
import time
start_time = time.time()
thr=50000
LOCAL_FILE_PATH = './load.jpg'
ACCESS_KEY = 'admin'
SECRET_KEY = ':('
API_HOST="192.168.10.93:9000"
TARGET_BUCKET="load"
FILENAME="load.jpg"
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
    with Pool() as pool:
        print('test')
        for result in pool.map(minioupload, range(thr)):
            print(result)
            print("---RESULT--- %s seconds ---" % (time.time() - start_time))
