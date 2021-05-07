
def cirArea(r):
    return 3.14159 * r * r

def triArea(b, h):
    return 0.5 * b * h

def rectArea(b, h):
    return b * h

while True:
    print("0. 끝내기")
    print("1. 원의 면적 구하기")
    print("2. 사각형의 면적 구하기")
    print("3. 삼각형의 면적 구하기")
    choice = int(input("원하는 작업을 선택하세요. : "))

    if choice == 0:
        break
    elif choice == 1:
        rad = int(input("원의 반지름 입력 : "))
        print("반지름", rad, "인 원의 면적은", cirArae(rad))
    elif choice ==2:
        base = int(input("삼각형의 밑변 : "))
        height = int(input("삼각형의 높이 : "))
        print("밑변 높이", base, height, "삼각형의 면적은", triArea(base, height))
    elif choice ==3:
        base = int(input("사각형의 밑변 : "))
        height = int(input("사각형의 높이 : "))
        print("밑변 높이", base, height, "사각형의 면적은", rectArea(base, height))
    else:
        print("잘못된 선택입니다.")
