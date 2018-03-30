import matplotlib.pyplot as plt
import pandas as pd

def plt_by_col(dataset, col, label, signs):
    if not isinstance(dataset, pd.DataFrame):
        raise "The type of dataset is not DataFrame!"
    
    if isinstance(signs, list) or isinstance(signs, tuple):
        pass
    else:
        signs = [signs, ]

    cnt = dataset[col].value_counts()
    for val in signs:
        df = dataset[dataset[label] == val][col].value_counts() / cnt
        plt.plot(df.values)
    plt.show()