import util
import numpy as np
import pandas as pd
from load_data import *
ijcai_18_train, ijcai_18_test = load_data()

ijcai_18_test['is_trade'] = -1 # test label 标注为-1，用以区分训练集和数据集
ijcai_18_merged = pd.concat([ijcai_18_train, ijcai_18_test], axis=0)

ijcai_18_merged = ijcai_18_merged.set_index("instance_id")

remodified_rows = (
    ('item_id', np.object),
    ('item_brand_id', np.object),
    ('item_city_id', np.object),
    ('user_id', np.object),
    ('user_gender_id', np.object),
    ('user_occupation_id', np.object),
    ('context_id', np.object),
    ('context_page_id', np.object),
    ('shop_id', np.object),
    ('is_trade', np.object),
)
for row, retype in remodified_rows:
    ijcai_18_merged[row] = ijcai_18_merged[row].astype(retype)

ijcai_18_test = ijcai_18_merged[ijcai_18_merged.is_trade == -1]
ijcai_18_train = ijcai_18_merged[ijcai_18_merged.is_trade != -1]

reindex = (
    "item_id",
    "item_brand_id",
    "item_city_id",
    "context_page_id",
    "shop_id", 
    "user_id",
    "context_id",
)

scaling = [
    "user_age_level",
    "user_star_level",
    "item_price_level",
    "item_sales_level",
    "item_collected_level",
    "item_pv_level",
    "shop_star_level",
    "shop_review_num_level",
    "context_page_id",
]

one_hot = [
    "user_gender_id",
    "user_occupation_id",
    "item_city_id"
]

ijcai_18_merged = util.reindex(ijcai_18_merged, reindex)
ijcai_18_merged = util.min_max_scaling(ijcai_18_merged, scaling)
ijcai_18_merged = util.one_hot(ijcai_18_merged, one_hot)

def get_dataset():
    return ijcai_18_merged