from myclass_new import *

A = Matrix(4,4)
B = Matrix(6,3)
print("Матрица А: ")
A.printMat()
print("Матрица В: ")
B.printMat()

C = A + B
if C != 1:
    print("Сложение матриц: A + B ")
    C.printMat()

D = A - B
if D != 1:
    print("Вычитание матриц: A - B")
    D.printMat()

E = A * 5
if E != 1:
    print("Умножение матрицы на число: А * 5")
    E.printMat()

F = A * B
if F != 1:
    print("Умножение двух матриц: А * В")
    F.printMat()


print("Транспонирование матрицы А: A^T")
A.transp()


if A.det() != 'ch':
    print("Определитель матрицы A = ", str(A.det()))
