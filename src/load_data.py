import pandas as pd

def load_data():
    ijcai_18_train = pd.read_csv("data/round1_ijcai_18_train_20180301.txt", sep=' ')
    ijcai_18_test = pd.read_csv("data/round1_ijcai_18_test_a_20180301.txt", sep=' ')
    return ijcai_18_train, ijcai_18_test