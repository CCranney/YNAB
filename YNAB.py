import os
import pandas as pd


class YNAB:
    def __init__(self):
        if not os.path.isdir('data'):
            os.makedirs('data')
            pd.DataFrame(data=[], columns=['Amount','Account','Memo', 'Date']).to_csv('data/income.csv', index=False)
            pd.DataFrame(data=[], columns=['TargetCategory','PriorCategory','Amount','Month']).to_csv('data/assignments.csv', index=False)
            pd.DataFrame(data=[], columns=['Category','Amount','EndMonth']).to_csv('data/regularPayments.csv', index=False)
            pd.DataFrame(data=[], columns=['Category','Amount','Account','Date']).to_csv('data/expenses.csv', index=False)
        self.income = pd.read_csv('data/income.csv')
        self.assignments = pd.read_csv('data/assignments.csv')
        self.regularPayments = pd.read_csv('data/regularPayments.csv')
        self.expenses = pd.read_csv('data/expenses.csv')

    def add_income(self, amount, account, memo, date):
        self.income.loc[len(self.income.index)] = [amount, account, memo, date]
        self.income.to_csv('data/income.csv')
