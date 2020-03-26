
import sys
import pytest
sys.path.append("..")
from python.calc import Calc

'''
class Calc:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b
'''


class TestCalc(object):
    def test_add_int(self):
        assert Calc().add(0,1) == 1 and Calc().add(-1,0) == -1, '整数加法计算错误'

    def test_add_int_max(self):
        assert Calc().add(sys.maxsize,1) == sys.maxsize+1 , '限制了int类型计算'

    def test_add_float(self):
        assert Calc().add(0.01,0.99) == 1.00, '浮点数计算错误'

    def test_add_string01(self):
        assert Calc().add('1','2') == '12' , 'add不支持字符串数字计算'

    def test_add_string02(self):
        assert Calc().add('a','b') == 'ab' , 'add不支持字符串相加'

    def test_add_exception(self):
        with pytest.raises(TypeError):
            Calc().add('1',1)

    def test_add_param_exception(self):
        with pytest.raises(TypeError):
            Calc().add(1)

    def test_div_int(self):
        assert Calc().div(1,2) == 0.5

    def test_div_float(self):
        assert Calc().div(-1,0.5) == -2.0

    def test_div_zero_1(self):
        assert Calc().div(0,99) == 0

    def test_div_zero_2(self):
        with pytest.raises(ZeroDivisionError):
            Calc().div(99,0)

    def test_div_Exception(self):
        with pytest.raises(TypeError):
            Calc().div('99','99')


if __name__=='__main__':
    pytest.main('-v -s -k')