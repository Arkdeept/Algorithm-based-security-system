#Arkdeept's sequrity system
#I am try to creat a security system where a intermidiate algorithm is requried so to access inside the page 
#we can put a mathematical algorithm in between so which only know to the user and that algorithm is never 
#into the system so tracking the password is next to imposival because it's password changes with every new otp 
import random
p = open('password.txt','r')
f = p.readline()
s = f.split(',')
print('LOGIN')
want_to_login = input('type YES to login else type NO \n')
if want_to_login.lower() == 'yes':
    username = input('Type the username:- ')
    if username == s[0]:
        OTP = random.randint(10000, 99999)
        print('OTP-',OTP)
        password = input('Type password:- ')
        OTP = str(OTP)
        check = 0
        for i in range(1,5):
            if i ==1:
                if s[i] == '+':
                    check = int(OTP[i-1])+int(OTP[i])
                elif s[i] == '-':
                    check = int(OTP[i-1])-int(OTP[i])
                elif s[i] == '*':
                    check = int(OTP[i-1])*int(OTP[i])
                elif s[i] == '^':
                    check = int(OTP[i-1])**int(OTP[i])   
            else:
                if s[i] == '+':
                    check = check+int(OTP[i])
                elif s[i] == '-':
                    check = check-int(OTP[i])
                elif s[i] == '*':
                    check = check*int(OTP[i])
                elif s[i] == '^':
                    check = check**int(OTP[i])
        print(check)
        if not password.isnumeric():
            print('sorry wrong password')
        else:
            if int(password) == check:
                print('you have sucessfully entered the account')
            else:
                print('sorry wrong password')
                
    else:
        print('wrong username')
else:
    print('Then why are you standing here')
    