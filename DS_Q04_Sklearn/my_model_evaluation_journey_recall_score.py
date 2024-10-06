"""
Evaluate the model prediction model for a data set using recall score method.

The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples. The best value is 1 and the worst value is 0.

Create a function my_model_evaluation_journey_recall_score which will calculate the Recall Score for a predicted model.

You will receive two arguments: true data and predicted data. Both of them are integers.

Average = None

:type  param_1: {Integer[]}

:type  param_2: {Integer[]}
:rtype: boolean

def my_model_evaluation_journey_recall_score(param_1, param_2):

"""

from sklearn.metrics import recall_score

def my_model_evaluation_journey_recall_score(param_1, param_3):
    try:
        # Do both lists have the same length?
        if len(param_1) != len(param_3):
            return False
        rs = recall_score(param_1, param_3, average=None)
        print("rs: ", rs)
        return True
    except Exception as e:
        print("An error occurred: ", e)
        return False
    
param_1 = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
param_2 = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
result = my_model_evaluation_journey_recall_score(param_1, param_2) # True
print("result: ", result)