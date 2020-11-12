import pandas as pd
import numpy as np


def load_and_proccess(rawData):
    rawData.columns = ['Age','Workclass','fnlwgt','Education','Education-Num','Marital-Status','Occupation','Realtionship','Race','Sex','Capital-Gain','Capital-Loss','Hours-Per-Week','Native-Country','Income']
    df1 = (rawData.drop(columns = ['fnlwgt','Education-Num',]))
    
    return df1
    