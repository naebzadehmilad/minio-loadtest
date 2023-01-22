from minio import Minio
import random
import threading
import time
start_time = time.time()
thr=10000
LOCAL_FILE_PATH = './tmdb.sql'
ACCESS_KEY = 'admin'
SECRET_KEY = ':('
API_HOST="192.168.10.93:9000"
TARGET_BUCKET="load"
FILENAME="tmdb.sql"
MINIO_CLIENT = Minio(API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
def minioupload():
    hash = random.getrandbits(128)
    hashtxt=str(hash)
    found = MINIO_CLIENT.bucket_exists(TARGET_BUCKET)
    if not found:
        MINIO_CLIENT.make_bucket(TARGET_BUCKET)
    else:
       print("Bucket already exists")
    MINIO_CLIENT.fput_object(TARGET_BUCKET, hashtxt+FILENAME,           LOCAL_FILE_PATH,)
    print("It is successfully uploaded to bucket")


minioupload()

for j in range(thr):
    thread = threading.Thread(target=minioupload())
    thread.start()
    print(thread.name)
    print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time))
