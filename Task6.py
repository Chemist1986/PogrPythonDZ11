class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix) or self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions to be added.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns != other.rows:
                raise ValueError("The number of columns in the first matrix must match the number of rows in the second matrix.")
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        elif isinstance(other, int) or isinstance(other, float):
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] * other
            return result
        else:
            raise TypeError("Multiplication is only supported between matrices and scalars.")



matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

print(matrix1)           
print(matrix2)               
print(matrix1 == matrix2)  

matrix_sum = matrix1 + matrix2
print(matrix_sum)  
                   
matrix_scalar = matrix1 * 2
print(matrix_scalar) 
                      
matrix_product = matrix1 * matrix2
print(matrix_product)  
                      