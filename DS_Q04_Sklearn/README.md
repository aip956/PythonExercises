Enter venv:
Change directory (to Exercises)

create venv: python3 -m venv new_venv

activate the venv: source new_venv/bin/activate

install pip: 
python3 -m pip install --upgrade pip

install scikit-learn:
pip install scikit-learn


r2
Mean Squared Error
Mean Absolute Error
Confusion Matrix
Accuracy Score
Recall Score


# Welcome to Ds Quest04
***

## Task
This quest introduces the process of model evaluation using various methods, such as R-Squared, Mean Squared Error, Confusion Matrix, and more. The task is to implement functions that calculate these metrics using sklearn's metrics functions, comparing them to given datasets.

## Description
To solve the problem, I have created several Python functions that evaluate model predictions based on the methods provided in the quest. These functions use the sklearn library for model evaluation metrics. The datasets are first converted into pandas dataframes, then the necessary metrics are calculated and returned.

For the R-Squared task, I calculated the R-Squared value between true and predicted data.
Similarly, for tasks like Mean Squared Error and Mean Absolute Error, I computed the errors by comparing true vs. predicted values.
For classification tasks, I used methods such as confusion matrix, accuracy score, recall score, and F1 score to evaluate the model's performance.

## Installation
Create venv: python3 -m venv new_venv

Activate the venv: source new_venv/bin/activate

Install pip: 
python3 -m pip install --upgrade pip

Install scikit-learn:
pip install scikit-learn

## Usage
Change to directory: cd ex01
Comment out the inputs and function call: my_model_evaluation_journey_mean_absolute_error(true_data, pred_data)


### The Core Team
