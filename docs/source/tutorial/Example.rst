===============================
Example
===============================


데이터 분석 목적
===============================
| 최고급 객실 숙박 L사는 자신들의 고객들의 지역, 가족 관계, 재산을 분석하여 맞춤형 서비스를 만들고자 한다.
| 이 때문에 데이터 분석 전문 회사인 A사에 고객들의 데이터를 넘겨서 데이터 분석을 의탁하려 한다.

| 하지만 고객 정보를 그대로 데이터 분석 전문 회사 A사에 전달하면 법에 위촉이 됨으로, 최고급 객실 숙박 L사는 고객을 식별할 수 없도록 가명처리 후 전달해야한다.
| 이를 위해 DIL 라이브러리를 이용하여 가명처리를 하겠다.


L사의 고객 데이터
--------------------------------
해당 데이터셋은 DIL의 Sample 디렉토리에 ''example_dataset.csv''로 저장되어 있습니다.

read_csv.py 코드
``````````````````````````
.. code-block:: python

    import pandas

    datas = pandas.read_csv("../../Sample/example_dataset.csv", index_col=0)
    print(datas)

read_csv.py 실행
``````````````````````````
.. command-output:: python tutorial/code/read_csv.py


가명처리해야하는 데이터 정리
===============================

데이터 분석 시 필요한 데이터 선정
---------------------------------------
주소, 가족, 재산

식별자, 준식별자, 민감정보 선정
--------------------------------
* 식별자 : 이름, 핸드폰
* 준식별자 : 생년월일, 성별, 주소
* 민감정보 : 직업, 가족, 재산


가명처리 기술 표
===============================

+------------+------------+
|    이름    |    
+============+
|    삭제    |
+------------+