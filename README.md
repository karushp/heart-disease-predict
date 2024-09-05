# Heart Disease Analysis and Prediction Model

## Project Summary

This project focuses on predicting heart disease using a dataset of 303 patient records. The goal was to enhance predictive accuracy through a series of steps including scaling, normalization, and hyperparameter tuning. The data was divided into training and testing sets, and an extensive grid search was performed to identify the optimal settings for the K-Nearest Neighbors (KNN) model. The resulting model achieved a cross-validation score of 0.8684 and a test set score of 0.8197.

Additionally, the analysis revealed that the 'thal' (Thalassemia) feature was notably influential in the model's predictions. Despite these achievements, the project faced limitations such as a small dataset, lack of consideration for temporal factors, and absence of external validation.

Data Source : [Kaggle](https://www.kaggle.com/datasets/krishujeniya/heart-diseae)

## Dataset Overview
The dataset contains 303 records and the following features:

- **age**: Age of the patient (in years)
- **sex**: Sex of the patient (1 = male, 0 = female)
- **cp**: Chest pain type (1-4)
- **trestbps**: Resting blood pressure (in mm Hg on admission to the hospital)
- **chol**: Serum cholesterol in mg/dl
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1 = yes; 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment
- **ca**: Number of major vessels (0-3) colored by fluoroscopy
- **thal**: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)
- **target**: Presence of heart disease (1 = yes, 0 = no)

Total Records: **303**

## Workflow

### 1. Preprocessing
- **Missing Values**:
  - No missing values in the dataset.

- **Checking Data Types**:
  - All data types are either integers or floats; no further processing required.

  ```plaintext
  RangeIndex: 303 entries, 0 to 302
  Data columns (total 14 columns):
  #   Column    Non-Null Count  Dtype
  ---  ------    --------------  -----
  0   age       303 non-null    int64
  1   sex       303 non-null    int64
  2   cp        303 non-null    int64
  3   trestbps  303 non-null    int64
  4   chol      303 non-null    int64
  5   fbs       303 non-null    int64
  6   restecg   303 non-null    int64
  7   thalach   303 non-null    int64
  8   exang     303 non-null    int64
  9   oldpeak   303 non-null    float64
  10  slope     303 non-null    int64
  11  ca        303 non-null    int64
  12  thal      303 non-null    int64
  13  target    303 non-null    int64
  dtypes: float64(1), int64(13)


### 2. Data Visualisation
  ![alt text](/images/cat_features.png)
  ![alt text](images/num_features.png)

### 3. Outliers
  - Identified Outliers in numerical features
  - Determined to keep the outlier

     ```plaintext
    Outliers in 'age':
        age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
    72   29   1   1        130    204  0        0        202    0        0.0    2    0    2     1
    129  74   0   1        120    269  0        0        121    1        0.2    2    1    2     1
    144  76   0   2        140    197  0        2        116    0        1.1    1    0    2     1
    238  77   1   0        125    304  0        0        162    1        0.0    2    3    2     0

    Outliers in 'trestbps':
        age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
    71   51   1   2        94     227  0        1        154    1        0.0    2    1    3     1
    124  39   0   2        94     199  0        1        179    0        0.0    2    0    2     1
    223  56   0   0        200    288  1        0        133    1        4.0    0    2    3     0
    248  54   1   1        192    283  0        0        195    0        0.0    2    1    3     0

### 4. Correlation Analysis
  - **Features and Target Correlation**
   ![alt text](images/features_correlation.png)

### 5. Target Distribution
- **Balanced Target Distribution**
  ![alt text](images/target_distribution.png)

### 6. Model Building
- **Scaling, Normalizing, Train-Test Split and Grid Search**
-  ```plaintext
    Best Parameters: {'classifier': KNeighborsClassifier(), 'classifier__n_neighbors': 5, 'preprocessor__num': Pipeline(steps=[('scaler', MinMaxScaler())])}
    Best Cross-Validation Score: 0.8683673469387756
    Test Set Score: 0.819672131147541

  **Feature Importance**
   ```plaintext
    thal: 0.080 ± 0.031
```
### 7. Final Pipeline
![alt text](images/final_pipeline.png)

## Limitations
- **Small Dataset:** The dataset includes only 303 data points, which may not be sufficient to capture the full variability needed for a robust predictive model.

- **Limited Feature Set:** The dataset includes a limited number of features, which may not capture all relevant factors affecting heart disease. Important variables like lifestyle, diet, or genetic factors are not included, which could limit the model’s predictive power

- **No Consideration of Temporal Factors:** The model does not account for temporal data, such as patient history or the progression of symptoms over time, which are crucial for a comprehensive understanding of heart disease.

- **Lack of External Validation:** The model's performance has been validated using cross-validation within the same dataset, but it has not been tested on an external dataset, limiting its ability to generalize to new, unseen data.

## Conclusion
This project was focused on enhancing predictive accuracy by implementing scaling and normalization techniques. The data was divided into training and testing sets and an extensive grid search was conducted to optimize the model's hyperparameters. This process resulted in a finely-tuned K-Nearest Neighbors (KNN) model, which achieved a notable cross-validation score of 0.8684 and a test set score of 0.8197.

Feature importance revealed that the 'thal' (Thalassemia) feature significantly influenced the model's predictions, with an importance score of 0.080 ± 0.031.

This comprehensive approach to model development ensured that the final model was precise and interpretable, offering valuable insights into heart disease prediction.
