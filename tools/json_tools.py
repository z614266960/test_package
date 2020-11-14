# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:26:45 2020

@author: 61426
"""
import json

def create_json(data,path='config/record.json'):
    '''
    Parameters
    ----------
    data : ang
        想要创建json的数据.
    path : string, optional
        创建路径. The default is 'config/record.json'.
    Returns
    -------
    None.
    '''
    with open(path,"w") as f:
        json.dump(data,f)
        print("加载入文件完成...")  
    
def read_json(path='config/record.json'):
    '''
    Parameters
    ----------
    path : string, optional
        读取路径路径. The default is 'config/record.json'.
    Returns
    -------
    dict:加载的结果.
    '''
    with open(path,'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict
