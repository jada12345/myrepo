#password store beta vers 1.3 by Jad.A started on: 13/04/17 finished on: N/A
#password variables decrypter

b = 'a'
c = 'b'
d = 'c'
e = 'd'
f = 'e'
A = 'f'
Z = 'g'
Y = 'h'
I = 'i'
M = 'j'
L = 'k'
K = 'l'
J = 'm'
g = 'n'
a = 'o'
k = 'p'
T = 'q'
m = 'r'
O = 's'
q = 't'
s = 'u'
S = 'v'
o = 'w'
P = 'x'
i = 'y'
h = 'z'

z = 'A'
X = 'B'
t = 'C'
j = 'D'
R = 'E'
w = 'F'
x = 'G'
y = 'H'
p = 'I'
U = 'J' 
V = 'K'
v = 'L'
W = 'M'
u = 'N'
r = 'O'
Q = 'P'
N = 'Q'
n = 'R'
l = 'S'
H = 'T'
G = 'U'
F = 'V'
E = 'W'
D = 'X'
C = 'Y'
B = 'Z'

#password list

password_list = ['apple id', 'Bt','hotmail','youtube','psn']

#passwords DEC

APPLE_ID_DEC = (q + f + O + q + ' ' + k + b + O + O + o + a + m + e)
BT_DEC = (w + t + ' ' + X + b + m + d + f + K + a + u + z)
HOTMAIL_DEC = (U + z + j + M + b + e + U + z + j + M + b + e)
YOUTUBE_DEC = (str(1) + str(2) + str(1) + Y + b + Y + b + Y + b)
PSN_DEC = (k + b + O + O + str(1) + str(2) + str(3) + E + r + n + j)

#passwords ENC

APPLE_ID_ENC = ('qfOq kbOOoame')
BT_ENC = ('wt XbmdfKauz')
HOTMAIL_ENC = ('UzjMbeUzjMbe')
YOUTUBE_ENC = ('121YbYbYb')
PSN_ENC = ('kbOO123Ernj')

#password variables

password_1 = 'apple id'
password_2 = 'bt'
password_3 = 'hotmail'
password_4 = 'psn'

#password program

password_q = input('Input password ')

if (password_q != A + a + P + q + m + a + q + ' '):
    import time
    time.sleep(1)

    print('Incorrect, Try again')

elif (password_q == A + a + P + q + m + a + q + ' '):
    import time
    time.sleep(1)

    print('Password correct, Welcome to password store beta vers 1.3 by Jad.a \n')

    import time
    time.sleep(1)

while (password_q != A + a + P + q + m + a + q + ' '):
    password_q = input('Input password ')

    import time
    time.sleep(1)

    if (password_q != A + a + P + q + m + a + q + ' '):
        print('Incorrect, Try again')
       
    elif (password_q == A + a + P + q + m + a + q + ' '):
        print('Password correct, Welcome to password store beta vers 1.3 by Jad.a \n')
        import time
        time.sleep(1)

#main menu

main_menu_enter = input('would you like to enter the main menu?' + ' Type: Yes to enter, Type: No to exit then click enter ')

if ('no' in main_menu_enter or 'No' in main_menu_enter or main_menu_enter == 'n' or main_menu_enter == 'N'):
    print('Goodbye! ')

    import sys
    sys.exit()


elif ('yes' in main_menu_enter or 'Yes' in main_menu_enter or main_menu_enter == 'y' or main_menu_enter == 'Y'):
    print('Welcome to the main menu')

    import time
    time.sleep(1)

main_menu_choice = input('There are 2 options for you... You can view how many passwords are in the list or skip straight ahead and view a password: type 1 or 2 then press enter for what you would like to view ')

#main menu choice 2
if (main_menu_choice == '2'):
    password_view_choice = input('Would you like to view a known password? Type: Yes to enter the password viewer terminal, Type: No to exit then click enter ')

    print('These are the following passwords:')
    import time
    time.sleep(1)
    print('apple id')
    import time
    time.sleep(1)
    print('bt')
    import time
    time.sleep(1)
    print('hotmail')
    import time
    time.sleep(1)
    print('youtube')
    import time
    time.sleep(1)
    print('psn')
    import time
    time.sleep(1)

