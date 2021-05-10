# Authors:
# grace.lin@slu.edu
# lili.hostetler@slu.edu

import random # importing the random module

class PasswordGenerator:
    login = [{'username': "", 'password': ""}]

    def __init__(self):
        '''
        Initialize the instances for lowercase letters, uppercase
        letters, symbols, and numbers.
        '''
        # putting each item into lists so that they are randomizable and iterable.
        self._lower = list('abcdefghijklmnopqrstuvwxyz')
        self._upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self._symbol = list('!@#$%^&*<>?:;=~()\|/_{}`')
        self._number = list('0123456789')

    def passwordGenerator(self, length = 8):
        '''
        This class method is responsible for the generation of the randomized,
        secure passwords.
        '''
        # combining all the initializes instances
        combine = self._lower + self._upper + self._symbol + self._number
        
        # choosing a random selection from the lists
        randLower = random.choice(self._lower)
        randUpper = random.choice(self._upper)
        randSymbol = random.choice(self._symbol)
        randNumber = random.choice(self._number)
        
        # adding together the random selections, hence, creating a random
        # temporary password. 
        temp_password = randLower + randUpper + randSymbol + randNumber

    
        for i in range(length - 4): # makes sure that it generates a password of length 8.
            temp_password += random.choice(combine) # creates a different password each time.
        return temp_password

    def store(self, user, password):
        '''
        This class method is responsible for storing login information of
        the user.
        '''
        self.login[0] = {user, password}

    def recall(self):
        '''
        This class method is responsible for recalling the login information of
        the user.
        '''
        login_ind = self.login
        for i in login_ind:
            return i

## Driver
##
##if __name__ == '__main__':
##    pw = PasswordGenerator()
##    pw.store('user1', pw.passwordGenerator())
##    print(pw.recall())
