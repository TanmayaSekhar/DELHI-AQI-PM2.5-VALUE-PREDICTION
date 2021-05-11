#Importing all necessary libraries
import pandas as pd 
import statsmodels.api as sm
import gzip, pickle, pickletools 
##Load the Dataset
cleaneddata = pd.read_csv("delhi_AQIclean.csv",index_col=0)
##Create & fit the model
model=sm.tsa.statespace.SARIMAX(cleaneddata,order=(2, 1, 2),seasonal_order=(2,0,2,24)).fit()


#Dump the model in pickel file in non compressized form 
#pickle.dump(model, open('model.pkl', 'wb'))

#Dump the model in pickel file in compressized form 
filepath = "time.pkl"
with gzip.open(filepath, "wb") as f:
    pickled = pickle.dumps(model)
    optimized_pickle = pickletools.optimize(pickled)
    f.write(optimized_pickle)