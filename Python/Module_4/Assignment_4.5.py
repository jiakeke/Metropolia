"""
4. While loops (while)
    4.5. Write a program that asks the user for a username and password.
         If either or both are incorrect, the program ask the user to enter
         the username and password again. This continues until the login
         information is correct or wrong credentials have been entered five
         times. If the information is correct, the program prints out Welcome.
         After five failed attempts the program prints out Access denied.
         The correct username is python and password rules.

"""
_username = 'python'
_password = 'rules'

attempts = 5

print('Sign in!')
print('Please input the correct username and password to login.')
print('You have only 5 times to try.')

while attempts > 0:
    username = input('Username: ')
    password = input('Password: ')
    if username == _username and password == _password:
        print('Welcome!')
        break
    else:
        print('Username or password is invalid.')
        attempts -= 1
        print(f'You have {attempts} attempts left...')

else:
    print('Access denied!')

