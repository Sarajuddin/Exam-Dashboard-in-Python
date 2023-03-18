import csv
import pandas as pd
from cryptography.fernet import Fernet

with open('key.txt', 'r') as file:
    key = file.read()
    key = key.lstrip("b'").rstrip("'")
    b = bytes(key, 'UTF-8')
    fernet = Fernet(b)

def studentDisplay():
    print("\n\tPress 1 - New Registration | Sign Up")
    print("\tPress 2 - Have already Account? | Sign in")
    print("\tPress 3 - Quit app")
    ch = input("\tPress any button given above : ")
    return ch

def studentWrite(data):
    # Encrypt the data first...
    encMessage = fernet.encrypt(data[1].encode())
    data[1] = encMessage
    with open('students_login.csv', mode = 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(data)
        print("\n\tAccount is Created Successfully...\n")

def studentRead(lst):
    data = []
    flag = False
    with open('students_login.csv', mode = 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if row[0] == lst[0]:
                d = row[1].lstrip("b'").rstrip("'")
                decMessage = fernet.decrypt(d)
                decMessage = str(decMessage).lstrip("b'").rstrip("'")
                if decMessage == lst[1]:
                    data.append(row)
                    break
                else:
                    print("\n\tWrong Password \n")
                    flag = True
                    break
    return data, flag

def studentDashboard():
    print("\n\tPress 1 - Start Test")
    print("\tPress 2 - View Result")
    print("\tPress 3 - Log Out")
    ch = input("\tEnter you choice : ")
    return ch

def questionRead():
    questions = []
    options = []
    answers = []
    with open('questions.csv', mode = 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            questions.append(row[0])
            options.append(row[1:])
    with open('answers.csv', mode = 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            answers.append(row)
    return questions, options, answers


def startExam(email, name):
    print("\n\t################ Examination Portal ################\n\n")
    questions, options, answers = questionRead()
    count, sum, myans = 0, 0, []
    for question, option in zip(questions, options):
        count += 1
        print("\n\tQuestion - {} : {}".format(count, question))
        print('\t', f'{f"A : {option[0]}":<30}{f"C : {option[2]}":<30}')
        print('\t', f'{f"B : {option[1]}":<30}{f"D : {option[3]}":<30}')
        while True:
            lst = [['A'], ['B'], ['C'], ['D'], ['A','B'], ['A','C'], ['A','D'], ['B','A'], ['B','C'], ['B','D'], ['C','A'], ['C','B'], ['C','D'], ['D','A'], ['D','B'], ['D','C']]
            ans = input("\tEnter Your Answer : ").upper().split()
            if ans in lst:    
                myans.append(ans)
                break
            else:
                print("\n\tPlease Enter 'A,B,C,D' only\n")
    # print("MyAns : ",myans)
    final = []
    for answer in answers:
        # print('Answer : ', answer)
        r = []
        for ans in answer:
            # print(ans)
            x = ans[0]
            if x == '[':
                y = ans.lstrip('[')
                y = y.rstrip(']')
                r.append(y)
        # print('r : ', r)
        final.append(r)
    # print("Final Ans : ", final)
    for ans1, ans2 in zip(final, myans):
        if ans1 == ans2:
            sum += 10
    flag, count = readResult(email)
    if flag:
        df = pd.read_csv("students_result.csv")
        df.loc[count-1, 'Percentage'] = str(sum)
        df.to_csv("students_result.csv", index=False)
    else:
        details = list((email, name, str(sum)))
        with open('students_result.csv', mode = 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(details)
        print("\n\tYour score has been stored...")
    return sum

def getStudentResult(email):
    res = []
    with open('students_result.csv', 'r') as file:
        results = csv.reader(file)
        for result in results:
            if email == result[0]:
                res.append(result)
                return res 
    return res

def readResult(email):
    flag, count = False, 0
    with open('students_result.csv', 'r') as file:
        results = csv.reader(file)
        for result in results:
            if email == result[0]:
                flag = True
                return flag, count
            count += 1
    return flag, count