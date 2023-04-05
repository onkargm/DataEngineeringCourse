import pandas as pd
import numpy as np
import locale

commerce_csv_data_path = "annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
commerce_csv_dataf = pd.read_csv(commerce_csv_data_path,encoding="unicode_escape",nrows=1000)

def converttoint(numberstring):
    try:
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
        number = locale.atoi(numberstring)
    except Exception as exc:
        number=0
    number = number *100+500
    return number


print(commerce_csv_dataf.columns)
#added extra column for calculations and operations
commerce_csv_dataf["Extra_Costs"]=commerce_csv_dataf["Value"].apply(converttoint)
print(commerce_csv_dataf.columns)
print(commerce_csv_dataf.tail(10))

#create new average column of all attributes
extra_costs_array = commerce_csv_dataf["Extra_Costs"].to_numpy()
print(extra_costs_array)
print("Mean",np.mean(extra_costs_array))
print("Minimum",np.min(extra_costs_array))
print("Maximum",np.max(extra_costs_array))

#add a random integer
commerce_csv_dataf["Industry_code"]=np.random.randint(low=10000,high=30000,size=commerce_csv_dataf.shape[0],dtype=int)
print(commerce_csv_dataf.dtypes)
print(commerce_csv_dataf)