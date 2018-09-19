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
    def runMethod1(self):
        m1= Method1(self.getFromFileInput(),self.getStreamOut1())
        m2 = Method1(self.getFromFileInput(), self.getStreamOut2())
        m3 = Method1(self.getFromFileInput(), self.getStreamOut3())
        print("The liniear model has been solved\n")
        new_in=self.getFromFileTest()
        new_out=self.getOutFromFileTest()
        for index in range(len(new_in)):
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


            print("FLOW(cm)")
            print(res2[0][0])
            print("Real result: ")
            print(new_out[index][1])

            print("Compressive Strength (28-day)(Mpa)")
            print(res3[0][0])
            print("Real result: ")
            print(new_out[index][2])
    def runMethod2(self):

        new_in=self.getFromFileTest()
        new_out=self.getOutFromFileTest()
        for index in range(len(new_in)):
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


            print("FLOW(cm)")
            print(res2)
            print("Real result: ")
            print(new_out[index][1])

            print("Compressive Strength (28-day)(Mpa)")
            print(res3)
            print("Real result: ")
            print(new_out[index][2])
    def runMethod3(self):

        new_in=self.getFromFileTest()
        new_out=self.getOutFromFileTest()
        for index in range(len(new_in)):
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


            print("FLOW(cm)")
            print(res2[0][0])
            print("Real result: ")
            print(new_out[index][1])

            print("Compressive Strength (28-day)(Mpa)")
            print(res3[0][0])
            print("Real result: ")
            print(new_out[index][2])


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

fileI="In.txt"
fileT="test.txt"
ui=UI(fileI,fileT)
ui.run()






