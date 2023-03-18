import sys
import admin
import students
import stdiomask
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
while True:
    print("\n\t###############  Welcome to the Exam Portal  ###############\n\n")
    print("\tPress 1 - You are an Administrator")
    print("\tPress 2 - You are a Student")
    print("\tPress 3 - Quit app")
    m = input("\tSelect any one option : ")
    if m == '1':
        while True:
            print("\n\t##############  Admin DASHBOARD  ##############\n")
            ch = admin.adminDisplay()
            lst = []
            if ch == '1':
                email = input("\tEnter Email ID : ")
                password = stdiomask.getpass("\tEnter Password : ")
                lst = list((email, password))
                if(re.fullmatch(regex, email)):
                    row, flag = admin.adminRead(lst)
                    if not row and flag:
                        admin.adminWrite(lst)
                    else:
                        if flag:
                            print("\n\tAccount already exists\n")
                        else:
                            continue
                else:
                    print("\n\tInvalid Email ID\n")
            elif ch == '2':
                email = input("\tEnter Email ID : ")
                password = stdiomask.getpass("\tEnter Password : ")
                lst = list((email, password))
                if(re.fullmatch(regex, email)):
                    row, flag = admin.adminRead(lst)
                    if row and flag:
                        while True:
                            res = admin.adminDashboard()
                            if res == '1':
                                admin.adminAllRecord()
                            elif res == '2':
                                break
                            else:
                                print("\n\tPlease choose correct option\n")
                    else:
                        if not flag:
                            continue
                        print("\n\tRecord not found\n")                   
                else:
                    print("\n\tInvalid Email ID\n")
            elif ch == '3':
                print("\n\tThank You! 💖💖💖\n")
                sys.exit()
            else:
                print("\n\tPlease choose correct option\n")    
    elif m == '2':
        while True:
            print("\n\t##############  STUDENT DASHBOARD  ##############\n")
            ch = students.studentDisplay()
            lst = []
            if ch == '1':
                email = input("\tEnter Email ID : ")
                password = stdiomask.getpass("\tEnter Password : ")
                lst = list((email, password))
                if(re.fullmatch(regex, email)):
                    row, flag = students.studentRead(lst)
                    if not row and flag == False:
                        students.studentWrite(lst)
                    else:
                        print("\n\tAcount already exists\n")
                else:
                    print("\n\tInvalid Email ID\n")
            elif ch == '2':
                email = input("\tEnter Email ID : ")
                password = stdiomask.getpass("\tEnter Password : ")
                lst = list((email, password))

                if(re.fullmatch(regex, email)):
                    row, flag = students.studentRead(lst)
                    if row:
                        while True:
                            res = students.studentDashboard()
                            if res == '1':
                                # admin.adminUpdateFile()
                                ans_flag = admin.verifyAnswerFile()
                                if ans_flag:
                                    name = input("\n\tEnter Your Name : ")
                                    marks = students.startExam(email, name.title())
                                    print("\n\t{}!, You got {} %".format(name, marks))
                                else:
                                    print("\n\t🚫🚫🚫 'answer.csv' file is not in proper format. Please do changes and try again. 🚫🚫🚫")
                            elif res == '2':
                                result = students.getStudentResult(email)
                                if result:
                                    print("\n\tEmail ID\t\tName\t\tPercentage")
                                    print("\t{}\t\t{}\t\t{}".format(result[0][0], result[0][1], result[0][2]))
                                else:
                                    print("\n\tRecord Not Found...\n")
                            elif res == '3':
                                break
                            else:
                                print("\n\tPlease choose correct option\n")
                    else:
                        if flag:
                            continue
                        else:
                            print("\n\tRecord not found\n")                 
                else:   
                    print("\n\tInvalid Email ID\n")
            elif ch == '3':
                print("\n\tThank You! 💖💖💖\n")
                sys.exit()
            else:
                print("\n\tPlease choose correct option\n")
    elif m == '3':
        print("\n\tThank You! 💖💖💖\n")
        sys.exit()
    else:
        print("\n\tPlease choose correct option\n")