def check(data:list, privacyListAdd=None):
    privacyList = ['이름', '성명', '주민등록번호', '주소','운전면허번호', '전화번호', '생년월일', '생일', '이메일', '이메일 주소']

    if privacyListAdd:
        privacyList.append(privacyListAdd)

    result = set(privacyList) & set(data)

    return list(result)