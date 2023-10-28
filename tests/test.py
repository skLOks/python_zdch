# pytest

import pytest
from main import *

@pytest.mark.parametrize('x, exp_res',
						[(165, "Положительное"),
						(-21, "Отрицательное"),
						(0, "Ноль"),
						("фыв", "Это не число"),
						(-2, "Отрицательное")])
def testcod(x, exp_res):
	assert otr(x) == exp_res

@pytest.mark.parametrize('x, exp_res',
						[(6, "Чётное"),
						(-21, "Не чётное"),
						(8, "Чётное"),
						(19, "Не чётное"),
						("34", "Это не число")])
def testcode(x, exp_res):
	assert chyot(x) == exp_res

@pytest.mark.parametrize('x, exp_res',
						[("sda", "Это не число"),
						(23, 2),
						(1, 1),
						(4444, 4),
						(55555, 5)])
def testco(x, exp_res):
	assert kol(x) == exp_res

@pytest.mark.parametrize('x, exp_res',
						[([1, 2, 3, 4, 5], 15),
						(['sad', 21], "Введите нормальный список"),
						([4, 4, 4, 4], 16),
						([1], 1),
						([1.6, 432], 433.6)])
def testc(x, exp_res):
	assert sumlist(x) == exp_res

@pytest.mark.parametrize('x, exp_res',
						[('1,2,3,4,5', 15),
						('sadsa', "Что то не то, переделывай"),
						('4,4,4,4', 16),
						('1', 1),
						('1,432', 433)])
def test(x, exp_res):
	assert sumstr(x) == exp_res
