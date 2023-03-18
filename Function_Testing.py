import csv
import pandas as pd
from cryptography.fernet import Fernet
import pdb

# key1 = Fernet.generate_key()
# print(key1, type(key1))
# with open('key.txt', 'w') as file:
#     file.write(str(key1))
#     print("Key is generated...")
with open('key.txt', 'r') as file:
    key = file.read()
    print(key, type(key))
    key = key.lstrip("b'").rstrip("'")
    b = bytes(key, 'UTF-8')
    print("\nKey : ", b, type(b))
    fernet = Fernet(b)
    print(fernet)

def encrypt(lst):
    # lst = ['lakshya@gmail.com', '12345']
    encMessage = fernet.encrypt(lst[1].encode())  
    print("\noriginal string: ", lst[1])
    print("\nencrypted string: ", encMessage)
    # print(type(encMessage))
    # encMessage = encMessage.lstrip('b')
    # data = list((email, encMessage))
    lst[1] = encMessage
    print(lst)
    with open('encryption.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(lst)
        print("\n\tData inserted....\n")

def decrypt(lst):
    with open('encryption.csv', 'r') as file:
        rows = csv.reader(file)
        data = []
        for row in rows:
            if lst[0] == row[0]:
                data.append(row)
                break
    print(data)
    d = data[0][1].lstrip("b'").rstrip("'")
    # print("\nData : ", bytes(d, 'UTF-8'))
    # print(type(d))
    decMessage = fernet.decrypt(d)
    # print("\ndecrypted string: ", decMessage)
    # print(type(decMessage))
    s = str(decMessage).lstrip("b'").rstrip("'")
    data[0][1] = s
    print(data)
    print("Password is matched...")


lst = ['lakshya@gmail.com', '12345']
# encrypt(lst)
decrypt(lst)

def codingDecoding():
    lst = ['lakshya@gmail.com', '12345']
    
    encMessage = fernet.encrypt(lst[1].encode())  
    print("\noriginal string: ", lst[1])
    print("\nencrypted string: ", encMessage)
    # print(type(encMessage))
    # encMessage = encMessage.lstrip('b')
    # data = list((email, encMessage))
    lst[1] = encMessage
    print(lst)
    with open('encryption.csv', 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(lst)
        print("\nData inserted....")

    with open('encryption.csv', 'r') as file:
        rows = csv.reader(file)
        data = []
        for row in rows:
            if lst[0] == row[0]:
                data.append(row)
                break
    print(data)
    d = data[0][1].lstrip("b'").rstrip("'")
    # print("\nData : ", bytes(d, 'UTF-8'))
    # print(type(d))
    decMessage = fernet.decrypt(d)
    # print("\ndecrypted string: ", decMessage)
    # print(type(decMessage))
    s = str(decMessage).lstrip("b'").rstrip("'")
    data[0][1] = s
    print(data[0])
    print("Password is matched...")

# codingDecoding()


# # updating the column value/data
# score = '70'
# email = 'saraju@gmail.com'
# df.loc[0, 'Percentage'] = score

# # writing into the file
# df.to_csv("students_result.csv", index=False)

# print(df)

# def updateFile():
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

def updateFile():
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

# updateFile()


def writeQuestions():
    # fields = ['Email', 'Password']
    # rows = [['Which of the following is the correct extension of the Python file', '.python', '.pl', '.py', '.p'],
    #         ['All keywords in Python are in _________', 'Capitalized', 'lower case', 'UPPER CASE', 'None of the Mentioned'],
    #         ['What will be the value of the following Python expression? 4 + 3 % 5', '7', '2', '4', '1'],
    #         ['Which of the following is used to define a block of code in Python language?', 'Indentation', 'Key', 'Brackets', 'All of the above'],
    #         ['Which keyword is used for function in Python language?', 'function', 'def', 'fun', 'define'],
    #         ['Which of the following character is used to give single-line comments in Python?', '//', '#', '!', '/*'],
    #         ['Which of the following is not a core data type in Python programming?', 'Tuple', 'Lists', 'Class', 'Dictionary'],
    #         ['What will be the output of the following Python function? len(["hello",2, 4, 6])', 'Error', '6', '4', '3'],
    #         ['Which one of the following is not a keyword in Python language?', 'pass', 'eval', 'assert', 'nonlocal'],
    #         [' Which of the following statements is used to create an empty set in Python?', '()', '[]', '{}', 'set()']]
    # answers = [['C'], ['D'], ['A'], ['A'], ['B'], ['B'], ['C'], ['C'], ['B'], ['D']]
    details = [['Email', 'Name', 'Percentage']]
    with open('students_result.csv', mode = 'w', newline='') as file:
        # rows = csv.reader(file)
        csvwriter = csv.writer(file)
        # csvwriter.writerow(fields)
        csvwriter.writerows(details)
        print("File is Created...")
# writeQuestions()

def readFile():
    data = []
    with open('admin_login.csv', mode = 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            print(row)
            # data.append(row)

    # return data
# readFile()
# data = readFile()
# print(data)
def readResult():
    with open('answers.csv', 'r') as file:
        answers = csv.reader(file)
        # print("File is read.")
        a = 'B'
        sum = 0
        for answer in answers:
            for ans in answer:
                x = ans[0]
                # print(x)
                # print(x)
                if x == '[':
                    if a == ans[1]:
                        print("Answer Matched", ans)
                        sum += 10
                        print(sum)
# readResult()