#main menu choice 1
elif (main_menu_choice == '1'):
    print('There are currently',len(password_list),'items in the password store')

    import time
    time.sleep(1)

    password_look = input('Would you like to view what passwords are in the list or exit? Type: Yes to look, Type: No to exit then click enter ')

    if ('no' in password_look or 'No' in password_look or password_look == 'n' or password_look == 'N'):
        print('Goodbye!')
        import sys
        sys.exit()

    elif ('yes' in password_look or 'Yes' in password_look or password_look == 'y' or password_look == 'Y'):

        print('These are the following passwords:')
        import time
        time.sleep(1)
        print('apple id')
        import time
        time.sleep(1)
        print('bt')
        import time
        time.sleep(1)
        print('hotmail')
        import time
        time.sleep(1)
        print('youtube')
        import time
        time.sleep(1)
        print('psn')
        import time
        time.sleep(1)

    password_view_choice = input('Would you like to view the password for one of the above? Type: Yes to enter the password viewer terminal, Type: No to exit then click enter ')


#part 3 for menu op 1, part 1 for menu op 2 as have same options so skip to this to save time 
if ('no' in password_view_choice or 'No' in password_view_choice or password_view_choice == 'n' or password_view_choice == 'N'):
    print('Goodbye!')
    import sys
    sys.exit()

elif ('yes' in password_view_choice or 'Yes' in password_view_choice or password_view_choice == 'y' or password_view_choice == 'Y'):    
    password_view = input('Please choose a password name to view its password. Type the password name you would like to view then click enter, please spell the name exactly from the previous given list. ')

    import time
    time.sleep(1)

    if ('apple id' in password_view):
        pass_choice = 'apple id'
        choice_pass_enc = 'qfOq0kbOOoame'
        choice_pass_dec = q + f + O + q + ' ' + k + b + O + O + o + a + m + e

    elif ('bt' in password_view):
        pass_choice = 'bt'
        choice_pass_enc = 'wt0XbmdfKauz'
        choice_pass_dec = w + t + ' ' + X + b + m + d + f + K + a + u + z

    elif ('hotmail' in password_view):
        pass_choice = 'hotmail'
        choice_pass_enc = 'UzjMbeUzjMbe'
        choice_pass_dec = U + z + j + M + b + e + U + z + j + M + b + e

    elif ('youtube' in password_view):
            pass_choice = 'youtube'
            choice_pass_enc = '121YbYbYb'
            choice_pass_dec = str(1) + str(2) + str(1) + Y + b + Y + b + Y + b

    elif ('psn' in password_view):
        pass_choice = 'psn'
        choice_pass_enc = 'kbOO123Ernj'
        choice_pass_dec = k + b + O + O + str(1) + str(2) + str(3) + E + r + n + j       

   

print('Please input the main password to view the following password:',choice_pass_enc,'the password is currently encrypted')

main_password = input('')  

if (main_password != U + b + e + ' ' + o + b + O + ' ' + Y + f + m + f):
    import time
    time.sleep(1)

    print('Incorrect, Try again')

elif (main_password == U + b + e + ' ' + o + b + O + ' ' + Y + f + m + f):
    import time
    time.sleep(1)

    print('Password correct, Decrypting',pass_choice,'password')

    import time
    time.sleep(3)

    print('Working...')

    import time
    time.sleep(4)

    print('Your password for',pass_choice,'is: ',choice_pass_dec)

    import time
    time.sleep(1.5)

    print('goodbye!')


while (main_password != U + b + e + ' ' + o + b + O + ' ' + Y + f + m + f):
    main_password = input('')

    import time
    time.sleep(1)

    if (main_password != U + b + e + ' ' + o + b + O + ' ' + Y + f + m + f):
        print('Incorrect, Try again')
       
    elif (main_password == U + b + e + ' ' + o + b + O + ' ' + Y + f + m + f):
        print('Password correct, Decrypting',pass_choice,'password')

        import time
        time.sleep(3)

        print('Working...')

        import time
        time.sleep(4)

        print('Your password for',pass_choice,'is: ',choice_pass_dec)

        import time
        time.sleep(1.5)

        print('goodbye!')

     



        
    







   

        




  

        





    


