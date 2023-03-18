import csv
import pandas as pd
from cryptography.fernet import Fernet

with open('key.txt', 'r') as file:
    key = file.read()
    key = key.lstrip("b'").rstrip("'")
    b = bytes(key, 'UTF-8')
    fernet = Fernet(b)

def adminDisplay():
    print("\n\tPress 1 - New Registration | Sign Up")
    print("\tPress 2 - Have already Account? | Sign in")
    print("\tPress 3 - Quit app")
    ch = input("\tPress any button given above : ")
    return ch

def adminWrite(data):
    # Encrypt the data first...
    encMessage = fernet.encrypt(data[1].encode())
    data[1] = encMessage
    with open('admin_login.csv', mode = 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(data)
        print("\n\tAccount is Created Successfully...\n")

# lst = ['lakshya@gmail.com', '12345']
# adminWrite(lst)

def adminRead(lst):
    data = []
    flag = True
    with open('admin_login.csv', mode = 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if row[0] == lst[0]:
                # data.append(row)
                d = row[1].lstrip("b'").rstrip("'")
                decMessage = fernet.decrypt(d)
                decMessage = str(decMessage).lstrip("b'").rstrip("'")
                # print(decMessage)        
                if decMessage == lst[1]:
                    data.append(row)
                    break
                else:
                    print("\n\tWrong Password \n")
                    flag = False
                    break
    # print(data)
    # d = data[0][1].lstrip("b'").rstrip("'")
    # decMessage = fernet.decrypt(d)
    # s = str(decMessage).lstrip("b'").rstrip("'")
    # data[0][1] = s
    return data, flag

# lst = ['lakshya@gmail.com', '12345']
# data, flag = adminRead(lst)
# print(data)


def adminDashboard():
    print("\n\tPress 1 - View Records")
    print("\tPress 2 - Log Out")
    ch = input("\tEnter your choice : ")
    return ch

def adminAllRecord():
    with open('students_result.csv', mode = 'r') as file:
        rows = csv.reader(file)
        print()
        for row in rows:
            # print("\t{}\t\t{}\t\t{}".format(row[0], row[1], row[2]))
            print('\t', f'{f"{row[0]}":<50}{f"{row[1]}":<40}{f"{row[2]}":<40}')
            # print('\t', f'{f"B : {option[1]}":<30}{f"D : {option[3]}":<30}')
        else:
            print("\tNo More Record Found...")

# def adminUpdateFile():
#     df = pd.read_csv("answers.csv", header=None)
#     df = df.dropna()
#     lst = df.values.tolist()
#     for x in lst:
#         for i, ch in enumerate(x):
#             if ch[0] == '[' or ch[0] == ']':
#                 el = '['+ch[1].upper()+']'
#                 x[i] = el
#             elif ch[-1] == ']' or ch[-1] == '[':
#                 el = '['+ch[-2].upper()+']'
#                 x[i] = el
#             else:
#                 x[i] = ch.upper()
#     df = pd.DataFrame(lst)
#     df.to_csv("answers.csv", index=False, header=False)

def verifyAnswerFile():
    df = pd.read_csv("answers.csv", header=None)
    listoflist = df.values.tolist()
    for lst in listoflist:
        for ch in lst:
            if ch[0] == '[' and ch[-1] != ']':
                return False
            elif ch[-1] == ']' and ch[0] != '[':
                return False
            elif ch[0] == ']':
                return False
            elif ch[-1] == '[':
                return False
            else:
                continue
    return True