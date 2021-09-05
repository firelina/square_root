import pytest
from main import calculate


class TestCalculate:

    def test_int(self):
        assert calculate('4', '0') == '±2'
        assert calculate('8', '3') == '±2.828'

    def test_float(self):
        assert calculate('5.98', '7') == '±2.4454039'

    def test_complex_num(self):
        assert calculate('-4', '1') == '±2.0j'
        assert calculate('4 + 5j', '3') == '±2.28∓1.096j'
        assert calculate('5j + 4', '3') == '±2.28∓1.096j'

    def test_null(self):
        assert calculate('0', '0') == '0'

    def test_num_float_incor(self):
        assert calculate('7,9', '1') in ['Please, enter a number', 'Por favor, introduzca un número', '请输入数字', 'Пожалуйста, введите число']

    def test_not_num(self):
        assert calculate('78 98', '0') in ['Please, enter a number', 'Por favor, introduzca un número', '请输入数字', 'Пожалуйста, введите число']
        assert calculate('78 98 67', '0') in ['Please, enter a number', 'Por favor, introduzca un número', '请输入数字',
                                      'Пожалуйста, введите число']

    def test_string(self):
        assert calculate('uyliutyli', '0') in ['Please, enter a number', 'Por favor, introduzca un número', '请输入数字', 'Пожалуйста, введите число']
        assert calculate('%1', '0') in ['Please, enter a number', 'Por favor, introduzca un número', '请输入数字', 'Пожалуйста, введите число']

    def test_pre_incor(self):
        assert calculate('9', 'oiuopiu') in ['Incorrect input', 'Entrada incorrecta', '输入不正确', 'Неверный ввод']

    def test_pre_float(self):
        assert calculate('9', '8.9') in ['Incorrect input', 'Entrada incorrecta', '输入不正确', 'Неверный ввод']

    def test_pre_neg(self):
        assert calculate('9', '-8') in ['Incorrect input', 'Entrada incorrecta', '输入不正确', 'Неверный ввод']

    def test_big_num(self):
        assert calculate('18777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777783555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555556', '0') == '±4333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333334'
