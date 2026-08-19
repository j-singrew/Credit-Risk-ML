from config.logConfig import logging
import os
from dotenv import load_dotenv
import duckdb



load_dotenv()
#from data.__init__ import application_test,application_train,bureau_balance ,bureau,credit_card_balance,home_credit_column,installments,POS_cash,previous_application,sample_submission
try:    
    application_test = os.getenv("application_test")
    duckdb.sql("SELECT 'whistling_duck' AS waterfowl, 'whistle' AS call")


except:
    print("nonei")
