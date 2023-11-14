print('''
     YUSUF AND SONS LIMITED
        Balance manager
    Kindly enter the information below;
''')

principal = float(input('Please enter your AMOUNT; '))
TIME = float(input('Please enter your TIME; '))
RATE= float(input('Please enter your RATE; '))
NO_OF_TIME = float(input('please enter number of time intrest applied per time period; '))

Simple_intrest = (principal *(1+ RATE * TIME))
Conpound_intrest =(principal * (1 + RATE/ NO_OF_TIME) ** (RATE * TIME))

print(f'simple intrest = {Simple_intrest}')
