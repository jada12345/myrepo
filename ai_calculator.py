usrname = input("hi! whats your name?")
print("Welcome!",usrname,"Did you know I could do math?\n")
import time
time.sleep(3)
print("Im a bit dumb so please ask your questions 1 bit at a time " + "Here we go!\n")
import time
time.sleep(2)
print("FIRST OPERATION")
import time
time.sleep(1)

#variables:
add = "add"
minus = "minus"
times = "times"
divide = "divide"

def calc():
    #first op
    num_1 = input("what is your first number (can be a decimal or normal)?\n")
    operation = input("add,minus,times or divide\n")
    num_2 = input("what is your last number(can be a decimal or normal)?")

    if operation == add:
        print(num_1,"+",num_2,"=",float(num_1) + float(num_2))

    elif operation == minus:
        print(num_1,"-",num_2,"=",float(num_1) - float(num_2))

    elif operation == times:
        print(num_1,"*",num_2,"=",float(num_1) * float(num_2))

    elif operation == divide:
        print(num_1,"/",num_2,"=",float(num_1) / float(num_2))    

    import time
    time.sleep(1)

    another_question = input("\nanother question? yes or no?")    

    if another_question == "yes" or another_question == "Yes":
        calc()

    elif another_question == "no" or another_question == "No":
        print("Goodbye!")
    
calc()              
        
   

    


      
