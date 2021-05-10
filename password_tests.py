# Authors:
# grace.lin@slu.edu
# lili.hostetler@slu.edu

from password import PasswordGenerator
import unittest

symbol=list('!@#$%^&*<>?:;=~()\|/_{}`')
capitals=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

class BasicTest(unittest.TestCase):

    def testUpper(self):
        '''
        Tests if the randomly generated password has an uppercase letter.
        '''
        password=PasswordGenerator()
        key=password.passwordGenerator()
        self.assertTrue(any(k.isupper() for k in key))

    def testLower(self):
        '''
        Tests if the randomly generated password has an lowercase letter.
        '''
        password=PasswordGenerator()
        key=password.passwordGenerator()
        self.assertTrue(any(k.islower() for k in key))

    def testLength(self):
        '''
        Tests if the randomly generated password has a length of 8.
        '''
        password=PasswordGenerator()
        key=password.passwordGenerator()
        self.assertTrue(len(key)>=8)

    def testSymbol(self):
        '''
        Tests if the randomly generated password has a symbol.
        '''
        password=PasswordGenerator()
        key=password.passwordGenerator()
        self.assertTrue(any(k.isalpha() for k in key))

if __name__ == '__main__':
    unittest.main()
    
