import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# Data set load
df_heart = pd.read_csv('heart-disease.csv')


# Creating new interactive features based on existing features
df_heart['thalach_age_ratio']= df_heart['thalach']/df_heart['age']
df_heart['trestbps_age_ratio']= df_heart['trestbps']/df_heart['age']
df_heart['chol_age_ratio']= df_heart['chol']/df_heart['age']

# Feature and target
X = df_heart.drop(columns='target')
y = df_heart['target']

# Split datat into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1)


# Defining Categorical and Numerical columns
categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'thalach_age_ratio', 'trestbps_age_ratio', 'chol_age_ratio']

# Define the transformer for categorical features
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Define the transformer for numerical features
numerical_transformer = Pipeline(steps=[
    ('scaler', MinMaxScaler())
])

# Combine transformers into a preprocessor using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Define the final pipeline with the best classifier and preprocessor
final_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', KNeighborsClassifier(n_neighbors=5))
])

# Fitting the pipeline
final_pipeline.fit(X_train, y_train)
