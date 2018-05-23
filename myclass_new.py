import random

class Matrix:
    def __init__(self, s, p):
        self.stroka = s
        self.stolbec = p
        self.matrix = []
        for i in range(self.stroka):
            self.matrix.append([])
            for j in range(self.stolbec):
                self.matrix[i].append(random.randint(0,4))

    def printMat(self):
        for i in range(self.stroka):
            print(self.matrix[i])
        print("\n")


    def __add__(self, other):
        if (self.stroka == other.stroka) and (self.stolbec == other.stolbec):
            result = Matrix(self.stroka, self.stolbec)
            for i in range(self.stroka):
                for j in range(self.stolbec):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            print("Сложение матриц не может быть выполнено")
            return 1

    def __sub__(self, other):
        if (self.stroka == other.stroka) and (self.stolbec == other.stolbec):
            result = Matrix(self.stroka, self.stolbec)
            for i in range(self.stroka):
                for j in range(self.stolbec):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        else:
            print("Вычитание матриц не может быть выполнено")
            return 1

    def __mul__(self, other):
        if type(other).__name__ == 'int':
            result = Matrix(self.stroka, self.stolbec)
            for i in range(self.stroka):
                for j in range(self.stolbec):
                    result.matrix[i][j] = self.matrix[i][j] * other
            return result
        elif self.stolbec == other.stroka:
            result = Matrix(self.stroka, other.stolbec)
            for i in range(self.stroka):
                for j in range(other.stolbec):
                    res = 0
                    for k in range(self.stolbec):
                        res += self.matrix[i][k]*other.matrix[k][j]
                    result.matrix[i][j] = res
            return result
        else:
            print("Умножение матриц не может быть выполнено")
            return 1

    def transp(self):
        result = Matrix(self.stroka, self.stolbec)
        trans = []
        for stolbec in range(self.stolbec):
            trans_vl = []
            for stroka in range(self.stroka):      
                trans_vl.append(self.matrix[stroka][stolbec])
            trans.append(trans_vl)
        for i in range(self.stolbec):
            print(trans[i])
        print("\n")

    
    def del_stroka(self,pos):
        del self.matrix[pos]
        self.stroka -= 1

    def del_stolbec(self,pos):
        for i in range(self.stroka):
            del self.matrix[i][pos]
        self.stolbec -= 1

    
    def det(self):
        if self.stroka == self.stolbec:
            if self.stroka == self.stolbec == 1:
                det = 0
                det = self.matrix[0][0]
                return det
            elif self.stroka == self.stolbec == 2:
                det = 0
                det = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrisa[0][1]
                return det
            elif self.stroka == self.stolbec == 3:
                det = 0
                det += self.matrix[0][0] * self.matrix[1][1]* self.matrix[2][2] + self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0] + self.matrix[1][0] * self.matrix[2][1] * self.matrix[0][2]
                det -= self.matrix[0][2] * self.matrix[1][1]* self.matrix[2][0] + self.matrix[1][0] * self.matrix[0][1] * self.matrix[2][2] + self.matrix[1][2] * self.matrix[2][1] * self.matrix[0][0]
                return det
            else:
                det = 0
                for stolbec in range(self.stolbec):
                    result = Matrix(self.stroka, self.stolbec)
                    
                    result.matrix = [row[:] for row in self.matrix]
                    
                    result.del_stroka(0)
                    result.del_stolbec(stolbec)

                    det += self.matrix[0][stolbec] * pow(-1,stolbec) * result.det()
            return det
        else:
            print("Определитель матрицы не может быть найден")
            return 'ch'
