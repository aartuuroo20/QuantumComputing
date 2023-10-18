import numpy as np

class Matrix:
    def genMatrix(self):
        a = 1/np.sqrt(2)

        matrix = np.array([[a,0,0,0],
              [0,1.,0,0],
              [a,0,1.,0],
              [0,0,0,1.]])
        
        def gram_schmidt_columns(X):
            Q, R = np.linalg.qr(X)
            return Q
        
        matrix_aux = gram_schmidt_columns(matrix)


        

        
    

        

        


    
    
    