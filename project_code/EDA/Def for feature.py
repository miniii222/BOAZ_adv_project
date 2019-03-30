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
train = pd.read_csv(path_data + '/train.csv')
#test = pd.read_csv(path_data + '/test.csv')
item_metadata = pd.read_csv(path_data + '/item_metadata.csv')
df_item_list =  pd.read_csv(path_data + '/df_item_list.csv')

##%% Def
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


def explode(df_in, col_expl):
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
            #'interaction item info', 
            'interaction item image', #'interaction item rating',
            'interaction item deals', 'search for item',
            'clickout item'
            ]

    df_item_actions = pd.DataFrame(columns = ['reference'])
    
    for action in action_list:
        df_item_actions = pd.merge(df_item_actions, get_popularity(df, '{0}'.format(action)), 
                             on = 'reference', how = 'outer')
        
    df_item_actions = df_item_actions.rename(columns = {'reference': 'item_id'})

    return df_item_actions





####


# item list 구하기
df_target = train.loc[train["action_type"] == "clickout item"][['impressions']]
df_ex = explode(df_target, 'impressions')
df_ex

df_item_list = get_domain(df_ex, 'impressions').rename(columns = {'impressions' : 'item_id'})
#df_item_list.to_csv('{0}/data/df_item_list.csv'.format(path_data_out), index = False)




# item price 구하는 함수
df_item_list =  pd.read_csv(path_data + '/df_item_list.csv')
df_item_list.head()



clickout_only = train.loc[train['action_type'] == 'clickout item']
clickout_only = clickout_only.loc[:, ['impressions', 'prices']]
clickout_only.head()


impressions_split = clickout_only.impressions.str.split('|')
prices_split = clickout_only.prices.str.split('|')



# item_metadata 에 있는 호텔 리스트의 가격정보 담기
hotel_contain_dic = {}

for i in df_item_list.index:
    
    hotel_contain_dic[df_item_list.loc[i]['item_id']] = []



# 구매정보가 있지만 item_metadata에 없는 호텔리스트
hotel_not_contain_list = []

# metadataset 안에 있는 것과 매핑
for i in range(0, len(impressions_split)):
    
    for x, y in zip(impressions_split.iloc[i], prices_split.iloc[i]):
        
        try:
            hotel_contain_dic[int(x)].append(int(y))
            break
            
        except KeyError:
            print('{0} is not in our keys'.format(x))
            hotel_not_contain_list.append(int(x))


hotel_contain_dic.items()

# 6326, 6312 ?? 


for x, y in hotel_contain_dic.items():
    print(x, y)


# price 계산











#set 으로 확인
            
            
####

# item rating, star 구하는 함수
# filter score 구하는 함수
# poi one hot encoding    



### 실행문
df_location = get_domain(train, 'city')
df_platform = get_domain(train, 'platform')

df_location = get_location(df_location)

df_item_action = merge_popularity(train)
df_item_action

df_item_ = get_domain(df_item_action, 'item_id')
df_item_








### csv 로 저장문 

path_data_out = 'C:/Users/HS/Documents/GitHub/Recommendation system'

DataList = [df_location, df_platform]
DataList_Name = ['df_location', 'df_platform']
for i, j in zip(DataList, DataList_Name):
    i.to_csv('{0}/{1}.csv'.format(path_data_out, str(j)), index = False)





