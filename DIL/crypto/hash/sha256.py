import sys, os

sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    )
)

import pandas, hashlib
from util import DataSetting


class SHA256(DataSetting):
    def run(self, column: str):
        datas = self._toList(column)

        result = []
        for data in datas:
            hash = hashlib.sha256()
            hash.update(data.encode("utf-8"))

            result.append(hash.hexdigest())

        self.datas.loc[:, column] = result


if __name__ == "__main__":
    excel = pandas.read_csv("../Sample/test_100.csv", index_col=0)
    print(excel.head())

    hash = SHA256(excel)
    hash.run("이름")
    print(excel.head())
