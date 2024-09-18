
import pyttsx3

# robo speaking code is here
def robo(message):
    speak= pyttsx3.init()
    speak.setProperty('rate',100)
    speak.say(message)
    speak.runAndWait()

# calling robo function
robo("this is class program test with constructor ")
robo("in this program we adding two number and printing table of given number")

# this is class you can give any name
class family:
    def __init__(self,a,b):
        self.a = a
        self.b= b

# adding program code
    def adding(self):
        print(f"some of {self.a} and {self.b} is : {(self.a+self.b)}")
        robo(f"some of {self.a} and {self.b} is : {(self.a+self.b)}")

# table program code
    def table(slef):
        robo("do you want print table")
        t=input("do you want print table ? y/n : ")
        
        if(t=="y"):
            robo("please enter the number, wich number of you want to print table")
            enter=int(input("\nplease enter : "))
            robo(f"do you want to print table of {enter}, ok here we go")
            print("\n")
            for i in range(1,11):
                print(f"{enter} X {i} = {enter*i}")
                
            robo("do you want to speak that table by robo")    
            say=input("do you want to speak that table by robo ? y/n : ")
            
            # here robo speaking table code
            if(say=="y"):
                for i in range(1,10):
                    robo(f"{enter} into {i} = {enter*i}")
            else:
                robo("ok no problem, bye bye ")
        else:
            robo("ok no problem, bye bye")

# taking input for adding two number from user
a = int(input("please enter the first number : "))
b = int(input("please enter the second number : "))

robo("now we adding given two number ")
f=family(a,b) # creating object 
f.adding() # calling adding function
f.table() # calling table function 
