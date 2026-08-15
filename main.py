from config.logConfig import logging
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
#from data.__init__ import application_test,application_train,bureau_balance ,bureau,credit_card_balance,home_credit_column,installments,POS_cash,previous_application,sample_submission
try:    
    application_test = os.getenv("application_test")
    print(application_test )
    info_test = pd.read_csv(application_test)

except:
    print("nonei")
