# coding: utf-8
import os
import datetime
import traceback
import logging


def get_traceback_string():
    return traceback.format_exc()


def write_log(log_type, target="./logs", error_message=None):
    """

    :param log_type: 에러 타입 정의. 파일명의 prefix 가 됨
    :param error_message: 에러 메시지. 만약 없으면 traceback 이 찍힘
    :param target: 파일이 저장되는 장소
    :return:
    """
    # path check & create
    if not os.path.exists(target):
        os.makedirs(target)
    # file check & create
    _today = datetime.datetime.today()
    file_name = '{}_{}.log'.format(log_type, _today.strftime("%Y%m%d"))
    full_path = '{}/{}'.format(target, file_name).replace('//', '/')
    logging.basicConfig(filename=full_path,
                        filemode='a',
                        format='%(asctime)s|%(pathname)s|%(funcName)s|%(message)s')
    # write message
    if error_message is None:
        error_message = get_traceback_string()
    logging.error(error_message)


def div0():
    try:
        1/0
    except ZeroDivisionError:
        write_log('div0')

def main():
    div0()
    print 'done'


if __name__ == "__main__":
    main()
