import os
import DepthCamera
from Essential_module import Plate_matrix
from Studentclass import *



def startProgram():
    studentList = {}
    menuNumber = int(input("Enter number of menu: "))
    while True:
        print("--------------------------------------------------")
        print("* 프로그램 이용 방식 *")
        print("1. 학번 입력 (example: 20xxxxxx)")
        print("2. 식판을 올려놓고 enter를 입력하여 사진 찍기")
        print("--> 음식을 먹기 전, 음식을 먹은 후 두 번 촬영")
        print("--> 최종 사진은 음식을 먹은 후 두번째 촬영 후 나오게 된다.")
        print("--------------------------------------------------")
        studentNumber = int(input("학번을 입력하십시오: "))
        os.system('cls')
        if studentNumber in studentList.keys():
            input("2차 측정: 식판을 올려놓고, enter를 입력하시오...")
            print("Loading...")
            matrix = DepthCamera.TakePhoto(None)
            studentList[studentNumber].saveSecondMatrix(matrix)
            # 부피 계산과정 후 사진 보여주기
            print("Calculated Volume: "+str(studentList[studentNumber].calculateSecondVolume())+'/'+str(studentList[studentNumber].calculateFirstVolume()))
            
            del studentList[studentNumber]

        else:
            newStudent = Student(studentNumber)
            input("1차 측정: 식판을 올려놓고, enter를 입력하시오...")
            print("Loading...")
            matrix = DepthCamera.TakePhoto(newStudent)
            newStudent.saveFirstMatrix(matrix)
            studentList[studentNumber] = newStudent



def TakePlatePhoto():
    input("식판을 올려놓은 후, enter를 입력하시오...")
    print("Loading...")
    Plate_matrix = DepthCamera.TakePhoto(None)

