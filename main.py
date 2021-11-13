import os

from Functions import *

if __name__ =="__main__":
    os.system('cls')
    while True:
        print("--------------------------------------------------")
        print("1. 프로그램 시작 ")
        print("2. 식판 사진 찍기 ")
        print("3. 도움말 ")
        print("4. 프로그램 종료 ")
        print("--------------------------------------------------")
        select = int(input("1,2,3 중의 하나의 숫자를 입력하시오: "))
        os.system('cls')
        if select == 1:
            startProgram() # 프로그램 시작 함수
        elif select == 2:
            TakePlatePhoto() # 식판 사진 찍기
        elif select == 3:
            print("--------------------------------------------------")
            print("1. 프로그램 시작: 음식 부피 측정 프로그램을 시작합니다.")
            print("2. 식판 사진 찍기: 식판 사진을 찍습니다.")
            print("3. 도움말: 프로그램을 설명합니다.")
            print("--------------------------------------------------")
            input("Enter를 입력하여 나가기")
            os.system('cls')
        elif select == 4:
            exit()
        else:
            print("Wrong Input")
