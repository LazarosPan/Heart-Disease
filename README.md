# Heart Disease Detection using Machine Learning

## Overview

This project investigates the application of machine learning and data mining techniques to improve the early detection and prediction of cardiovascular diseases (CVDs). Given the global impact of heart disease as a leading cause of mortality, this project leverages various machine learning algorithms and data preprocessing methods to enhance the predictive accuracy of heart disease detection models.

## Table of Contents
1. [Introduction](#introduction)
2. [Objectives](#objectives)
3. [Preprocessing and Data Handling](#preprocessing-and-data-handling)
    - [Feature Selection](#feature-selection)
    - [Oversampling Techniques](#oversampling-techniques)
    - [Dimensionality Reduction](#dimensionality-reduction)
4. [Machine Learning Models](#machine-learning-models)
5. [Results and Comparison](#results-and-comparison)
6. [Conclusion and Future Work](#conclusion-and-future-work)
7. [References](#references)

## Introduction

Cardiovascular diseases (CVDs) are a leading cause of death worldwide. Early diagnosis is essential for effective treatment and improving patient outcomes. This project utilizes machine learning algorithms to create models that predict the onset of heart disease based on clinical features and health indicators.

## Objectives

- To implement and compare various machine learning algorithms for heart disease prediction.
- To explore the impact of different data preprocessing techniques such as feature selection and oversampling.
- To evaluate the effect of dimensionality reduction techniques like PCA on model performance.
- To compare model accuracy, interpretability, and efficiency across different feature sets.

## Preprocessing and Data Handling

### Feature Selection

Feature selection techniques were applied to reduce the number of variables, improving model performance by eliminating irrelevant or redundant features. This step helps in optimizing model complexity and enhancing classification accuracy.

### Oversampling Techniques

Due to the challenge of unbalanced datasets, oversampling methods were employed to address underrepresented classes. The following oversampling techniques were applied:
- **ADASYN**
- **Borderline SMOTE**
- **KMeans SMOTE**
- **SMOTE**

KMeans was used as a pre-processing step within SMOTE to improve the balancing of the dataset.

### Dimensionality Reduction

After feature selection, **Principal Component Analysis (PCA)** was applied to further reduce the dimensionality of the data. This step aimed to improve model performance by transforming the selected features into a lower-dimensional space.

## Machine Learning Models

The following machine learning algorithms were implemented:
- **RandomForestClassifier** (from sklearn.ensemble)
- **KNeighborsClassifier** (from sklearn.neighbors)
- **QuadraticDiscriminantAnalysis** (from sklearn.discriminant_analysis)
- **MLPClassifier** (from sklearn.neural_network)
- **XGBClassifier** (from xgboost)
- **LGBMClassifier** (from lightgbm)

These models were applied under three conditions:
1. Using all features without selection or dimensionality reduction.
2. After applying feature selection.
3. After applying PCA for dimensionality reduction.

## Results and Comparison

The performance of the models was evaluated and compared across different feature sets (all features, selected features, and PCA-transformed features). Metrics such as accuracy, precision, recall, and F1-score were used to determine the best-performing model for heart disease detection.

## Conclusion and Future Work

In this review, the critical role of machine learning and data mining algorithms in the early detection and prediction of cardiovascular diseases (CVDs) was explored. Data preprocessing techniques, such as ensemble preprocessing and oversampling, were essential to improving model accuracy. Feature selection and dimensionality reduction further refined model performance by reducing complexity and improving classification outcomes. Among the classification techniques, Decision Trees and Random Forests often provided higher accuracy.

Despite these advancements, challenges such as data quality and model interpretability remain. Future research should focus on developing hybrid models and incorporating real-world clinical data to validate the findings. The ongoing evolution in machine learning for healthcare holds promise for more precise and individualized detection and treatment of cardiovascular diseases.
