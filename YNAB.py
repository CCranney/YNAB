import os
import pandas as pd


class YNAB:
    def __init__(self):
        if not os.path.isdir('data'):
            os.makedirs('data')
            pd.DataFrame(data=[], columns=['Amount','Account','Memo', 'Month']).to_csv('data/income.csv', index=False)
            pd.DataFrame(data=[], columns=['TargetCategory','PriorCategory','Amount','Month']).to_csv('data/assignments.csv', index=False)
            pd.DataFrame(data=[], columns=['Category','Amount','EndMonth']).to_csv('data/regularPayments.csv', index=False)
            pd.DataFrame(data=[], columns=['Category','Amount','Account','Month']).to_csv('data/expenses.csv', index=False)
