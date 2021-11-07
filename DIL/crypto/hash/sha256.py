import pandas, hashlib
from util import DataSetting


class SHA256(DataSetting):
    """
    | 암호화 기술 중 단방향 암호화(SHA-256)를 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.

    Args:
        datas (pandas.DataFrame) : 단방향 암호화(SHA-256)를 적용할 DataFrame 지정
    """

    def run(self, column: str):
        """
        SHA-256 암호화를 수행하는 메소드

        Args:
            column (str) : SHA-256 암호화를 적용할 컬럼

        Returns:
            bool : 기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)

        result = []
        for data in datas:
            hash = hashlib.sha256()
            hash.update(data.encode("utf-8"))

            result.append(hash.hexdigest())

        self.datas.loc[:, column] = result

        return True
