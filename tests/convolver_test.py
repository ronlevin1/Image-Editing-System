from core.convolver import Convolver
import numpy as np

if __name__ == '__main__':
    kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
    kernel1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
    img1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
    img2 = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
    print(Convolver.apply_kernel(img2, kernel1))