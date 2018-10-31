import pandas as pd
import numpy as np
from sklearn import preprocessing


ds=pd.read_csv("D:\\Automation\\QEDGE\\PythonLearningLBG\\mip-python\\mip-python\\mip-python\\data\\flights.csv",nrows=100)
ds.drop("DAY_OF_WEEK",axis=1,inplace=True)
ds=ds.rename(columns={"WHEELS_OFF":"HAS_WHEELS"})
col=ds.columns
ds=np.array_split(ds,4)
ds=np.concatenate(ds)
ds=pd.DataFrame(ds,columns=col)
# ds=ds[ds['AIRLINE']=='AA']
#ds=ds[(ds['DESTINATION_AIRPORT']=='PBI') & (ds.ARRIVAL_DELAY < 10)]

#fill the blanks in the AIR_SYSTEM_DELAY column with the average of the column itself
# ds['AIR_SYSTEM_DELAY']=(ds['AIR_SYSTEM_DELAY'].fillna(ds['AIR_SYSTEM_DELAY'].mean()))

#Create a column "has_A", which contains 1 if the airline name contains the letter 'A', 0 otherwise
# ds["has_A"]=ds.AIRLINE.str.contains("A",1,0).astype(int)

#get a random sample of the rows in the dataframe
# ds=ds.sample(n=5,axis=0)
# print(ds)

#normalise the column "DEPARTURE_DELAY" to the range 0-1 with MinMax normalisation
# ds['DEPARTURE_DELAY']=(ds.DEPARTURE_DELAY-ds.DEPARTURE_DELAY.min())/(ds.DEPARTURE_DELAY.max()-ds.DEPARTURE_DELAY.min())
# print(ds['DEPARTURE_DELAY'])

#binarise the column "ORIGIN_AIRPORT"
# ds['ORIGIN_AIRPORT']=ds['ORIGIN_AIRPORT'].str.encode('utf-8')
# print(ds['ORIGIN_AIRPORT'].values)