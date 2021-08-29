import pandas, numpy

DataFrame = pandas.core.frame.DataFrame

def roundOff(data:int, seatNum:int) -> int:
    '''
    Creator: 오석재
    Date: 2021.07.17
    version: 1.0

    [Explanation]
        이 함수는 반올림(사사오입)을 구현한 함수입니다.
        랜덤 라운딩을 구현하기 위해 전테 데이터인 DataFrame이 아닌 data를 인자으로 받아서 라운드 처리를 합니다.

    [Parameter]
        - data:int -> 라운드하고자 하는 정수형 데이터
        - seatNum:int -> 라운드하고 하는 정수형 데이터의 자리

    [수정해야하는 부분]
    '''
    if seatNum < 0:
        print('[Error] seatNum의 인자는 0를 초과해야합니다.')
        return -1
    elif len(str(data)) < seatNum:
        print('[Error] 최대범위를 넘어섰습니다.')
        return -1

    data = list(str(data))
    if int(data[-seatNum]) >= 5:
        data[-seatNum-1] = str(int(data[-seatNum-1]) + 1)
        data[-seatNum:] = '0' * len(data[-seatNum:])
    else:
        data[-seatNum:] = '0' * len(data[-seatNum:])

    return int(''.join(data))

def roundUp(data:int, seatNum:int) -> int:
    '''
    Creator: 오석재
    Date: 2021.07.17
    version: 1.0 -> 사소한 것 수정 시 소수점 수정, 큰 틀 변경시 앞자리 수정

    [Explanation]
        이 함수는 올림을 구현한 함수입니다.
        랜덤 라운딩을 구현하기 위해 전테 데이터인 DataFrame이 아닌 data를 인자으로 받아서 라운드 처리를 합니다.

    [Parameter]
        - data:int -> 라운드하고자 하는 정수형 데이터
        - seatNum:int -> 라운드하고 하는 정수형 데이터의 자리
        
    [수정해야하는 부분]
    '''
    if seatNum < 0:
        print('[Error] seatNum의 인자는 0를 초과해야합니다.')
        return -1
    elif len(str(data)) < seatNum:
        print('[Error] 최대범위를 넘어섰습니다.')
        return -1

    data = list(str(data))
    if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
        data[-seatNum-1] = str(int(data[-seatNum-1]) + 1)
        data[-seatNum:] = '0' * len(data[-seatNum:])

    return int(''.join(data))

def roundDown(data:int, seatNum:int) -> int:
    '''
    Creator: 오석재
    Date: 2021.07.17
    version: 1.0 -> 사소한 것 수정 시 소수점 수정, 큰 틀 변경시 앞자리 수정

    [Explanation]
        이 함수는 내림을 구현한 함수입니다.
        랜덤 라운딩을 구현하기 위해 전테 데이터인 DataFrame이 아닌 data를 인자으로 받아서 라운드 처리를 합니다.

    [Parameter]
        - data:int -> 라운드하고자 하는 정수형 데이터
        - seatNum:int -> 라운드하고 하는 정수형 데이터의 자리
        
    [수정해야하는 부분]
    '''
    if seatNum < 0:
        print('[Error] seatNum의 인자는 0를 초과해야합니다.')
        return -1
    elif len(str(data)) < seatNum:
        print('[Error] 최대범위를 넘어섰습니다.')
        return -1

    data = list(str(data))
    if int(data[-seatNum]) or len(set(data[-seatNum:])) > 1:
        data[-seatNum:] = '0' * len(data[-seatNum:])

    return int(''.join(data))