import sys, pandas
sys.path.append('../')

import test3, test4

if __name__ == '__main__':
    excel = pandas.read_excel('../test2.xlsx', index_col=0)
    indexSize = len(excel)

    test3.classification(excel, indexSize, '기관명', '회사')
    test4.local(excel, indexSize, '수입', [1,5])
    print(excel)