# TODO: 사용자 모듈 import
from func_nums import even_odd, get_avg, get_max, get_min


# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_always():
    assert True == even_odd(10)
    assert 3 == get_avg([1,2,3,4,5])
    assert 100 == get_max([1,2,3,46,7,8,90,100])
    assert -1 == get_min([20,12,5,9,2,-1,19,590])