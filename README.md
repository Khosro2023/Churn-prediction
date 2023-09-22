# README: Customer Churn Analysis for Financial Institution

## Introduction

This README provides an overview of the Customer Churn Analysis project for a financial institution. The primary objective of this project is to analyze the client database to identify patterns and factors that may lead to customers closing their bank accounts after accepting products from other institutions. The project involves feature engineering, clustering, and classification using machine learning algorithms, including Logistic Random Forest, Gradient Boosting, and Support Vector Machines with Weighted Error Minimization (SVM WEM).

## Project Description

### Feature Engineering

In this project, we focus on feature engineering to gain insights into customer behavior and factors affecting churn. This includes converting existing features into Dominic future features. Dominic future features are a specialized transformation of data attributes that can enhance predictive power in machine learning tasks. The goal is to identify the most relevant features that influence customer churn.

### Clustering and Classification

After feature engineering, the project employs various machine learning algorithms for clustering and classification tasks:

- **Logistic Random Forest**: This algorithm is used to build predictive models that estimate the probability of a customer churning. It helps identify which customers are more likely to close their bank accounts.

- **Gradient Boosting**: Gradient boosting is used to improve the accuracy of churn predictions by creating an ensemble of decision trees. It can capture complex relationships between features and churn behavior.

- **Support Vector Machines with Weighted Error Minimization (SVM WEM)**: SVM WEM is used to classify customers into groups based on their likelihood of churning. It assigns different weights to misclassified samples, making it effective in handling imbalanced datasets common in churn analysis.

## Dependencies

To run this project, you will need the following Python libraries with the specified versions:

- numpy==1.24.3
- pandas==2.0.3
- ipykernel==6.23.1
- matplotlib==3.7.1
- scikit-learn==1.3.0
- nbformat==5.9.2

## Usage

1. Clone the project repository to your local machine.

2. Install the required dependencies.

3. Utilize Jupyter notebooks or the project's main script to perform feature engineering, clustering, and classification tasks.

## License

This project is licensed under the MIT License.

## Contact Information

For any questions or inquiries related to this project, please contact [Your Name] at [Your Email].

Thank you for considering the Customer Churn Analysis project to improve revenue and customer retention in your financial institution. We hope this project provides valuable insights into customer behavior and churn prediction.