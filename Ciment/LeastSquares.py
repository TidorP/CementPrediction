import numpy as np
from numpy.linalg import inv

class Method1:
    def __init__(self,dataIn,dataOut):
        self.dataIn=dataIn
        self.dataOut=dataOut
    #input matrix from files
    def constructInputMatrix(self):
        input=self.dataIn
        Matrix=np.array(input)
        return Matrix
    def constructOutMatrix(self):
        out=self.dataOut
        Matrix=np.array(out)
        return Matrix
    def getWeightsMatrix(self): # we follow the matrix formula y=XB+err to get the B weights
        input=self.constructInputMatrix()
        #print(input)
        input_trans=input.T
        res=input_trans.dot(input)
        res_inv=inv(res)
        result=res_inv.dot(input_trans)
        result=result.dot(self.constructOutMatrix())
        return result
    def getError(self):
        input = self.constructInputMatrix()
        out=self.constructOutMatrix()
        xB=input.dot(self.getWeightsMatrix())
        return out-xB
    # here the input is smth like x=(x1,x2,..,xm)
    def model(self,input):
        res=input.dot(self.getWeightsMatrix())
        return res



