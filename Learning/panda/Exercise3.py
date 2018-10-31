import pandas as pd
import numpy as np
import math
from scipy.stats.mstats import winsorize

flights=pd.read_csv("../data/flights.csv")
airports=pd.read_csv("../data/airports.csv")
flights.fillna(0,inplace=True)
airports.fillna(0,inplace=True)


def mergeColumns(df,colName1,colName2,newColName):
    df[newColName]=df.colName1 + '-' + df.colName2
    return df[newColName]

# Write a function that, for all the quantitative cols, returns mean, quartiles, stdev, max, kurtosis
def quantStat():
    flights_num=flights.select_dtypes(include=['int64'])
    flights_num.aggregate(['mean','quantile','std','max','kurt'])
    # print(flights_num.head())

#replace the NaN with mean values in the column 'AIR_SYSTEM_DELAY'
def replaceNanSeriesWithMean(df,colName):
    df[colName]=df[colName].fillna(df[colName].mean())
    return df[colName]

# Remove outliers for 'departure_delay' - remove rows in excess of 3 standard deviations from mean
def seriesRemoveOutlier(objDS,sName):
    # objDS.fillna(0,include=True)
    XminusMean = objDS[sName] - objDS[sName].mean()
    sd = 3 * objDS[sName].std()
    outlier = objDS[np.abs(XminusMean) <= sd]
    return outlier


# Remove those rows where (for quantitative variables) any quant variable has value > 3std from mean
def dataframeRemoveOutlier(df):
    ds=df._get_numeric_data()
    for colName in ds.columns:
        ds=seriesRemoveOutlier(ds, colName)

def class1():
    ds=flights.groupby(['AIRLINE'])
    print(ds.DEPARTURE_DELAY.mean())



def dataFrameWinsorize(df):
    df=df._get_numeric_data()
    # print(df.shape)
    print(df.columns)
    for colName in df.columns:
        ser = winsorize(df[colName], limits=[0.05, 0.05])
    # print(df.shape)

# log transform the column 'departure_delay' into a new column 'Log_dep_delay'
def logTransform(df,colName):
    df[colName] = np.log(df[colName])
    return df[colName]

# create a new dataframe where all the quantitative columns are log-transformed
def dataframeLogTransform(df):
    ds=df._get_numeric_data()
    ds = np.log(ds)
    return ds

#Normalise all the quantitative columns with standard normalisation
def normalize(dataset):
    dataset=dataset._get_numeric_data()
    dataNorm=((dataset-dataset.min())/(dataset.max()-dataset.min()))*20
    dataNorm["diagnosis"]=dataset["diagnosis"]
    return dataNorm

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def sigmoidSeries(ds,series):
    ds[series]=ds[series].apply(sigmoid)

def leftJoin(ds1,ds2,colName):
    result=pd.merge(ds1,ds2,on=colName,how='left')
    return result

def geoHash():
    df = flights.merge(airports, how='left', left_on='ORIGIN_AIRPORT', right_on='IATA_CODE')
    fd = df[['AIRLINE', 'LONGITUDE', 'LATITUDE']].groupby('AIRLINE').mean()

def number_of_flights_for_each_route():
    flights['ROUTE'] = flights.ORIGIN_AIRPORT + ' - ' + flights.DESTINATION_AIRPORT
    df = flights[['ROUTE', 'YEAR']].groupby('ROUTE').count()

def flights_before_12():
    ds = flights.loc[flights.DEPARTURE_TIME < 1200, :]
    ds1 = ds[['AIRLINE', 'YEAR']].groupby('AIRLINE').count()


# For each airline, the percentage delay for each dep_airport, over total delay across all dep_airport

# The mean geohash of "longitude" and "latitude" for each airline

# The percentage of flights leaving before 12pm, over total flights for each airline

# for each airline, the percentage of flights in each route over all the routes

# Do PCA to reduce the variables 'departure_delay' and 'arrival_delay' to a single component

# mergeColumns(df,'ORIGIN_AIRPORT','DESTINATION_AIRPORT','ROUTE')
# quantStat()
# replaceNanSeriesWithMean(flights,'AIR_SYSTEM_DELAY')
# seriesRemoveOutlier(flights,'DEPARTURE_DELAY')
# dataframeRemoveOutlier(flights)
# dataFrameWinsorize(flights)
# logTransform(flights,"DEPARTURE_DELAY")
# normalize(flights)
# sigmoidSeries(flights,'ARRIVAL_DELAY')
# airports.rename(columns={'IATA_CODE':'ORIGIN_AIRPORT'},inplace=True)
# leftJoin(flights,airports,'ORIGIN_AIRPORT')
# dataframeLogTransform(flights)
# geoHash()
# number_of_flights_for_each_route()
# flights_before_12()