import pandas, hashlib, base64
from Crypto import Random
from Crypto.Cipher import AES

from util import DataSetting

DataFrame = pandas.DataFrame


class AES256(DataSetting):
    """
    | 암호화 기술 중 양방향 암호화(AES-256)를 구현한 클래스
    | 모든 메소드는 생성자에 원본 데이터를 인자 값으로 넣으면 원본 데이터를 수정한다.

    Args:
        datas (pandas.DataFrame) : 양방향 암호화 기술(AES-256 암호화)을 적용할 DataFrame 지정
        key (str) : AES-256 암호화에 사용될 암호키 지정
    """

    def __init__(self, datas: DataFrame, key: str):
        self.datas = datas

        self.bs = 32
        self.key = hashlib.sha256(key.encode("utf-8")).digest()

    def encrypt(self, column: str):
        """
        AES-256 암호화를 수행하는 메소드

        Args:
            column (str) : AES-256 암호화를 적용할 컬럼

        Returns:
            bool : 기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)

        result = []
        for raw in datas:
            raw = self._pad(raw)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            cipherText = base64.b64encode(iv + cipher.encrypt(raw.encode()))
            result.append(cipherText.decode())

        self.datas.loc[:, column] = result

        return True

    def decrypt(self, column: str):
        """
        AES-256 복호화를 수행하는 메소드

        Args:
            column (str) : AES-256 복호화를 적용할 컬럼

        Returns:
            bool : 기술 적용 성공 시 True 리턴
        """
        datas = self._toList(column)

        result = []
        for enc in datas:
            enc = base64.b64decode(enc.encode())
            iv = enc[: AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            plainText = self._unpad(cipher.decrypt(enc[AES.block_size :])).decode(
                "utf-8"
            )
            result.append(plainText)

        self.datas.loc[:, column] = result

        return True

    def _pad(self, s):
        return s + (self.bs - len(s.encode("utf-8")) % self.bs) * chr(
            self.bs - len(s.encode("utf-8")) % self.bs
        )

    @staticmethod
    def _unpad(s):
        return s[: -s[-1]]
