# -*- coding: utf-8 -*-
from tools import json_tools

# 创建json
# =============================================================================
# json = {'ID_list' : ['F2286'],
#       'seasons' : ['3-4'],
#       'predict_days' : [1],
#       'times' : ['08']
#       }
# 
# json_tools.create_json(json)
# =============================================================================

# 读取json
data = json_tools.read_json()

ID_list = data['ID_list']
seasons = data['seasons']
predict_days = data['predict_days']
times = data['times']



from build_model import lstm_model,add_lstm,svr_model
# 创建lstm模型
for ID in ID_list:
    lstm_model.build_lstm(ID)

# 添加obp
for ID in ID_list:
    for season in seasons:
        for predict_day in predict_days:
            for time in times:
                add_lstm.add_obp(ID, season, predict_day, time)
                svr_model.build_svr(ID, season, predict_day, time)

