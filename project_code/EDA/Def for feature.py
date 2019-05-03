# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:27:22 2019

@author: HS PARK
"""

##%% (1) initial setting
# import library
import os
import math
import pandas as pd
import numpy as np

# change directory
os.getcwd() 
os.chdir('C:/Users/HS/Documents/GitHub/BOAZ_adv_project/project_code/EDA')


##%% (2) read dataset
# read dataset
path_data = 'C:/Users/HS/Documents/GitHub/Recommendation system/data'
train = pd.read_csv(path_data + '/train_v3.csv')
test = pd.read_csv(path_data + '/test_v3.csv')
#item_metadata = pd.read_csv(path_data + '/item_metadata_v2.csv')
#df_item_list =  pd.read_csv(path_data + '/df_item_list_v2.csv')

##%% Def

# 선 전처리 필요

def get_new_train(df):
    
    strange_index = [3593077, 12178010, 15149208, 15199625]
    unknown_index = list(df.loc[df['action_type'] == 'interaction item info'].loc[df['reference'] == 'unknown'].index)
    
    for i in strange_index:
        df.iloc[i, 4] = 'search for poi'
        # print(df.ix[i, 4])
    for i in unknown_index:
        df.iloc[i, 5] = '9'
    
    return df


def get_new_test(df):
    
    unknown_index = list(df.loc[df['action_type'] == 'interaction item info'].loc[df['reference'] == 'unknown'].index)
    
    for i in unknown_index:
        df.iloc[i, 5] = '9'
    
    return df



# def string_to array
def string_to_array(s):
    """Convert pipe separated string to array."""

    if isinstance(s, str):
        out = s.split("|")
    elif math.isnan(s):
        out = []
    else:
        raise ValueError("Value must be either string of nan")
    return out


def explode(df_in, col_expl : str):
    """Explode column col_expl of array type into multiple rows."""

    df = df_in.copy()
    df.loc[:, col_expl] = df[col_expl].apply(string_to_array)

    df_out = pd.DataFrame(
        {col: np.repeat(df[col].values,
                        df[col_expl].str.len())
         for col in df.columns.drop(col_expl)}
    )

    df_out.loc[:, col_expl] = np.concatenate(df[col_expl].values)
    df_out.loc[:, col_expl] = df_out[col_expl].apply(int)

    return df_out


### 함수들
# get_domain 
def get_domain(df, col : str):
    """ columns 별로 unique 한 범주를 찾아 데이터프레임으로 만든다"""
    
    mask = df.groupby(col).sum().index
    df_out = pd.DataFrame(data = mask, columns = [col])
    
    return df_out


# get_location
def get_location(df):
    ''' df_location 한정. "," 로 split 한 컬럼을 데이터프레임으로 만든다'''
    
    location_list = df.city.str.split(',')
    location_dic={}

    contries = []
    cities = []

    location_dic = {'country' : contries ,
                    'city' : cities} 

    for i in location_list:
        if i[0] not in cities:
            cities.append(i[0])
            contries.append(i[1])

    df_out = pd.DataFrame(location_dic).sort_values(by = ['country'], axis= 0).reset_index(drop=True)
    
    return df_out


# get_popularity
def get_popularity(df, action : str):
    """데이터프레임 안에서 아이템별로 action type의 횟수를 구한다"""

    mask = df["action_type"] == action  # 구하는 action_type
    name = str(action.replace(' ', '_'))
    df_clicks = df[mask]  
    df_item_clicks = (
        df_clicks
        .groupby("reference")
        .size()
        .reset_index(name="n_{0}".format(name))
        .transform(lambda x: x.astype(int))  # ?
    )

    return df_item_clicks


#def merge_popularity(df)
def merge_popularity(df):
    '''데이터프레임에서 아이템별로 구했던 action type 횟수를 merge 한다'''
    
    action_list = [         
            # action_type 의 reference 가 item_id 인 행동만 뽑는다.
            'interaction item info', 
            'interaction item image', 'interaction item rating',
            'interaction item deals', 'search for item',
            'clickout item'
            ]

    df_item_actions = pd.DataFrame(columns = ['reference'])
    
    for action in action_list:
        df_item_actions = pd.merge(df_item_actions, get_popularity(df, '{0}'.format(action)), 
                             on = 'reference', how = 'outer')
        
    df_item_actions = df_item_actions.rename(columns = {'reference': 'item_id'})

    return df_item_actions


########################

def get_impression_price(df):

    target_item = df.loc[df["action_type"] == "clickout item"][['impressions']].rename(columns = {'impressions' : 'item_id'})
    target_price = df.loc[df["action_type"] == "clickout item"][['prices']].rename(columns = {'prices' : 'price'})
    
    target_item = explode(target_item, 'item_id')
    target_price = explode(target_price, 'price')
    
    df_out = pd.concat([target_item, target_price], axis = 1)
    
    return df_out


df_item_price = get_impression_price(train)


#def get_dic_item_price(df):

def get_dic_item_forList(df, col_name : str, index_name = 'item_id' ):

    sample_ = df.item_id.value_counts()
    sample_.name = col_name
    sample_.index.name = index_name

    dic_item = dict()

    for i in sample_.index:
        dic_item[i] = list()
    
    for i in df.index:
        x = df.iloc[i, 0]
        y = df.iloc[i, 1]

        dic_item[x].append(int(y))
        
    return dic_item


def get_dic_item_forSet(df):#, col_name : str, index_name = 'item_id' ):

    sample_ = df.item_id.value_counts()
    #sample_.name = col_name
    #sample_.index.name = index_name

    dic_item = dict()

    for i in sample_.index:
        dic_item[i] = set()
    
    for i in df.index:
        x = df.iloc[i, 0]
        y = df.iloc[i, 1]

        dic_item[x].add(y)
        
    return dic_item


dic_item = get_dic_item_forList(df_item_price)

##########################

def get_aggPrice(dic_item : dict):

    dic_agg_price = dict()
    
    item_id_list = list()
    mean_price_list = list()
    min_price_list = list()
    max_price_list = list()
    var_price_list = list()
    std_price_list = list()
    n_impressions_list = list()
    
    for i in dic_item:
        
        # 계산하기
        prices = np.array(dic_item.get(i))
        mean_price = float(np.mean(prices))
        n_impressions = len(prices)
        
        try:
            min_price = np.min(prices)
            max_price = np.max(prices)
            var_price = np.var(prices)
            std_price = np.std(prices)
            
        except ValueError:
            min_price = np.nan
            max_price = np.nan
            var_price = np.nan
            std_price = np.nan
            pass
    
        
        # list에 담기
        item_id_list.append(i)
        mean_price_list.append(mean_price)
        min_price_list.append(min_price)
        max_price_list.append(max_price)
        var_price_list.append(var_price)
        std_price_list.append(std_price)
        n_impressions_list.append(n_impressions)
        
    
    # 딕셔너리 만들기
    dic_agg_price['item_id'] = item_id_list
    dic_agg_price['mean_price'] = mean_price_list
    dic_agg_price['min_price'] = min_price_list
    dic_agg_price['max_price'] = max_price_list
    dic_agg_price['var_price'] = var_price_list
    dic_agg_price['std_price'] = std_price_list
    dic_agg_price['n_impressions'] = n_impressions_list
    
    # 데이터프레임
    df_item_aggPrice = pd.DataFrame(dic_agg_price)

    return df_item_aggPrice


#######################


####
####
# filter score 구하는 함수



# item rating, star 구하는 함수
# poi one hot encoding    

########
    
df_item_action = merge_popularity(test)
df_item_action


#######################
### 실행문
df_location = get_domain(train, 'city')
df_platform = get_domain(train, 'platform')

df_location = get_location(train)
df_location


df_item_action = merge_popularity(train)
df_item_action

df_item_ = get_domain(df_item_action, 'item_id')
df_item_

df_itme_aggPrice = get_aggPrice(dic_item)

df_itme_aggPrice.shape
df_itme_aggPrice.columns
df_itme_aggPrice.head()
df_itme_aggPrice.tail()

df_item_action.columns
df_item_v1 = pd.merge(df_itme_aggPrice, df_item_action, on = 'item_id', how = 'outer')
print(df_item_v1.shape)
#print(df_item_v1.dtypes)
print(df_item_v1.columns)
print(df_item_v1.head())
print(df_item_v1.tail())



df_item_all = pd.merge(item_metadata, df_item_v1,  on = 'item_id', how = 'outer')

print(df_item_all.columns)
print('df_item_all:', df_item_all.shape)
print('item_metadata:', item_metadata.shape)
df_item_all.shape[0] - item_metadata.shape[0]
###


df1 = train.loc[train['action_type'] == 'search for poi'][['city', 'reference']]

df1.columns = ['item_id', 'poi']
df1.columns
df1.shape
df1.head()

get_dic_item_forSet(df1)

df1.item_id.value_counts() #4258


sample_ = df1.item_id.value_counts()

dic_item = dict()

for i in sample_.index:
    dic_item[i] = set()


for i in df1.index:
    x = df1.iloc[i, 0]
    y = df1.iloc[i, 1]

    dic_item[x].add(y)
    
train.groupby(['reference', 'city']).size()

### csv 로 저장문 

path_data_out = 'C:/Users/HS/Documents/GitHub/Recommendation system/data'

DataList = [df_item_v1]
DataList_Name = ['df_item_v1']
for i, j in zip(DataList, DataList_Name):
    i.to_csv('{0}/{1}.csv'.format(path_data_out, str(j)), index = False)



df_item_v1.to_csv(path_data_out + '/df_item_v1.csv', index = False)
df_item_all.to_csv(path_data_out + '/df_item_v2.csv', index = False) 
df_location.to_csv(path_data_out + '/df_location.csv', index = False) 