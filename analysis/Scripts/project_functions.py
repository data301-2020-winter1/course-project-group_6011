import pandas as pd
import numpy as np


def load_and_proccess(rawData):
    rawData.columns = ['Age','Workclass','fnlwgt','Education','Education-Num','Marital-Status','Occupation','Realtionship','Race','Sex','Capital-Gain','Capital-Loss','Hours-Per-Week','Native-Country','Income']
    return rawData

def describedf(data):
    return data.describe()

def nuniquedf(data):
    return data.nunique(axis=0)

def columnsdf(data):
    return data.columns

def shapedf(data):
    return data.shape