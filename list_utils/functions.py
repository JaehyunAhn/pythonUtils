# coding: utf-8
def grouper(ITER_LIST, UNIT_SIZE):
    """
    리스트를 유닛 사이즈만큼 분리해서 묶어주는 함수
    :param ITER_LIST: 분리해서 담고자 하는 리스트
    :param UNIT_SIZE: 한 리스트당 쌓일 사이즈
    :return: [예시] : grouper([A,B,C,D,E,F,G], 3) --> [A,B,C] [D,E,F] [G]
    """
    _ret_list = [ITER_LIST[i:i+UNIT_SIZE] for i in range(0, len(ITER_LIST), UNIT_SIZE)]
    return _ret_list


def grouper_days_to_unit_size(DAYS, UNIT_SIZE):
    """
    오늘부터 앞으로 날짜를 보면서 리스트 만들어주는 함수
    :param DAYS:
    :param UNIT_SIZE:
    :return:
    """
    import datetime
    base = datetime.datetime.today().date()
    tmp_list = [base - datetime.timedelta(days=x) for x in range(0, DAYS, UNIT_SIZE)]
    last_day = base - datetime.timedelta(days=DAYS+1)
    tmp_list.append(last_day)

    ret = []
    for idx in range(len(tmp_list)-1):
        ret.append([str(tmp_list[idx+1] + datetime.timedelta(days=1)), str(tmp_list[idx])])
    return ret


def grouper_period_to_unit_size(PERIOD, UNIT_SIZE):
    """
    그룹 리스트를 넣으면 날짜 계산해서 리스트 만들어주는 함수
    :param PERIOD:
    :param UNIT_SIZE:
    :return:
    """
    import datetime
    start_date = datetime.datetime.strptime(PERIOD[0], "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(PERIOD[1], "%Y-%m-%d").date()

    _interval = (end_date - start_date).days
    tmp_list = [end_date - datetime.timedelta(days=x) for x in range(0, _interval, UNIT_SIZE)]
    start_date -= datetime.timedelta(days=1)
    tmp_list.append(start_date)

    ret = []
    for idx in range(len(tmp_list)-1):
        ret.append([str(tmp_list[idx+1] + datetime.timedelta(days=1)), str(tmp_list[idx])])
    return ret


def list_to_dict(KEY_INDEX, LIST):
    """
    리스트를 받아서 KEY, LIST DICT 로 편성해주는 함수
    :param KEY_INDEX: int value, LIST 한 줄의 몇 번째 요소가 KEY VALUE 로 사용되는가를 의미
    :param LIST: 인풋 리스트
    :return:
    """
    return_dict = {}
    for item in LIST:
        return_dict.update({item[KEY_INDEX], item})
    return return_dict


def convert_date_list(date_from, date_to):
    """
    A - B 까지 날짜 리스트 반환
    :param date_from:
    :param date_to:
    :return:
    """
    import datetime
    date_from_obj = datetime.datetime.strptime(str(date_from), "%Y%m%d")
    date_to_obj = datetime.datetime.strptime(str(date_to), "%Y%m%d")

    date_list = list()
    for days in range((date_to_obj - date_from_obj).days + 1):
        _item = int((date_from_obj + datetime.timedelta(days=days)).strftime("%Y%m%d"))
        date_list.append(_item)
    return date_list

if __name__ == "__main__":
    a = convert_date_list(20170810, 20170902)
    print a

    # peri = ['2011-02-01', '2012-02-01']
    # r = grouper_period_to_unit_size(peri, 100)
    # for item in r:
    #     print item

    print '<libs/python_utils.py> 테스트 끝.'