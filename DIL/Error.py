def test_statistics_aggregation():
    CURRENT_DIR_PATH=os.path.dirname(__file__)
    TEST_FIXTURE_REL_PATH="../Sample/test_100.csv"
    TEST_FIXTURE_PATH=os.path.join(CURRENT_DIR_PATH, TEST_FIXTURE_REL_PATH)
    
class Error(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)