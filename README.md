# Click Through Rate Analysis and Prediction

This repository contains a Jupyter notebook for analyzing and predicting user Click-Through Rates (CTR) using various machine learning techniques. The data is based on ad interaction metrics, and the goal is to uncover patterns that lead to ad clicks and build a predictive model.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Modeling](#modeling)
- [Results](#results)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Project Overview

This project aims to identify key factors influencing whether users click on ads and predict future user behavior based on the available data. It uses a dataset with information like user age, income, daily time spent on the site, and internet usage. The analysis includes data cleaning, feature engineering, visualization, and model building.

## Dataset

The dataset contains 10,000 records with the following columns:
- **Timestamp**: Date and time of the user's interaction.
- **Daily Time Spent on Site**: Minutes spent on the site daily.
- **Age**: User's age.
- **Area Income**: Average income of the user's geographic area.
- **Daily Internet Usage**: Minutes of daily internet usage.
- **Clicked on Ad**: Target variable indicating whether the user clicked on the ad (1) or not (0).

### Data Loading
The data is loaded from a CSV file stored in Google Drive. The `Timestamp` column is parsed into datetime format to extract features like the hour, day of the week, and month.

## Requirements

- Python 3.x
- Google Colab or Jupyter Notebook
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - xgboost
  - scipy
  

Install the dependencies using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost scipy
```

## Project Structure

```
.
click_through_rate_project/
│
├── data/
│   └── ad_10000records.csv
├── logs/
│   └── process.log
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── data_transformation.py
│   ├── model.py
│   ├── predict_pipeline.py
│   └── utils.py
├── main.py
├── app.py
├── README.md
└── requirements.txt
              # Project documentation
```

## Exploratory Data Analysis

1. **Date and Time Features**:
   - Extracted **hour**, **day of the week**, and **month** from the `Timestamp`.
   - Analyzed user interaction patterns based on these features.

2. **Distribution Analysis**:
   - Analyzed numerical features like **Area Income**, **Daily Internet Usage**, and **Daily Time Spent on Site**.
   - Binned features into ranges to identify significant patterns.

3. **Click Analysis**:
   - Investigated how user characteristics affect the likelihood of clicking on an ad.

### Key Insights:
- **Daily Time Spent on Site** and **Daily Internet Usage** are strong indicators of click behavior.
- **Income** tends to have a significant impact on ad engagement.

## Feature Engineering

1. **New Features**:
   - **Is_Weekend**: Identifies weekend days (Saturday and Sunday).
   - **Time_Spent_Ratio**: Ratio of time spent on the site to overall internet usage.
   - **Income_Per_Age**: Proxy metric for economic behavior across age groups.
   - **Age Grouping**: Users are categorized as Teen, Young Adult, Adult, or Senior.
   - **Income Bracket**: Users are classified into low, middle, or high income using quantile binning.

2. **Box-Cox Transformation**:
   - Applied to numerical features for normalization.

3. **Encoding and Scaling**:
   - One-hot encoding for categorical features.
   - Standardization using RobustScaler for numerical features.

## Modeling

The following classifiers were evaluated:
- **Logistic Regression**: Baseline model with hyperparameter tuning.
- **Decision Tree**: Simple decision-based model.
- **Random Forest**: Ensemble learning model to handle feature interactions.
- **Gradient Boosting**: Focuses on boosting weak learners.
- **XGBoost**: Advanced boosting model known for high performance.

### Hyperparameter Tuning
Hyperparameters were tuned using **GridSearchCV** to find the best configuration for Logistic Regression.

**Best Parameters**:
- Regularization Strength (`C`): 1
- Regularization Type (`penalty`): l2
- Solver (`solver`): lbfgs

### Model Evaluation Metrics:
- **Accuracy**: Measures overall performance.
- **Precision**: Evaluates the correctness of positive predictions.
- **Recall**: Assesses the ability to capture positive instances.
- **F1 Score**: Harmonic mean of precision and recall.
- **ROC AUC Score**: Represents the model's ability to distinguish between classes.

## Results

**Performance on Test Data**:
- **Accuracy**: 88%
- **Precision**: 87%
- **Recall**: 87%
- **F1 Score**: 87%
- **ROC AUC**: 95%


The Logistic Regression model performed well, achieving a high AUC score without overfitting, indicating a strong ability to discriminate between users who clicked on ads and those who did not.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/tadeni00/ML_ZOOMCAMP_2024/click_through_rate_analysis.git
   cd click_through_rate_analysis
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook click_through_rate.ipynb
   ```

3. Follow the steps in the notebook to load data, explore, and build models.

## Conclusion

The project provides a comprehensive analysis of factors influencing ad clicks and a robust predictive model. The findings reveal that user engagement time, age, and income significantly impact click-through rates. The Logistic Regression model with optimized hyperparameters delivers reliable performance, making it a suitable choice for predicting user behavior.

### Future Enhancements:
- Implement more advanced models like Neural Networks.
- Explore feature interactions using SHAP values for better interpretability.
- Incorporate real-time prediction capabilities using a deployed model API.

This project provides a solid foundation for understanding user behavior in digital advertising and improving ad targeting strategies based on user characteristics.