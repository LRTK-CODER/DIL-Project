class SeatNumNegativeError(Exception):
    def __init__(self):
        super().__init__('seatNum의 인자는 0를 초과해야합니다.')

class MaximumRangeError(Exception):
    def __init__(self):
        super().__init__('최대범위를 넘어섰습니다.')