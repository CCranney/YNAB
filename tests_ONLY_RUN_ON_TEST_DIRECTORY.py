import unittest
import YNAB
import os
import pandas as pd
import shutil

# import files/functions to test here, such as 'from mycode import *''
class MyTest(unittest.TestCase):

    #example code
    def test_YNAB_initialization(self):

        if os.path.isdir('data'): shutil.rmtree('data')

        self.YNAB = YNAB.YNAB()

        self.assertTrue(os.path.isdir('data'))

        self.assertTrue(os.path.isfile('data/income.csv'))
        income = pd.read_csv('data/income.csv')
        self.assertEqual(set(income.columns), set(['Amount','Account','Memo', 'Month']))

        self.assertTrue(os.path.isfile('data/assignments.csv'))
        assignments = pd.read_csv('data/assignments.csv')
        self.assertEqual(set(assignments.columns), set(['TargetCategory','PriorCategory','Amount','Month']))

        self.assertTrue(os.path.isfile('data/regularPayments.csv'))
        regularPayments = pd.read_csv('data/regularPayments.csv')
        self.assertEqual(set(regularPayments.columns), set(['Category','Amount','EndMonth']))

        self.assertTrue(os.path.isfile('data/expenses.csv'))
        expenses = pd.read_csv('data/expenses.csv')
        self.assertEqual(set(expenses.columns), set(['Category','Amount','Account','Month']))


if __name__ == '__main__':
    unittest.main()
