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


# Chronic Kidney Dieses Prdiction Function
def CKD_Disease_Prediction():
    c1,c2 = st.columns([0.2,2])
    c1.image('ckd_logo.png')
    c2.title("Chronic Kidney Disease Prediction") # Seeting up Logo and Title

    ckd_model = pickle.load(open('ckd_model.pkl','rb')) # Model Importation

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
                'anemia': None} # Formdata 
    

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

        submit_button = st.form_submit_button(label = 'submit') # Submit Button

        if submit_button:
            st.success('Form Submitted Successfully')
            st.write('The Given Form Data is')
            st.table(form_data) # Genral info of input data
            data = pd.DataFrame(form_data,index=[0])
            result = (ckd_model.predict_proba(data)[:,1]>=0.2).astype('int') # Prdict CKD patients
            if result == 1:
                st.error('The person is having Chronic Kidney Disease')
            else:
                st.success('The person is not having Chronic Kidney Disease') # Result 
        
    ############# File Upload Layout to predict attrition #############
    file_upload = st.file_uploader('Upload CSV file for Bulk Prediction',type='csv',key='file_uploader')
    if file_upload is not None:
        df = pd.read_csv(file_upload,index_col=0)
        st.success('File Uploaded Successfully')
        df = MD.ckd_Fun(df) # Preprocessing Stpes
        if 'classification' in df.columns:
            df.drop(columns=['classification'],inplace=True)
        
        result_df = (ckd_model.predict_proba(df)[:,1]>=0.2).astype('int') # Predict the diease
        result_df = pd.DataFrame(
                            dict(zip(df.index,result_df)).items(),
                            columns=['id','classification']).set_index('id')
        
        result_df['classification'] = result_df['classification'].replace({1:'ckd',0:'notckd'})
        result_df = pd.merge(result_df,df,how='inner',on='id') 
        result_df_1 = result_df[result_df['classification']=='ckd']  # Reslt for CKD Patients
        result_df_2 = result_df[result_df['classification']=='notckd']      # Rsult for Non CKD Patients

        c1,c2 = st.columns(2)
        c1.error(f'The number of persons having Chronic Kidney Disease are {result_df_1.shape[0]}')
        c1.dataframe(result_df_1)
        c2.success(f'The number of persons not having Chronic Kidney Disease are {result_df_2.shape[0]}')
        c2.dataframe(result_df_2) 
        # Print the result in columns 
    st.markdown(open('ckd_info.md','r',encoding='utf-8').read(), unsafe_allow_html=True) # Genral medical lab ranges for ckd findings
        

