# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
import pickle
import streamlit as st
from Fun import Multi_disease
MD = Multi_disease()

# Setting Page Configuration
st.set_page_config(page_title='Multiple Diseases Prediction', 
                   layout='wide',page_icon='💉')


def Ckd_Home():
    c1,c2 = st.columns([0.2,2])
    c1.image('ckd_logo.png')
    c2.title("Chronic Kidney Disease Prediction")

    ckd_model = pickle.load(open('ckd_model.pkl','rb'))

    form_data = {'age': None,
                'blood_pressure': None,
                'specific_gravity': None,
                'albumin': None,
                'sugar': None,
                'blood_glucose_random': None,
                'blood_urea': None,
                'serum_creatinine': None,
                'sodium': None,
                'potassium': None,
                'hemoglobin': None,
                'packed_cell_volume': None,
                'white_blood_cell': None,
                'red_cell_count': None,
                'red_blood_cell': None,
                'platelet_count': None,
                'prothrombin_complex_concentrate': None,
                'basophils': None,
                'hypertension': None,
                'diabetes_mellitus': None,
                'coronary_artery_disease': None,
                'appetite': None,
                'pulmonary_edema': None,
                'anemia': None}
    

    ########## Form layout ##########
    with st.form(key = 'Chronic Kidney Disease Prediction'):


        # Input fields
        c1,c2,c3,c4 = st.columns(4)
        form_data['age'] = c1.number_input('Age',min_value=1,max_value=120)
        form_data['blood_pressure'] = c2.number_input('Blood Pressure')
        form_data['specific_gravity'] = c3.number_input('Specific Gravity')
        form_data['albumin'] = c4.number_input('Albumin')

        c1,c2,c3,c4 = st.columns(4)
        form_data['sugar'] = c1.number_input('Sugar')
        form_data['blood_glucose_random'] = c2.number_input('Blood Glucose Random')
        form_data['blood_urea'] = c3.number_input('Blood Urea')
        form_data['serum_creatinine'] = c4.number_input('Serum Creatinine')

        c1,c2,c3,c4 = st.columns(4)
        form_data['sodium'] = c1.number_input('Sodium')
        form_data['potassium'] = c2.number_input('Potassium')
        form_data['hemoglobin'] = c3.number_input('Hemoglobin')
        form_data['packed_cell_volume'] = c4.number_input('Packed Cell Volume')

        c1,c2,c3,c4 = st.columns(4)
        form_data['white_blood_cell'] = c1.number_input('White Blood Cell Count')
        form_data['red_cell_count'] = c2.number_input('Red Cell Count')
        form_data['red_blood_cell'] = c3.selectbox('Red Blood Cell',options=['normal','abnormal'])
        form_data['platelet_count'] = c4.selectbox('Platelet Count',options=['normal','abnormal'])

        c1,c2,c3,c4 = st.columns(4)
        form_data['prothrombin_complex_concentrate'] = c1.selectbox('Prothrombin Complex Concentrate',options = ['notpresent','present'])
        form_data['basophils'] = c2.selectbox('Basophils',options = ['notpresent','present'])
        form_data['hypertension'] = c3.selectbox('Hypertension',options=['yes','no'])
        form_data['diabetes_mellitus'] = c4.selectbox('Diabetes Mellitus',options=['yes','no'])

        c1,c2,c3,c4 = st.columns(4)
        form_data['coronary_artery_disease'] = c1.selectbox('Coronary Artery Disease',options=['yes','no'])
        form_data['appetite'] = c2.selectbox('Appetite',options=['good','poor'])
        form_data['pulmonary_edema'] = c3.selectbox('Pulmonary Edema',options=['yes','no'])
        form_data['anemia'] = c4.selectbox('Anemia',options=['yes','no'])

        submit_button = st.form_submit_button(label = 'submit')

        if submit_button:
            st.success('Form Submitted Successfully')
            st.write('The Given Form Data is')
            st.table(form_data)
            data = pd.DataFrame(form_data,index=[0])
            result = (ckd_model.predict_proba(data)[:,1]>=0.2).astype('int')
            if result == 1:
                st.error('The person is having Chronic Kidney Disease')
            else:
                st.success('The person is not having Chronic Kidney Disease')
        
    ############# File Upload Layout to predict attrition #############
    file_upload = st.file_uploader('Upload CSV file for Bulk Prediction',type='csv',key='file_uploader')
    if file_upload is not None:
        df = pd.read_csv(file_upload,index_col=0)
        st.success('File Uploaded Successfully')
        df = MD.ckd_Fun(df)
        if 'classification' in df.columns:
            df.drop(columns=['classification'],inplace=True)
        
        result_df = (ckd_model.predict_proba(df)[:,1]>=0.2).astype('int')
        result_df = pd.DataFrame(
                            dict(zip(df.index,result_df)).items(),
                            columns=['id','classification']).set_index('id')
        
        result_df['classification'] = result_df['classification'].replace({1:'ckd',0:'notckd'})
        result_df = pd.merge(result_df,df,how='inner',on='id') 
        result_df_1 = result_df[result_df['classification']=='ckd']
        result_df_2 = result_df[result_df['classification']=='notckd']

        c1,c2 = st.columns(2)
        c1.error(f'The number of persons having Chronic Kidney Disease are {result_df_1.shape[0]}')
        c1.dataframe(result_df_1)
        c2.success(f'The number of persons not having Chronic Kidney Disease are {result_df_2.shape[0]}')
        c2.dataframe(result_df_2)
        

        


def Ckd_Prediction():
    st.title('Chronic Kidney Disease Prediction')

    



# Navigation
st.navigation([Ckd_Home,Ckd_Prediction],position='top').run()