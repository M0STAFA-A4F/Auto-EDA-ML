import pandas as pd
import numpy as np
import json


class DataFrame:
    all = None
    features = None
    target = None
    
    def read_file(self, file):
        fname_split = file.name.split('.')
        df = None
        
        if fname_split[-1] == 'csv':
            df = pd.read_csv(file)
        
        elif fname_split[-1] == 'xlsx':
            df = pd.read_excel(file)
        
        elif fname_split[-1] == 'json':
            string_data = file.getvalue().decode('utf-8')
            json_data = json.loads(string_data)
            df = pd.json_normalize(json_data)
            df = df.replace('', None)
        
        return df

    def remainder_col(self, features_name, all_columns):
        return list(set(all_columns) - set(features_name))
    
    def prediction_type(self, threshold=0.05):
        '''
        0 -> Classification
        1 -> Regression
        '''
        df_target = self.target
        df_target = pd.DataFrame(df_target)
        dtype = str(df_target.dtypes).split()
        
        if dtype[1] == 'float64':
            return 1
        
        elif dtype[1] == 'int64':
            unique_ratio = len(np.unique(df_target)) / len(df_target)
            
            if unique_ratio < threshold:
                return 0
            else:
                return 1
        
        else:
            return 0
