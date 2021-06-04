
def calcarea(r):
    area = 3.14159 * r * r
    return area

r = int(input("원의 반지름 : "))
print("반지름이", r , "인 원의 면적은", area, "입니다.")


def calcArea(b, h):
    area = b * h
    return area

base = int(input("밑변의 길이 : "))
height = int(input("높이의 길이 : "))
recArea = calcArea(base, height)
print("밑변과 높이가", base, height, "인 사각형의 면적은", recArea, "입니다.")

