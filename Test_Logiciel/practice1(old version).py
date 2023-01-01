import math

def min_int_list(input_list):
    # Trouver la valeur minimale dans une liste
    min_value = input_list[0]
    for value in input_list:
        if value < min_value:
            min_value = value
    return min_value

def sqrt(number):
    #Trouver la racine carrée par dichotomie
    low, up = 0, number
    mid = (low + up) / 2
    precision = 1e-6
    while abs(mid ** 2 - number) > precision:
        mid = (low + up) / 2
        if mid ** 2 > number:
            up = mid
        if mid ** 2 < number:
            low = mid
    return mid

def cal_circumference(radius):
    # L'entrée par défaut est le rayon
    return radius * math.pi * 2

def cal_angle(a, b, c):
    # Calcule trois angles à partir de trois côtés, en appliquant la formule triangle cosinus
    cos_a = (c ** 2 + b ** 2 - a ** 2) / (2 * b * c)
    cos_b = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    cos_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    A = math.degrees(math.acos(cos_a))
    B = math.degrees(math.acos(cos_b))
    C = math.degrees(math.acos(cos_c))
    return A, B, C
