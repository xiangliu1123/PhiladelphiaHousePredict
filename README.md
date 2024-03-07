# Predictive Modeling of House Prices

## Introduction
This project aims to develop a predictive model for house prices using various machine learning algorithms. The process involves data preprocessing, feature engineering, model development, and evaluation to select the best-performing model. The dataset was collected from [https://www.phila.gov/property/data/](https://www.phila.gov/property/data/), containing over 500,000 data points across 35 features. We extracted 21 features including "basement", "category_code", "exterior_condition", "garage_spaces", "interior_condition", "parcel_shape", "total_area", "total_livable_area", "number_of_bathrooms", "number_of_bedrooms", "number_of_rooms", "number_stories", "general_construction", "taxable_land", "street_code", "view_type", "year_built", "zip_code", "lat", "lng", with "market_value" as the target variable.

## Data Process

### Handling Missing Values:

- Columns representing the number of bathrooms, bedrooms, rooms, stories, and general construction type were filled with zeros where values were missing. Subsequently, rows where these fields equaled zero were removed from the dataset.
- The `view_type` and `type_heater` columns were filled with "N" for entries missing these values.
- The `basements` column had specific replacements: "1", "2", "3", "4", and NaN values were replaced with "K" for unknown, and "0" was replaced with "N" for no basement.
- Missing values in `exterior_condition`, `garage_spaces`, and `interior_condition` were replaced with 3.0, 0.0, and 4.0, respectively.
- The `parcel_shape` column's missing values were filled with "N" for unknown.
- Missing values in `total_area` were filled with zeros, and rows with a total area of zero were removed.
- The `total_livable_area` also had missing values filled with zeros.
- `Year_built` missing values were replaced with the mean year of construction for the dataset.
- Missing `zip_code` values were initially filled with zero and then removed, with outlier zip codes also being excluded.

### Data Reduction:

- Properties categorized under codes 7 through 17, representing various special uses, were removed from the dataset.
- Data reduce from 500,000 to 8,200 due to vacant land and unuseable living area.

### Data Transformation:

- The longitude (`lng`) values were converted to their absolute values.

### Data Type Adjustments:

- The `zip_code` field was processed to ensure it is accurately represented as an integer.

### Saving Processed Data:

- The cleaned and processed dataset was saved to a new CSV file, `preprocess_data.csv`.
Exterior_condition:
4.0 = Average 
3.0 = Above Average
5.0 = Below Average
2.0 = Newer Construction / Rehabbed
7.0 = Sealed / Structurally Compromised
6.0 = Vacant
0.0 = Not Applicable

parcel_shape:
E = Rectangular
A = Other than a square, rectangular or triangle
B = Curves, narrow portions, long access driveways
C = Triangular
N = Unkown
D = Long and narrow


Basements：
K = Unknown
D = Full – Unknown Finish
F = Partial - Semi-Finished 
H = Partial - Unknown Finish
C = Full - Unfinished
A = Full - Finished
N = No Basement
E = Partial - Finished
J = Unknown Size - Unfinished
G = Partial - Unfinished
B = Full - Semi-Finished
I = Unknown Size - Finished 


Category_code:
1 = Single Family
2 = Multi Family
3 = Mixed Use
4 = Commercial
5 = Industrial
6 = Vacant Land

"general_construction"
A = Common brick 
B = Brick and Siding
E = Stone
C = Frame and siding
F = Stucco/Cement
G = Other/Mix
H = Brick and stucco
J = Stone/stucco
I = Stucco and siding
D = Frame and shingle

"type_heater"
A = Hot air (ducts)
B = Hot water (radiators or baseboards)
G = Radiant
N = None
C = Electric baseboard
E = Other
D = Outside heat pump

"view_type"
I = Typical/Other
A = Cityscape / Skyline
C = Park / Green Area 
D = Commercial 
N = Not Applicable
H = Industrial
E = Edifice / Landmark 
B = Flowing Water

## Feature Engineering
New features were engineered to enhance the model's predictive capability. This included creating interaction terms, transforming variables, and extracting meaningful information like area-to-room ratio or property age. Categorical variables were converted into dummy variables, and continuous variables were appropriately transformed.

## Model Development
Several machine learning algorithms were experimented with, including linear regression, decision trees, random forests, and gradient boosting. The RandomForestRegressor showed promise and was configured with 200 estimators and a random state of 42.

## Construction of Test Dataset and Model Evaluation
The model was trained on 80% of the data and tested on the remaining 20%. Performance was evaluated using MSE, RMSE, MAE, and R^2 Score, indicating a significant capture of variance in house prices but also highlighting areas for improvement.
MSE: 3648329085.2454042 
RMSE: 60401.39969607827 
MAE: 11709.269879518071 
R^2 Score: 0.9753011770869393

## Discussion
The project underscores the importance of feature engineering and model selection. The RandomForest model performed well, though overfitting and computational costs were challenges, tried to use PCA and other K-best feature for train it doesn't work too well with dataset.I think the effect of Principal Components on Prediction Performance: The results suggest a clear trend where adding more principal components generally leads to better model performance up to a certain poin.

## Recommendations
Future improvements could include hyperparameter tuning, exploration of advanced ensemble methods, and incorporation of external data sources.

## Conclusion
This project demonstrates the feasibility of using machine learning algorithms to accurately predict house prices, providing a strong foundation for further research and model optimization.
