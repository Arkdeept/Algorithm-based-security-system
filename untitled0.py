#Arkdeept's sequrity system
#I am try to creat a security system where a intermidiate algorithm is requried so to access inside the page 
#we can put a mathematical algorithm in between so which only know to the user and that algorithm is never 
#into the system so tracking the password is next to imposival because it's password changes with every new otp 
def check_user_name(username): # cheaking if the user name contains alphabets as well as numbers 
    if len(username) > 8:
        flag = False
        for char in username:
            if char.isdigit():
                flag = True
                break
        if not flag :
            print("your user name should cantain digits also")
            return False
        flag = False
        for char in username:
            if char.isalpha():
                flag = True
                break
        if not flag:
            print("your user name should contain alphabets also")
            return False
        return True
    print("your user name should contain atleast 8 characters")
    return False
print("We are going to create a account for you")
flag = False
while flag != True:
    user_name = input("plaese craete your user name:- ")
    if check_user_name(user_name):
        print("Okay user name accepted")
        flag = True
print("Okay now we will create your continous variable password ")
print("your password will be always different so you need to select the four opration from bellow")
print("+ , - , * , ^ ")
opration_input = ['+','-','*','^']
master_flag = False
while not master_flag:
    flag = False
    while not flag:
        first_opration_row = input("select your first operation : ")
        if first_opration_row not in opration_input:
            print("select properly,incorrect selection, select and type as written above")
        else:
            flag = True
    flag = False
    while not flag:
        second_opration_row = input("select your second operation : ")
        if second_opration_row not in opration_input:
            print("select properly,incorrect selection, select and type as written above")
        else:
            flag = True
    flag = False
    while not flag:
        third_opration_row = input("select your third operation : ")
        if third_opration_row not in opration_input:
            print("select properly,incorrect selection, select and type as written above")
        else:
            flag = True
    if first_opration_row == second_opration_row == third_opration_row:
        print("please select different operation type for above three type of operation")
    else:
        master_flag = True
flag = False
while not flag:
    forth_opration_row = input("select your fourth opration : ")
    if forth_opration_row not in opration_input:
        print("select properly,incorect selection, select and type as written above")
    else:
        flag = True
dictionary = [user_name,first_opration_row,second_opration_row,third_opration_row,forth_opration_row]
print('congrats your variable password is created')
store = open('password.txt','w')
store.write(','.join(dictionary))
print('The way of generating password is -')
print('example otp = 12345 \n opration are +,-,+,^ \n Then password will be ((((1+2)-3)+4)^5) ')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

