import numpy as np

class Matrix:
    def genMatrix(self):
        matrix = np.array([[1,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0],
              [2.3,0,1,0,0,0,0,0],
              [5,0,0,1,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [0,0,0,0,0,1,0,0],
              [0,0,0,0,0,0,1,0],
              [0.43,0,0,0,0,0,0,1]])

        def gram_schmidt_columns(X):
            Q, R = np.linalg.qr(X)
            return Q
        
        self.matrix_aux = gram_schmidt_columns(matrix)

    def printMatrix(self):
        print(self.matrix_aux)


        

        
    

        

        


    
    
    
        

        
    

        