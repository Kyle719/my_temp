#-*- coding: utf-8 -*-
from celery import Celery
import ac_worker_config

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
infer_task_app = Celery('infer_task', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)
infer_task_app.conf.broker_transport_options = {'visibility_timeout' : 259200}


import sys
sys.path.append(f'{ac_worker_config.ROOT_PATH}/01_ultralytics')
from ac_predict_detc import main

@infer_task_app.task(bind=True, name='infer-task')
def infer_main(self, num):
    main()

# if __name__ == '__main__':
#     dummy_param = 3
#     result = infer_main.delay(dummy_param)
#     print(f'result:{result}')
