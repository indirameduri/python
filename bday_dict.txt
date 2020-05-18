'''
dictionaries
'''

bday = {'Leonardo da Vinci':'04/15/1452','Galileo Galilei':'02/15/1564','Isaac Newton': '12/25/1642','Charles Darwin':'02/12/1809','quit':''}
choice=''
while(choice != 'quit'):
    print('\nWelcome to birthday dictionary\n')
    for i in bday:
        print(i)

    print('\nWhose birthday would you like to know? ')
    choice = input()

    print(bday[choice])