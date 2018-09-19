import numpy as np
import math

class Gradient:
    def __init__(self,dataIn,dataOut): #constructor
        self.dataIn=dataIn
        self.dataOut=dataOut
        self.normalized_dataIn = self.normalizeDataIn()[0]
        self.normalized_dataOut = self.normalizeDataOut()[0]
    #we need ot normalize the data to optimize to proccess
    def normalizeDataIn(self):
        list_means=[]
        noAttributes=len(self.dataIn[0])
        n=len(self.dataOut)
        for i in range(noAttributes):
            sum=0
            for el in self.dataIn:
                sum=sum+el[i]
            list_means.append(sum/n)
        list_deviation = []
        for i in range(noAttributes):
            sum=0
            for el in self.dataIn:
                sum=sum+(el[i]-list_means[i])**2
            list_deviation.append(math.sqrt(sum/(n-1)))
        normalized_dataIn=[]
        for i in range(n):
            li=[]
            for j in range(len(self.dataIn[i])):
                li.append((self.dataIn[i][j]-list_means[j])/list_deviation[j])
            normalized_dataIn.append(li)
        #denormalization
        #a=normalized_dataIn[0][0]
        #print(a*list_deviation[0]+list_means[0])
        #print("normaized data",normalized_dataIn)
        return [normalized_dataIn,list_means,list_deviation]
    #normalization for the output
    def normalizeDataOut(self):
        n=len(self.dataOut)
        sum=0
        for i in range(n):
            sum=sum+self.dataOut[i][0]
        mean=sum/n
        dev=0
        for i in range(n):
            dev=dev+(self.dataOut[i][0]-mean)**2
        dev_rate=math.sqrt(dev/(n-1))
        normalized_dataOut=[]
        for i in range(n):
            normalized_dataOut.append([(self.dataOut[i][0]-mean)/dev_rate])
        return [normalized_dataOut,mean,dev_rate]
    #we will use this function when we test our learning program
    def normalize_oneData(self,data):
        l=self.normalizeDataIn()
        for i in range(len(data[0])):
            data[0][i]=(data[0][i]-l[1][i])/l[2][i]
        return data
    # we will use this function to display the real output after the process of prediction which will be still normalzied
    def denormalize_dataOut(self,dataOut):
        l=self.normalizeDataOut()
        dataOut=dataOut*l[2]+l[1]
        return dataOut
    def constructInputMatrix(self): #data initialy given as bidimensional list
        input=self.normalized_dataIn
        Matrix=np.array(input)
        return Matrix
    def constructOutMatrix(self):
        l=self.normalized_dataOut
        l=np.array(l)
        return l
    def constructCoeffMatrix(self): #we have 7 features for each data row so we have to initialize 7+1(free) coefficient which will later be learnt
        m=len(self.dataIn[0])
        l=np.random.rand(m,1)
        l=np.array(l)
        coef=[[0.5] for i in range(m)]
        coef=np.array(coef)
        return coef
    #gradient function
    def gradientDescent(self,x, y, theta, alpha, num_iters): #BGD , the cost function is 1/2m sum_1,m (y_hat-y)^2
        """
           Performs gradient descent to learn theta
        """
        m = y.size  # number of training examples
        for i in range(num_iters):
            y_hat = np.dot(x, theta)
            theta = theta - alpha * (1.0 / m) * np.dot(x.T, y_hat - y)
        return theta
    def run_gradient(self):
        maxiter=10000
        input=self.constructInputMatrix()
        out=self.constructOutMatrix()
        coef=self.constructCoeffMatrix()
        learning_rate=0.001
        return self.gradientDescent(input,out,coef,learning_rate,maxiter)
    #prediction function
    def model(self,input):
        copy=input[0].copy()
        input=[copy]
        print(input)
        input = self.normalize_oneData(input)
        input=np.array(input)
        res = input.dot(self.run_gradient())
        return self.denormalize_dataOut(res[0][0])
