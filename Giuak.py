
import numpy as np

A = np.random.randint(1,101,size = (10,10))
B = np.random.randint(1,21,size = (2,10))
C = np.random.randint(1,21,size = (10,2))
print("MA TRAN A: \n",A)
print("MA TRAN B: \n",B)
print("MA TRAN C: \n",C)

#Yeu cau a: Tinh bieu thuc va in ra man hinh console
print("YEU CAU a")
D = A + A.T + np.dot(C , B)+ np.dot((B.T),(C.T))
print("Dap an cau a: \n")
print("A + A.T+CB+(B.T)*(C.T)= \n",D)

#Yeu cau b: Tinh bieu thuc dang phan so co luy thua va in ra man hinh console
print("Yeu cau b")
E = 0
for i in range(1,11):
    E += (A/(9+i))**i
print ("Dap an cau b: ")
print (E)

#Yeu cau c: Luu cac so le cua ma tran thanh 1 vecto moi va in ra man hinh console
print("Yeu cau c")
arr_oldnum = []
for row in A:
    for num in row:
        if num % 2 != 0:
            arr_oldnum.append(num)
print("Dap an cau C: ")
print(np.array(arr_oldnum))

#Yeu cau d:Luu cac so nguyen to cua ma tran thanh 1 vecto moi va in ra man hinh console
print("Yeu cau d")
arr_primenum = []
for row in A:
    for n in row:
        if n > 1:
            for i in range (2,int (n**(1/2)+1)):
                if n % i == 0:
                    break
            else: 
                arr_primenum.append(n)
print("Dap an cau D: ")
print(np.array(arr_primenum))

#Yeu cau e: Tim hang co nhieu so nguyen to nhat va in ra man hinh console
print("Yeu cau e")
index = 0
result = []


#Yeu cau f:
