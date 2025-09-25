import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


class Multi_disease:
    def __init__(self):
        pass

    def ckd_Fun(self,df):
        

        if set(df.columns == ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu',
          'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad',
          'appet', 'pe', 'ane', 'classification']) == {True}:
          
          df.columns = [ 'age','blood_pressure','specific_gravity','albumin','sugar','red_blood_cell','platelet_count',
               'prothrombin_complex_concentrate','basophils','blood_glucose_random','blood_urea','serum_creatinine',
               'sodium','potassium','hemoglobin','packed_cell_volume','white_blood_cell','red_cell_count','hypertension',
               'diabetes_mellitus','coronary_artery_disease','appetite','pulmonary_edema','anemia','classification']
        else:
            df.columns = df.columns

        df = df.replace("?", np.nan)

        return df
    
    def cld_Fun(self,df):

            df.columns = [i.lower() for i in df.columns]

            for i in df.select_dtypes(include='object').columns:
                df[i] = df[i].apply(lambda x: x.lower())
            
            df.reset_index(drop=True,inplace=True)

            if 'AST/ALT_rati0' in df.columns:
                df = df
            else:
                df['AST/ALT_ratio'] = df['aspartate_aminotransferase'] / df['alamine_aminotransferase']
 
            df = df[['age', 'gender', 'total_bilirubin', 'direct_bilirubin',
                'alkaline_phosphotase', 'alamine_aminotransferase',
                'aspartate_aminotransferase', 'AST/ALT_ratio', 'total_protiens', 'albumin',
                'albumin_and_globulin_ratio' ]]
            
            return df
    
    def pd_Fun(self,df):
            pass