# Chronic Liver Dieses Prediction Function 
def Liver_Disease_Prediction():
    c1,c2 = st.columns([0.2,2])
    c1.image('cld_logo.png')
    c2.title("Chronic Liver Disease Prediction") # Icon and Title

    cld_model = pickle.load(open('cld_model.pkl','rb')) # Import model

    form_data = {'age': None,
                'gender': None,
                'total_bilirubin': None,
                'direct_bilirubin': None,
                'alkaline_phosphotase': None,
                'alamine_aminotransferase': None,
                'aspartate_aminotransferase': None,
                'total_protiens': None,
                'albumin': None,
                'albumin_and_globulin_ratio': None} # Input lables
    
    ############## Form Layout #############
        
    with st.form(key = 'Chronic liver Disease Prediction'):

        c1,c2,c3,c4 = st.columns(4)
        form_data['age'] = c1.number_input('Age',min_value=1,max_value=120)
        form_data['gender'] = c2.selectbox('Gender',options=['male','female'])
        form_data['total_bilirubin'] = c3.number_input('Total Bilirubin')
        form_data['direct_bilirubin'] = c4.number_input('Direct Bilirubin')

        c1,c2,c3,c4 = st.columns(4)
        form_data['alkaline_phosphotase'] = c1.number_input('ALP (Alkaline Phosphatase)')
        form_data['alamine_aminotransferase'] =c2.number_input('ALT (Alanine Aminotransferase, SGPT)')
        form_data['aspartate_aminotransferase'] = c3.number_input('AST (Aspartate Aminotransferase, SGOT)')
        form_data['total_protiens'] =c4.number_input('Total Protein')

        c1,c2,c3,c4 = st.columns(4)
        form_data['albumin'] = c1.number_input('Albumin')
        form_data['albumin_and_globulin_ratio'] =c2.number_input('A/G Ratio')


        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.success("Form Submitted Successfully")
            st.write('The Given Form Data is')
            st.table(form_data)
            data = pd.DataFrame(form_data,index=[0]) 
            data = MD.cld_Fun(data) # Preprocessing
            result = cld_model.predict(data) # Prdict the Result

            if result == 0:
                st.success("The Patient is Healthy")
            if result == 1:
                st.error("The Patient having mild infection in Liver ")
            if result == 2:
                st.error("The Patient having moderate infection in Liver, need immediate care, may possible Chronic Liver Disease")
            if result == 3:
                st.error("The Patient having severe infection in Liver, need immediate care,Confirm Chronic Liver Disease")
            # Result Print

    ############# File Upload Layout to predict attrition #############
    file_upload = st.file_uploader('Upload CSV file for Bulk Prediction',type='csv',key='file_uploader')
    if file_upload is not None:
        df = pd.read_csv(file_upload) # Read Uploaded Data
        df = MD.cld_Fun(df)
        df['class'] =cld_model.predict(df)
        
        c1,c2 = st.columns(2)
        c1.success(f"Health Patients {df[df['class']==0].shape[0]}")
        c1.dataframe(df[df['class']==0])
        c2.error(f"Mild Live Infection Patients {df[df['class']==1].shape[0]}")
        c2.dataframe(df[df['class']==1])

        c1,c2 = st.columns(2)
        c1.error(f"Moderate Live Infection Patients (Possible Cld) {df[df['class']==2].shape[0]}")
        c1.dataframe(df[df['class']==2])
        c2.error(f"Severe Live Infection Patients (CLD) {df[df['class']==3].shape[0]}")
        c2.dataframe(df[df['class']==1])
        # Result print in columns
    st.markdown(open('cld_info.md','r',encoding='utf-8').read(), unsafe_allow_html=True) # Gneral lab result ranges for CLD cases

