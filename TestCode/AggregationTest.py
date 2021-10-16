import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import pandas
from DIL import statistics


def test_statistics_aggregation():
    CURRENT_DIR_PATH=os.path.dirname(__file__)
    TEST_FIXTURE_REL_PATH="../Sample/test_100.csv"
    TEST_FIXTURE_PATH=os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)
    excel = pandas.read_csv(TEST_FIXTURE_PATH, index_col=0)
    print(excel.head())
    aggregation = statistics.Aggregation(excel)

    # 평균값
    # aggregation.mean('나이')
    # 최댓값
    # aggregation.max('나이')
    # 최솟값
    # aggregation.min('나이')
    # 최빈값
    # aggregation.mode('나이')
    # 중간값
    median_value = aggregation.median('나이')

    # I think 45 is median value from the fixture field '나이'
    for value in median_value:
        assert value == 45
    print(excel.head())
