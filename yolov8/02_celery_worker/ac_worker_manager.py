#-*- coding: utf-8 -*-
from ac_worker_main import infer_main

print('STARTING Infer Main')

def execute_infer_main():
    dummy_param = 3
    result = infer_main.delay(dummy_param)
    print(f'result:{result}')


if __name__ == '__main__':
    execute_infer_main()


