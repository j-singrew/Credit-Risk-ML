# User credit risk ML

# Dataset: https://www.kaggle.com/competitions/home-credit-default-risk/rules


# ------------------------------------------------------------------------------
application_{train|test}.csv

This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET).
Static data for all applications. One row represents one loan in our data sample.
bureau.csv

All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample).
For every loan in our sample, there are as many rows as number of credits the client had in Credit Bureau before the application date.
bureau_balance.csv

Monthly balances of previous credits in Credit Bureau.
This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample * # of relative previous credits * # of months where we have some history observable for the previous credits) rows.
POS_CASH_balance.csv

Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit.
This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credits * # of months in which we have some history observable for the previous credits) rows.
credit_card_balance.csv

Monthly balance snapshots of previous credit cards that the applicant has with Home Credit.
This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credit cards * # of months where we have some history observable for the previous credit card) rows.
previous_application.csv

All previous applications for Home Credit loans of clients who have loans in our sample.
There is one row for each previous application related to loans in our data sample.
installments_payments.csv

Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample.
There is a) one row for every payment that was made plus b) one row each for missed payment.
One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample.
HomeCredit_columns_description.csv

This file contains descriptions for the columns in the various data files.

# ------------------------------------------------------------------------------



# Constant columns dropped 
'FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_10', 
'FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_13', 
'FLAG_DOCUMENT_14', 'FLAG_DOCUMENT_15', 
'FLAG_DOCUMENT_16', 'FLAG_DOCUMENT_17', 
'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_20', 
'FLAG_DOCUMENT_21'







<class 'pandas.DataFrame'>
RangeIndex: 48744 entries, 0 to 48743
Columns: 121 entries, SK_ID_CURR to AMT_REQ_CREDIT_BUREAU_YEAR
dtypes: float64(65), int64(40), str(16)
memory usage: 45.0 MB

COMMONAREA_MEDI
Type: Numeric
Mean: 0.04742038166437143
Median: 0.0223
Std: 0.08289220472380317

COMMONAREA_AVG
Type: Numeric
Mean: 0.047623660567906095
Median: 0.0227
Std: 0.08286838501819505

COMMONAREA_MODE
Type: Numeric
Mean: 0.04522303757623451
Median: 0.0203
Std: 0.08116860365377804

NONLIVINGAPARTMENTS_AVG
Type: Numeric
Mean: 0.009231480158472428
Median: 0.0
Std: 0.048749133634451255

NONLIVINGAPARTMENTS_MODE
Type: Numeric
Mean: 0.008357543677339742
Median: 0.0
Std: 0.04665724760400763

NONLIVINGAPARTMENTS_MEDI
Type: Numeric
Mean: 0.008978853023316233
Median: 0.0
Std: 0.0481484727382851

FONDKAPREMONT_MODE
Type: Categorical
Mode: ['reg oper account']
Unique: 4

LIVINGAPARTMENTS_AVG
Type: Numeric
Mean: 0.10588525432222501
Median: 0.0756
Std: 0.09828404908036381

LIVINGAPARTMENTS_MODE
Type: Numeric
Mean: 0.11087422951641193
Median: 0.0817
Std: 0.10398023527429018

LIVINGAPARTMENTS_MEDI
Type: Numeric
Mean: 0.10706329240791781
Median: 0.077
Std: 0.09973684264328671

FLOORSMIN_MEDI
Type: Numeric
Mean: 0.23784589015849616
Median: 0.2083
Std: 0.1652405974727326

FLOORSMIN_MODE
Type: Numeric
Mean: 0.233853986976287
Median: 0.2083
Std: 0.16503366529247926

FLOORSMIN_AVG
Type: Numeric
Mean: 0.23842308637424744
Median: 0.2083
Std: 0.16497617383590416

OWN_CAR_AGE
Type: Numeric
Mean: 11.786027263875365
Median: 9.0
Std: 11.462889058395241

YEARS_BUILD_MODE
Type: Numeric
Mean: 0.7583271475835992
Median: 0.7583
Std: 0.11011699165902865

YEARS_BUILD_AVG
Type: Numeric
Mean: 0.7511370908661231
Median: 0.7552
Std: 0.11318840747735055

YEARS_BUILD_MEDI
Type: Numeric
Mean: 0.7543436192839419
Median: 0.7585
Std: 0.11199767626463705

LANDAREA_MODE
Type: Numeric
Mean: 0.0659141093216203
Median: 0.0462
Std: 0.08287959725837203

LANDAREA_MEDI
Type: Numeric
Mean: 0.06806901903367497
Median: 0.0488
Std: 0.08286871426926247

LANDAREA_AVG
Type: Numeric
Mean: 0.06719209370424598
Median: 0.0483
Std: 0.0819089788783152

BASEMENTAREA_MEDI
Type: Numeric
Mean: 0.08952910012794389
Median: 0.0778
Std: 0.0810221902577918

BASEMENTAREA_MODE
Type: Numeric
Mean: 0.088998071364261
Median: 0.077
Std: 0.08265495448475493

BASEMENTAREA_AVG
Type: Numeric
Mean: 0.09006548358053357
Median: 0.0781
Std: 0.08153631903677132

NONLIVINGAREA_AVG
Type: Numeric
Mean: 0.029387290379523385
Median: 0.0038
Std: 0.07200747319379941

NONLIVINGAREA_MODE
Type: Numeric
Mean: 0.02816147837599294
Median: 0.0012
Std: 0.07350403224802061

NONLIVINGAREA_MEDI
Type: Numeric
Mean: 0.02929628861429832
Median: 0.0031
Std: 0.07299797314345019

ELEVATORS_AVG
Type: Numeric
Mean: 0.08516829547866696
Median: 0.0
Std: 0.13916433740886155

ELEVATORS_MEDI
Type: Numeric
Mean: 0.08412821057100403
Median: 0.0
Std: 0.13901437595658261

ELEVATORS_MODE
Type: Numeric
Mean: 0.08056993844194438
Median: 0.0
Std: 0.13750937436042784