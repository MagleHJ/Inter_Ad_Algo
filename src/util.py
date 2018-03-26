import pandas as pd
import numpy as np

def one_hot(dataset, feilds):
    def one_hot__(dataset, feild):
        df = pd.get_dummies(dataset[feild], prefix= feild)
        return pd.concat([dataset, df], axis=1)

    if not isinstance(dataset, pd.DataFrame):
        raise "The type of dataset is not DataFrame!"

    if isinstance(feilds, list) or isinstance(feilds, tuple):
        for feild in feilds:
            dataset = one_hot__(dataset, feild)
    elif isinstance(feilds, str):
        dataset = one_hot__(dataset, feilds)
    else:
        raise "Feilds is not a list/tuple/str arg!"
    
    return dataset


def min_max_scaling(dataset, feilds):
    def min_max_scaling_(dataset, feild):
        df = dataset[feild]
        df = (df - df.min()) / (df.max() - df.min())
        dataset[feild+'_after_min_max_scaling'] = df
        return dataset
    
    if not isinstance(dataset, pd.DataFrame):
        raise "The type of dataset is not DataFrame!"

    if isinstance(feilds, list) or isinstance(feilds, tuple):
        for feild in feilds:
            dataset = min_max_scaling_(dataset, feild)
    elif isinstance(feilds, str):
        dataset = min_max_scaling_(dataset, feilds)
    else:
        raise "Feilds is not a list/tuple/str arg!"
    
    return dataset
if __name__ == "__main__":
    df = {
        'a':[1,2,3,4]
    }

    df = pd.DataFrame(df)
    print(min_max_scaling(df, 'a'))