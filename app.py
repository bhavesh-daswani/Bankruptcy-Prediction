import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
st.title('Bankruptcy Prediction')

st.sidebar.header('User Input Parameters')

def user_input_features():
    ROA_C = st.sidebar.number_input('ROA(C) before interest and depreciation before interest')
    ROA_A = st.sidebar.number_input('ROA(A) before interest and % after tax')
    ROA_B = st.sidebar.number_input('ROA(B) before interest and depreciation after tax')
    EPS_in_the_Last_Four = st.sidebar.number_input('Persistent EPS in the Last Four Seasons')
    Per_Share_Net_profit_before_tax = st.sidebar.number_input('Per Share Net profit before tax (Yuan)')
    Net_worth_by_Assets = st.sidebar.number_input('Net worth/Assets')
    Debt_ratio = st.sidebar.number_input('Debt ratio %')
    Net_profit_before_tax_by_Paidin_capital = st.sidebar.number_input('Net profit before tax/Paid-in capital')
    Retained_Earnings_to_Total_Assets = st.sidebar.number_input('Retained Earnings to Total Assets')
    Net_Income_to_Total_Assets = st.sidebar.number_input('Net Income to Total Assets')
    data = {'ROA_C':ROA_C,
            'ROA_A':ROA_A,
            'ROA_B':ROA_B,
            'EPS':EPS_in_the_Last_Four,
            'Per_Share_Net_profit_before_tax':Per_Share_Net_profit_before_tax,
            'Net_worth_by_Assets':Net_worth_by_Assets,
            'Debt_ratio ':Debt_ratio,
            'Net_profit_before_tax_by_Paidin_capital':Net_profit_before_tax_by_Paidin_capital,
            'Retained_Earnings_to_Total_Assets':Retained_Earnings_to_Total_Assets,
            'Net_Income_to_Total_Assets':Net_Income_to_Total_Assets}
    features = pd.DataFrame(data,index = [0])
    return features
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)
    
load_model= pickle.load(open('trained_model.sav','rb'))
prediction = load_model.predict(df)

   

if prediction == 1:
    output='The Company is Bankrupt'
else:
    output='The Company is Solvent'

st.subheader(output)






         
