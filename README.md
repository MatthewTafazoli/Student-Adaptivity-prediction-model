# Student-Adaptivity-prediction-model

## Problem Description and Overview
This repository seeks to create and serve a model that infers a student's adaptability based on the student's socio-demographic factors. The dataset is a table of the socio-demographic factors of many foreign-born student and their respective ability to adapt to an IT-centric education. 

## Dataset Details
The dataset contains the data of 1204 students, each with 13 socio-economic values and a 14th "adaptivity" level based on those aformentioned values. 
The 13 values themselves are:

1. Gender: Boy or Girl
2. Age: 6 different 5 year age ranges spanning from 6-10 years old to 26-30 years old
3. Education Level: School (yet to reach Higher Education), College or University
4. Institution Type: Government or Non-Government
5. IT Student: Yes or No
6. Location: Yes or No
7. Load-Shedding (inconsistent electricity supplied due to surrounding economic factors): Yes or No
8. Financial Condition: Poor, Mid or Rich
9. Internet Type: Mobile Data or Wifi
10. Network Type: 2G, 3G or 4G
11. Class Duration: 0 hours, 1-3 hours or 3-6 hours
12. Self LMS (Whether they use self-teaching modules): Yes or No
13. Device: Computer, Mobile or Tablet

Additionally, each student is given a 14th "Adaptivity" value, that can be either "Low", "Mid", or "High". We seek to predict the Adaptivity value of students based on the above 13 values provided. 

## Analyzing the data, choosing the classifier, and training the model

From a simple data analysis (further details and visualization can be found in the .ipynb file in this repository), there are no particularly strong correlations between any two features in the dataset. Furthermore, some features are skewed more heavily towards one particular value (but no specific feature is greater than 5 to 1). However, there are no gaps/null values in the dataset and every student has all 14 values accounted for.

All values contained in the dataset are non-numeric, so during the model training and when the saved model is queried, we transform the data from non-numeric to corresponding numerical values. 

The dataset was divided with a simple 70/30 split, and trained using 10 different classifiers (Logistic Regression, Linear Discriminate Analysis, Decision Tree, Random Forest, Bagging, Gradient Boosting, ADA boost, XGB, Extra Trees, and a Voting Classifier composed of Extra Trees/Random Forest). 

Comparing the classification report, the Voting classifier composed of the Extra Trees and Random Forest classifiers returned the highest scores (93% Train Accuracy and 91% Test Accuracy), and thus was chosen as the model we would use for serving.

## How to install dependencies
For deploying the API from a clean Python 3.9 environment, this repository contains a requirements.txt that can be installed with the following command line command:

With that we should be able to serve the API using the files from this repository.
An example .json file is provided that models the type of query this model accepts. 

## How to train the model, run the serving code
A saved version of the model is provided already to be used by the API. If you wish to generate a file on your own, or modify that way we train the model:
1. Open the .ipynb in colab
2. Select "run all" from "runtime" in the toolbar
3. Download the data.csv from this repository and provide it in the first cell of the notebook
4. After the above steps, a .sav file should be produced in the notebooks directory which you can download to your local directory

Once you have the .sav file of the model, run the API python file from the same directory, and that should bring up the API endpoint

## How to query the model
With the API endpoint up and running, we can run single sample queries against the model and return it's prediction. The script accepts json inputs that match the format of the data in the dataset. Query data is case-sensitive and requires exact spelling, so confirm with the of the csv file when an error arise (the api is written to return an error when there is an issue with a givene input field). 

We use the following for the API Endpoint: http://127.0.0.1:5000/json

Post Requests can be made either from the command line or any other software for making API calls (see example of PostMan below)
