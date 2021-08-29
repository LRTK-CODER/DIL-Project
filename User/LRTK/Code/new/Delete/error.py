class MaximumRangeError(Exception):
    def __init__(self):
        super().__init__('최대범위를 넘어섰습니다.')