from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd


data = pd.read_csv('data/preprocess_data.csv')

data_encoded = pd.get_dummies(data, columns=['type_heater', 'general_construction', 'view_type', 'basements', 'parcel_shape'])

# Prepare the features and target variable
X = data_encoded.drop('market_value', axis=1)
y = data_encoded['market_value']
#hh
# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Regressor
random_forest = RandomForestRegressor(n_estimators=200, random_state=42)
random_forest.fit(X_train, y_train)

# Predict on the testing set
y_pred_rf = random_forest.predict(X_test)

# Calculate and display evaluation metrics for Random Forest
mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("MSE:", mse_rf, "RMSE:", rmse_rf, "MAE:", mae_rf, "R^2 Score:", r2_rf)
