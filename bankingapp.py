options = input("Welcome to Mozo Bank! Please click on the option below" 
      '\n Click 1 Withdraw: '
      '\n Click 2 Deposit: '
      '\n Click 3 Exit:\n')

if options=='1':
    balance = int(input('Enter your balance: '))
    withdraw = int(input('Enter the amount you want to withdraw: '))
    if balance < withdraw:
        print('Insufficient funds')
    else:
        print('New balance: ', (balance - withdraw))

elif options=='2':
    balance = int(input('Enter your balance: '))
    deposit = int(input('Enter the amount you want to deposit: '))
    print('New balance: ', (balance + deposit))