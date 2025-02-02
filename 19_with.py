# with -> 클로즈 할필요 없음 , 보다 수월한 파일 퀴즈 
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_files: 
    study_files.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_files: 
    print(study_files.read() )

'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 
보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

- x 주차 주간 보고 - 
부서 : 
이름 : 
업무 요약 : 

1주차붙 3주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오. 

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다. 
''' 

for i in range(1, 4): 
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file: # 다시 실행하면 덮어쓰기 
        report_file.write("-{0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")

