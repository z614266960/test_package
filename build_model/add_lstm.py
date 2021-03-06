# -*- coding: utf-8 -*-
"""
@author: 61426
"""
# F6054，F6060 站点数据不足

import pandas as pd
import numpy as np
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import  os
from tensorflow.keras.models import Sequential, load_model
from tools import file_tools

def add_obp(ID,season,predict_day,time,data_path='data/last_15_days/',
            obp_path = 'data/obp/',models_save_path = 'models/lstm/'):
    """
    通过lstm模型，添加lstm的预测值obp
    ----------
    ID : string
        要建模的站点
    season : string
        要建模的季节（3-4）
    predict_day : int
        要预测的天数
    time : string
        要预测的小树(08)
    data_path : string
        路径，过去15天的ob,ec数据
    obp_path : string
        obp的保存路径
    look_after : int
        预测未来多少个数据
    models_save_path : string
        路径，lstm模型存放地点
    ----------
    """
    print('*'*10)
    print(ID,season,predict_day,'start')
    
    FILES_PATH = data_path+str(predict_day)+'天/'+season+'/'+time+'/'+ID+'.csv'
    SAVE_PATH = obp_path+str(predict_day)+'天/'+season+'/'+time+'/'
    MODEL_SAVE_PATH = models_save_path+ID+'_1.h5'
    
    origin_data = pd.read_csv(FILES_PATH)
    origin_data['ob_p'] = ''
    
    # 获取数据
    data = origin_data
    cols = []
    for i in range(-15,-(predict_day-1),1):
        column = 'ob_'+str(i)
        cols.append(column)
    for i in range(-(predict_day-1),0,1):
        column = '10UV_'+str(i)
        cols.append(column)
    
    data = np.array(data[cols])
    
    
    #归一化
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)
    
    X = data.reshape(data.shape[0],data.shape[1],1)
    Y = np.array(origin_data['ob'])
    
    # 加载模型并预测
    model = load_model(MODEL_SAVE_PATH)
    Predicts = model.predict(X)
    
    from sklearn.metrics import mean_absolute_error
    my_mae = mean_absolute_error(Predicts,Y)
    print('my_mae:'+str(my_mae))
    
    # 保存obp结果
    origin_data['ob_p'] = Predicts
    cols = ['predict_time','MSL','ob','10UV','ob_p']
    file_tools.check_dir_and_mkdir(SAVE_PATH)
    origin_data[cols].to_csv(SAVE_PATH+ID+'_p.csv',index=False)





