from Ciment.LeastSquares import *
from Ciment.Gradient import *
from Ciment.PSO import *
class UI:
    def __init__(self,fileIn,fileTest):
        self.fileIn=fileIn
        self.fileTest=fileTest

    def printCommands(self):
        print("1: Least Squares Root Method \n")
        print("2: Gradient Descend Metohd \n")
        print("3: Particle Swarm | Evolutive Metohd \n")
        print("4: Use a method that combines all three together to find the best predictions \n")
        print("0: Exit")
    def getFromFileInput(self):
        l = []
        with open(self.fileIn, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(7):
                    li.append(int(currentline[j + 1]))
                l.append(li)
        return l
    def getFromFileOut(self):
        l = []
        with open(self.fileIn, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(8,11):
                    li.append(float(currentline[j]))
                l.append(li)
        return l
    def getFromFileTest(self):
        l = []
        with open(self.fileTest, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(7):
                    li.append(float(currentline[j + 1]))
                l.append(li)
        return l
    def getOutFromFileTest(self):
        l = []
        with open(self.fileTest, "r") as filestream:
            for line in filestream:
                li = []
                currentline = line.split(",")
                for j in range(8,11):
                    li.append(float(currentline[j]))
                l.append(li)
        return l
    #first out
    def getStreamOut1(self):
        l=self.getFromFileOut()
        stream1=[]
        for x in l:
            stream1.append([x[0]])
        return stream1
    #second out
    def getStreamOut2(self):
        l=self.getFromFileOut()
        stream1=[]
        for x in l:
            stream1.append([x[1]])
        return stream1
    #third out
    def getStreamOut3(self):
        l=self.getFromFileOut()
        stream1=[]
        for x in l:
            stream1.append([x[2]])
        return stream1
    #we run our method here
    def checkAcc(self,found,real):
        if(math.fabs(math.floor(found)-math.floor(real))<=3):
            return True
        return False
    def runMethod1(self):
        m1= Method1(self.getFromFileInput(),self.getStreamOut1())
        m2 = Method1(self.getFromFileInput(), self.getStreamOut2())
        m3 = Method1(self.getFromFileInput(), self.getStreamOut3())
        print("The liniear model has been solved\n")
        new_in=self.getFromFileTest()
        new_out=self.getOutFromFileTest()
        acc=0
        predictions=[]
        for index in range(len(new_in)):
            p=[]
            print("We wil introduse this new input: \n")
            print(new_in[index])
            res1=m1.model(np.array([new_in[index]]))
            res2=m2.model(np.array([new_in[index]]))
            res3 = m3.model(np.array([new_in[index]]))
            print("Our prediction:\n")

            print("SLUMP(cm)")
            print(res1[0][0])
            print("Real result: ")
            print(new_out[index][0])
            p.append(res1[0][0])
            if(self.checkAcc(res1[0][0],new_out[index][0])):
                acc=acc+1

            print("FLOW(cm)")
            print(res2[0][0])
            print("Real result: ")
            print(new_out[index][1])
            p.append(res2[0][0])
            if (self.checkAcc(res2[0][0], new_out[index][1])):
                acc = acc + 1

            print("Compressive Strength (28-day)(Mpa)")
            print(res3[0][0])
            print("Real result: ")
            print(new_out[index][2])
            p.append(res3[0][0])
            if (self.checkAcc(res3[0][0], new_out[index][2])):
                acc = acc + 1
            predictions.append(p)
        print("Accuracy:",acc/(len(new_in)*3))
        return predictions
    def runMethod2(self):
        new_in=self.getFromFileTest()
        new_out=self.getOutFromFileTest()
        acc=0
        predictions=[]
        for index in range(len(new_in)):
            p=[]
            m1 = Gradient(self.getFromFileInput(), self.getStreamOut1())
            m2 = Gradient(self.getFromFileInput(), self.getStreamOut2())
            m3 = Gradient(self.getFromFileInput(), self.getStreamOut3())
            print("We wil introduse this new input: \n")
            print(new_in[index])
            copy=[new_in[index]]
            res1=m1.model(copy)
            res2= m2.model(copy)
            res3 = m3.model(copy)
            print("Our prediction:\n")

            print("SLUMP(cm)")
            print(res1)
            print("Real result: ")
            print(new_out[index][0])
            p.append(res1)
            if (self.checkAcc(res1, new_out[index][0])):
                acc = acc + 1


            print("FLOW(cm)")
            print(res2)
            print("Real result: ")
            print(new_out[index][1])
            p.append(res2)
            if (self.checkAcc(res2, new_out[index][1])):
                acc = acc + 1

            print("Compressive Strength (28-day)(Mpa)")
            print(res3)
            print("Real result: ")
            print(new_out[index][2])
            p.append(res3)
            if (self.checkAcc(res3, new_out[index][2])):
                acc = acc + 1
            predictions.append(p)
        print("Accuracy:", acc / (len(new_in) * 3))
        return predictions
    def runMethod3(self):
        new_in=self.getFromFileTest()
        new_out=self.getOutFromFileTest()
        acc=0
        predicitons=[]
        for index in range(len(new_in)):
            p=[]
            m1 = Method3(self.getFromFileInput(), self.getStreamOut1())
            m2 = Method3(self.getFromFileInput(), self.getStreamOut2())
            m3 = Method3(self.getFromFileInput(), self.getStreamOut3())
            print("We wil introduse this new input: \n")
            print(new_in[index])
            res1=m1.model([new_in[index]])
            res2=m2.model([new_in[index]])
            res3 = m3.model([new_in[index]])
            print("Our prediction:\n")

            print("SLUMP(cm)")
            print(res1[0][0])
            print("Real result: ")
            print(new_out[index][0])
            p.append(res1[0][0])
            if (self.checkAcc(res1[0][0], new_out[index][0])):
                acc = acc + 1


            print("FLOW(cm)")
            print(res2[0][0])
            print("Real result: ")
            print(new_out[index][1])
            p.append(res2[0][0])
            if (self.checkAcc(res2[0][0], new_out[index][1])):
                acc = acc + 1

            print("Compressive Strength (28-day)(Mpa)")
            print(res3[0][0])
            print("Real result: ")
            print(new_out[index][2])
            p.append(res3[0][0])
            if (self.checkAcc(res3[0][0], new_out[index][2])):
                acc = acc + 1
            predicitons.append(p)
        print("Accuracy:", acc / (len(new_in) * 3))
        return predicitons
    def calculateEstimate(self,w,first,second,third):
        total = w[0] + w[1] + w[2]
        return (w[0]*first+w[1]*second+w[2]*third)/total
    def runBest(self):
        predictions1=self.runMethod1()
        predictions2=self.runMethod2()
        predictions3=self.runMethod3()
        weights=[2,5,1]
        new_out = self.getOutFromFileTest()
        acc=0
        for index in range(len(predictions1)):
            print("Our prediction:\n")
            print("SLUMP(cm)")
            a=self.calculateEstimate(weights,predictions1[index][0],predictions2[index][0],predictions3[index][0])
            print(a)
            print("Real result: ")
            print(new_out[index][0])
            if (self.checkAcc(a, new_out[index][0])):
                acc = acc + 1

            print("FLOW(cm)")
            b = self.calculateEstimate(weights, predictions1[index][1], predictions2[index][1], predictions3[index][1])
            print(b)
            print("Real result: ")
            print(new_out[index][1])
            if (self.checkAcc(b, new_out[index][1])):
                acc = acc + 1

            print("Compressive Strength (28-day)(Mpa)")
            c = self.calculateEstimate(weights, predictions1[index][2], predictions2[index][2], predictions3[index][2])
            print(c)
            print("Real result: ")
            print(new_out[index][2])
            if (self.checkAcc(c, new_out[index][2])):
                acc = acc + 1
        print("Final Accuracy:", acc / (len(predictions1) * 3))
    def run(self):
        print("Welcome to our ML Algorithm for predicting Cement Size and Value given some real life data! \n")
        print("The entity has the atributes: ")
        print("Cement,Slag,Fly ash,Water,SP,Coarse Aggr,Fine Aggr.")
        print("Base on this we will find a model that can deduce the: future SLUMP(cm),FLOW(cm),Compressive Strength (28-day)(Mpa)\n")
        while(True):
            self.printCommands()
            i = input('Enter command: ')
            if(i=='0'):
                print("Bye")
                break
            if(i=='1'):
                self.runMethod1()
            if(i=='2'):
                self.runMethod2()
            if (i == '3'):
                self.runMethod3()
            if(i == '4'):
                self.runBest()

fileI="In.txt"
fileT="test.txt"
ui=UI(fileI,fileT)
ui.run()

