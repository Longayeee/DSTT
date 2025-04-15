import numpy as np

A = np.random.randint(1,101,(10,10))
B = np.random.randint(1,21,(2,10))
C = np.random.randint(1,21,(10,2))
print("MA TRAN A: \n",A)
print("MA TRAN B: \n",B)
print("MA TRAN C: \n",C)

#Yeu cau a
print("YEU CAU a")
result = A + A.T + np.dot(C , B)+ np.dot((B.T),(C.T))
print("Dap an cau a: \n")
print(result)

#Yeu cau b
print("Yeu cau b")
result = 0
for i in range(1,11):
    result += ( A / (9 + i) ) ** i
print("Dap an cau b: ")
print(result)

#Yeu cau c
print("Yeu cau c")
arrOfOdd= []
for row in A:
    for num in row:
        if num % 2 != 0:
            arrOfOdd.append(num)
print("Dap an cau C: ")
print(np.array(arrOfOdd))

#Yeu cau d
print("Yeu cau d")
arrOfPrimes = []
for row in A:
    for num in row:
        if num > 1:
            for i in range (2,int(num ** 0.5)  + 1):
                if num % i == 0:
                    break
            else: 
                arrOfPrimes.append(num)
print("Dap an cau D: ")
print(np.array(arrOfPrimes))

#Yeu cau e
print("Yeu cau e")
maxCount = 0
result = []
for row in A:
    count = 0
    for num in row:
        if num > 1:
            for i in range (2,int(num ** 0.5)  + 1):
                if num % i == 0:
                    break
            else: 
                count += 1
    if count > maxCount:
        maxCount = count
        result = [row]
    elif count == maxCount:
        result.append(row)
print("Dap an cau e")
print(np.array(result)) 

#yeu cau f
print("Yeu cau f")
maxCountOdd = 0
resultOdd = []
for row in A:
    count = 0
    for num in row:
        if num % 2 != 0:
            count+=1
    if count > maxCountOdd:
        maxCountOdd = count
        resultOdd = [row]
    elif count == maxCountOdd:
        resultOdd.append(row)
print("Dap an cau f")
print(np.array(resultOdd))