# Function for Parkinsond Dieses Prediction 
def Parkinsons_Disease_Prediction():
    c1,c2 = st.columns([0.2,2])
    c1.image('parkinsons_logo.png')
    c2.title("Parkinsons Disease Prediction") # Logo and Title

    parkinsons_model = pickle.load(open('parkinsons_model.pkl','rb')) # Import Model 

    form_data = {'MDVP:Fo(Hz)': None,
                'MDVP:Fhi(Hz)': None,
                'MDVP:Flo(Hz)': None,
                'MDVP:Jitter(%)': None,
                'MDVP:Jitter(Abs)': None,
                'MDVP:RAP': None,
                'MDVP:PPQ': None,
                'Jitter:DDP': None,
                'MDVP:Shimmer': None,
                'MDVP:Shimmer(dB)': None,
                'Shimmer:APQ3': None,
                'Shimmer:APQ5': None,
                'MDVP:APQ': None,
                'Shimmer:DDA': None,
                'NHR': None,
                'HNR': None,
                'RPDE': None,
                'DFA': None,
                'spread1': None,
                'spread2': None,
                'D2': None,
                'PPE': None,
               }  # From labels
    
    
    
    
    
    with st.form(key="Parkinsons Dieses Prediction"):

        ## user input data
        c1,c2,c3,c4 = st.columns(4)
        form_data['MDVP:Fo(Hz)'] = c1.number_input('MDVP\:Fo(Hz)')
        form_data['MDVP:Fhi(Hz)'] = c2.number_input('MDVP:Fhi(Hz)')
        form_data['MDVP:Flo(Hz)'] = c3.number_input('MDVP:Flo(Hz)')
        form_data['MDVP:Jitter(%)'] = c4.number_input('MDVP:Jitter(%)')

        c1,c2,c3,c4 = st.columns(4)
        form_data['MDVP:Jitter(Abs)'] = c1.number_input('MDVP:Jitter(Abs)')
        form_data['MDVP:RAP'] = c2.number_input('MDVP:RAP')
        form_data['MDVP:PPQ'] = c3.number_input('MDVP:PPQ')
        form_data['Jitter:DDP'] = c4.number_input('Jitter:DDP')

        c1,c2,c3,c4 = st.columns(4)
        form_data['MDVP:Shimmer'] = c1.number_input('MDVP:Shimmer')
        form_data['MDVP:Shimmer(dB)'] = c2.number_input('MDVP:Shimmer(dB)')
        form_data['Shimmer:APQ3'] = c3.number_input('Shimmer:APQ3')
        form_data['Shimmer:APQ5'] = c4.number_input('Shimmer:APQ5')

        c1,c2,c3,c4 = st.columns(4)
        form_data['MDVP:APQ'] = c1.number_input('MDVP:APQ')
        form_data['Shimmer:DDA'] = c2.number_input('Shimmer:DDA')
        form_data['NHR'] = c3.number_input('NHR')
        form_data['HNR'] = c4.number_input('HNR')

        c1,c2,c3,c4 = st.columns(4)
        form_data['RPDE'] = c1.number_input('RPDE')
        form_data['DFA'] = c2.number_input('DFA')
        form_data['spread1'] = c3.number_input('spread1')
        form_data['spread2'] = c4.number_input('spread2')

        c1,c2,c3,c4 = st.columns(4)
        form_data['D2'] = c1.number_input('D2')
        form_data['PPE'] = c2.number_input('PPE')

        submit_button = st.form_submit_button(label='Submit') # Submit button 

        if submit_button:
            st.success("Form Submitted Successfully")
            st.write('The Given Form Data is')
            form_data['spread1'] = form_data['spread1'] * -1 # Change Spreat column value to negative for accurate lab info
            data = pd.DataFrame(form_data,index=[0])
            st.table(form_data)
            result = parkinsons_model.predict(data) # Result find using model 
            st.write(result)


            if result == 0:
                st.success("The Patient is Healthy")
            if result == 1:
                st.error("The Patient having mild Parkinsons ")
            if result == 2:
                st.error("The Patient having moderate Parkinsons Diseases need immediate care")
            if result == 3:
                st.error("The Patient having severe Parkinsons Diseases")
            
            # Result print
            
            
    
    ############# File Upload Layout to predict attrition #############
    file_upload = st.file_uploader('Upload CSV file for Bulk Prediction',type='csv',key='file_uploader')
    if file_upload is not None:
        df = pd.read_csv(file_upload)  # Read input file

        df['class'] = parkinsons_model.predict(df) # Prdict the results using model 

        c1,c2 = st.columns(2)
        c1.success(f"Health Patients {df[df['class']==0].shape[0]}")
        c1.dataframe(df[df['class']==0])
        c2.error(f"Mild Parkinsons Disease Patients {df[df['class']==1].shape[0]}")
        c2.dataframe(df[df['class']==1])

        c1,c2 = st.columns(2)
        c1.error(f"Moderate Parkinsons Disease Patients {df[df['class']==2].shape[0]}")
        c1.dataframe(df[df['class']==2])
        c2.error(f"Severe Parkinsons Disease Patients (PD) {df[df['class']==3].shape[0]}")
        c2.dataframe(df[df['class']==3])

        # Print the Results data frame in 4 columns which determins the level of dieases 


    st.markdown(open('parkinsons_info.md','r',encoding='utf-8').read(), unsafe_allow_html=True) # Genral lab ranges for Parkinsons Dieses




# Navigation
st.navigation([CKD_Disease_Prediction,Liver_Disease_Prediction,Parkinsons_Disease_Prediction],position='top').run() 