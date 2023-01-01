from practice1 import *

def test_min_int_list():
    list = [6,4,2,7,3,9]
    assert min_int_list(list) == 2

def test_sqrt():
    assert round(sqrt(2), 2) == 1.41
    assert round(sqrt(4), 2) == 2.00
    assert round(sqrt(5), 2) == 2.24

def test_cal_circumference():
    assert round(cal_circumference(1), 2) == 6.28
    assert round(cal_circumference(2.6), 2) == 16.34

def test_cal_angle():
    A, B, C = cal_angle(1, math.sqrt(3), 2)
    assert (round(A, 2), round(B, 2), round(C, 2)) == (30, 60, 90)
    A, B, C = cal_angle(1, math.sqrt(2), 1)
    assert (round(A, 2), round(B, 2), round(C, 2)) == (45, 90, 45)