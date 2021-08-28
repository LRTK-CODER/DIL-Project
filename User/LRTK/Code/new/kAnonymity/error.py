class ColumnsEmptyError(Exception):
    def __init__(self):
        super().__init__('k-익명성에 적용할 Column이 없습니다.')

class KSizeError(Exception):
    def __init__(self):
        super().__init__('k의 값은 1보다 커야합니다.')