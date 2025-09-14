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