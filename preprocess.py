import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'data\opa_properties_public.csv'
df = pd.read_csv(file_path)
data = df[["type_heater","number_of_bathrooms","number_of_bedrooms","number_of_rooms","number_stories", "general_construction","taxable_land","street_code","view_type","basements", "category_code", "street_code","taxable_land","exterior_condition", "garage_spaces", "interior_condition", "parcel_shape", "total_area","total_livable_area", "year_built", "zip_code", "lat", "lng","market_value"]]

# print(f"Total Data: {data.shape[0]}")


data.loc[:,"number_of_bathrooms"] = data.loc[:,"number_of_bathrooms"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.number_of_bathrooms == (0)].index) #and drop it


data.loc[:,"number_of_bedrooms"] = data.loc[:,"number_of_bedrooms"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.number_of_bedrooms == (0)].index)

data.loc[:,"number_of_rooms"] = data.loc[:,"number_of_rooms"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.number_of_rooms == (0)].index)


data.loc[:,"number_stories"] = data.loc[:,"number_stories"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.number_stories == (0)].index)

data.loc[:,"general_construction"] = data.loc[:,"general_construction"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.general_construction == (0)].index)



data.loc[:,"view_type"] = data.loc[:,"view_type"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.view_type == (0)].index)

data.loc[:, "type_heater"] = data.loc[:,"type_heater"].fillna("N") #replace NAN of type_heater with N for unknown



for i in range (7,17):
    #remove other sprcial use of the property other than SINGLE FAMILY, INDUSTRIAL, COMMERCIAL, MULTI FAMILY, MIXED USE, VACANT LAND
    data=data.drop(data[data.category_code == (i)].index)

# print(data.category_code.value_counts(dropna=False))

data.loc[:, "basements"] = data["basements"].replace("1","K") # replace 1,2,3,4 and NAN with "K" as unknown
data.loc[:, "basements"] = data["basements"].replace("2","K")
data.loc[:, "basements"] = data["basements"].replace("3","K")
data.loc[:, "basements"] = data["basements"].replace("4","K")
data.loc[:, "basements"] = data["basements"].replace("0","N") # replace 0 with "N" means no basements
data.loc[:, "basements"] = data.loc[:,"basements"].fillna("K")
# print(data.basements.value_counts(dropna=False))
    

data.loc[:, "exterior_condition"] = data.loc[:, "exterior_condition"].fillna(3.0) #replace the property with the 3.0 for average of all the property

data.loc[:, "garage_spaces"] = data.loc[:, "garage_spaces"].fillna(0.0) #replace the property with Nan with 0 perhaps theu have no garage space

data.loc[:, "interior_condition" ] = data.loc[:, "interior_condition"].fillna(4.0) #replace the property with Nan with 4.0 for average for all NAN property

data.loc[:, "parcel_shape"] = data.loc[:, "parcel_shape"].fillna("N") #replace NAN parcel shape with "N" as unknown



data.loc[:,"total_area"] = data.loc[:,"total_area"].fillna(0) #replace Nan row with 0
data=data.drop(data[data.total_area == (0)].index) #and drop the row that total area with 0 becasue it don't make sense


data.loc[:,"total_livable_area"] = data.loc[:,"total_livable_area"].fillna(0) #fill NAN with 0 which means that the land is vacant or none liviable space


data.loc[:,"year_built"] = data.loc[:,"year_built"].fillna(int(data.year_built.mean())) #replace NAN with the mean of the column for the year of built


data.loc[:,"zip_code"] = data["zip_code"].fillna(0) #replace NAN zip code with zero and drop it
data=data.drop(data[data.zip_code == (0)].index)
data["zip_code"] = data["zip_code"].astype(str) #parse such as 19115.0 to 19115 as int64 type
data["zip_code"] = data["zip_code"].str.split(".",expand=True)[0]
data["zip_code"] = data["zip_code"].astype("int64")
data=data.drop(data[data.zip_code == (88888)].index) #drop outliner

data.loc[:,"lng"] = data["lng"].abs() #covert the longtitude to absolute value to avoid the ordinary negative numbers


data.to_csv('Data\preprocess_data.csv', index=False)