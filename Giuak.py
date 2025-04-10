import numpy as np

A = np.random.randint(1,101,size = (10,10))
B = np.random.randint(1,21,size = (2,10))
C = np.random.randint(1,21,size = (10,2))
print("MA TRAN A: \n",A)
print("MA TRAN B: \n",B)
print("MA TRAN C: \n",C)

#Yeu cau a: Tinh bieu thuc va in ra man hinh console
print("YEU CAU a")
result = 0
result = A + A.T + np.dot(C , B)+ np.dot((B.T),(C.T))
print("Dap an cau a: \n")
print(result)

#Yeu cau b: Tinh bieu thuc dang phan so co luy thua va in ra man hinh console
print("Yeu cau b")
result = 0
for i in range(1,11):
    result += ( A / (9 + i) ) ** i
print("Dap an cau b: ")
print(result)

#Yeu cau c: Luu cac so le cua ma tran thanh 1 vecto moi va in ra man hinh console
print("Yeu cau c")
arrOfOdd= []
for row in A:
    for num in row:
        if num % 2 != 0:
            arrOfOdd.append(num)
print("Dap an cau C: ")
print(np.array(arrOfOdd))

#Yeu cau d:Luu cac so nguyen to cua ma tran thanh 1 vecto moi va in ra man hinh console
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

#Yeu cau e: Tim hang co nhieu so nguyen to nhat va in ra man hinh console
# A = [[2,2,2,1,2],[1,2,2,1,2],[2,2,2,1,2]]
print("Yeu cau e")
index = 0
result = []
for row in A:
    save = []
    for num_n in row:
        if num_n > 1:
            for i in range (2,int (num_n**(1/2)+1)):
                if num_n % i == 0:
                    break
            else: 
                save.append(num_n)
    count = len(save)
    if index < count:
        index = count
        result = [row]
    elif index == count:
        result.append(row)
print("Dap an cau e")
print(np.array(result)) 

# rs = [];
# maxCount = 0;
# for row in A:
#     count = 0
#     for el in row:
#         isPrime = el > 1
#         for i in range(2, int(el ** 0.5) + 1):
#             if el % i == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             count+=1
#     if count > maxCount:
#         maxCount = count
#         rs = [row];
#     elif count == maxCount:
#         rs.append(row);
# print(np.array(rs))

#Yeu cau f:
