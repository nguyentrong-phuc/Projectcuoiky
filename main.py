import pickle
import warnings

import numpy as np
import streamlit as st
import pandas as pd
warnings.filterwarnings("ignore")


st.title('Dự đoán chất lượng rượu vang: ')
col1, col2, col3 =st.columns(3)

# Id= np.str(col1.text_input("Id"))
fixed_acidity= np.str(col1.slider('fixed acidity', 0.0, 20.0, 5.0))
volatile_acidity= np.str(col2.slider('volatile acidity (g/L)', 0.00, 2.00, 0.55))
citric_acid= np.str(col3.slider('citric acid (g/L)', 0.00, 1.00, 0.55))
residual_sugar= np.str(col1.slider('residual sugar(g/L)', 0.00, 25.00, 10.00))
chlorides= np.str(col2.slider('chlorides', 0.000,0.001, 0.2, 0.001, format="%f"))
free_sulfur_dioxide= np.str(col3.slider('free sulfur dioxide'  ))
total_sulfur_dioxide= np.str(col1.slider('total sulfur dioxide', 0, 250, 100))
density= np.str(col2.text_input('density'))
pH= np.str(col3.slider('pH', 0.00, 5.00, 3.00))
sulphates= np.str(col1.slider('sulphates', 0.00, 2.00, 1.00))
alcohol= np.str(col2.slider('alcohol', 0.0, 25.0, 10.0 ))

features_num = ['fixed acidity','volatile acidity', 'citric acid',
                'residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide',
                'density','pH','sulphates', 'alcohol']
result= st.button('Dự đoán ')
sample=[ fixed_acidity,volatile_acidity, citric_acid,
         residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide, density,pH,sulphates, alcohol]
sample_df=pd.DataFrame([sample], columns=features_num)

model = pickle.load(open("finalized_model.sav","rb"))
if result:
    st.write('Chất lượng của rượu vang là:  ' , str(model.predict(sample_df)))


st.info('Bài tập lớn Trí tuệ nhân tạo - Trần Ngoan')
st.info('Mssv: K185480106014 ')
st.info(' Email:tvngoan343@gmail.com')
