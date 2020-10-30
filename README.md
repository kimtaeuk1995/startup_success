# Predicting Startup Success

# Introduction
In 2016, there were $57.4 million in capital flows of Venture Capital financing, going towards 3,718 companies. However, based on previous data, the mean period for a start up’s Initial Public Offering (IPO) is 7 years, but there were only 39 companies that went public last year. With VCs faced with this 1% chance that an investment will actually be successful, choosing the right founder and startup to bet on can be quite a random process, and is usually done based on quantitative metrics. In order to ultimately predict a founder’s likelihood of success. I will define success as the startup being able to IPO or M&A and unsuccessful companies as companies that have been around for more than 10 years or have not received funding for more than 3 years. 

# Goal
The goal of this project is to use machine learning classificaton methods to determine which companies will succeed within 10 years of initial funding. The two main problems that VCs face are 1) Operating in low-information environment and 2) reliance on outliers. To elaborate on the second point, success of VCs mainly rest on one or two outliers that can bring them 100x or 500x return that can cover the cost of unsuccessful invesetments in portfolio. Keeping that in mind, I want to focus on the fact that VCs do not want to miss out on that one potential unicorn company such as Facebook or Twitter. The model will serve as an initial screener in which VCs can then perform due dilligence on. 

# Methodologies
1. Used Crunchbase API to collect startup data until 2015. 
2. Created new categories by generalizing the 46 unique list into 20 newly created categories then replaced each of 46 unique values in each observation for the respective of new category.
3. Created a binary feature to support features with missing data. These binary features meant to signal whether the observation had value in the feature.
4. Discretization of all features into a maximum of 4 bins using equal frequency instead of equal-width binning to ensure the missing values imputed with "0" and high values would not have too much weight in the newly created bins. 
5. Accomodated for class imbalance using SMOTE (Synthetic Minority Over-Sampling Technique)
6. Tested 4 different machine learning algorithm. (Logistic Regression, Support Vector Machines, Random Forests, XGBoost)
7. Optimized, evaluated, and selected the best model -- Logistic Regression
8. Discovered feature importance
9. Built a flask app for users to test out using startup information, and have them classified by percentage of likelihood of succeding or failing. 

# Findings and Conclusions
The main objective was to generate a model to classify successful companies or startups in a manner that allows to uncover as much successful companies. By building a binary classifier to classify a company as successful or not-successful with a True Positive Rate (TPR) 90.1% and False Positie Rate of 8.1% with 91% Recall it is assumed that the objective was achieved. The model can classify with high efficiency the total of successful companies in the dataset. The machine learning algorithm used is Logistic Regression which provies a fast and easy to interpret and implement model with positive results. 



