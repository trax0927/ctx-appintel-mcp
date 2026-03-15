import pandas as pd
from sklearn.metrics import r2_score

df = pd.read_csv('validation_data.csv')
df['Your_Model_Predicted'] = df['Predicted_Downloads']  

correlation = r2_score(df['Sensor_Tower_Reported_Downloads'], df['Your_Model_Predicted']) * 100
print(f"Correlation with Sensor Tower: {correlation:.1f}%")
print("First 5 rows:")
print(df[['App', 'Your_Model_Predicted', 'Sensor_Tower_Reported_Downloads']].head())
