"""
Evaluate the model prediction model for a data set using F1 method.

In statistical analysis of binary classification, the F1 score (also F-score or F-measure) is a measure of a test's accuracy. It considers both the precision p and the recall r of the test to compute the score: p is the number of correct positive results divided by the number of all positive results returned by the classifier, and r is the number of correct positive results divided by the number of all relevant samples (all samples that should have been identified as positive).

The F1 score is the harmonic mean of the precision and recall, where an F1 score reaches its best value at 1 (perfect precision and recall). The F1 score is also known as the Sorensen–Dice coefficient or Dice similarity coefficient (DSC).

Create a function my_model_evaluation_journey_f_one which will calculate the F1 Score for a predicted model.

You will receive two arguments: true data and predicted data. Both of them are integers.

Average = None

Prototype:
:type  param_1: {Integer[]}

:type  param_2: {Integer[]}
:rtype: boolean

def my_model_evaluation_journey_f_one(param_1, param_2):

"""
from sklearn.metrics import f1_score

def my_model_evaluation_journey_f_one(param_1, param_2):
    try:
        # Do both lists have the same length?
        if len(param_1) != len(param_2):
            return False
        f1 = f1_score(param_1, param_2, average=None)
        print("f1: ", f1)
        return True
    except Exception as e:
        print("An error occurred: ", e)
        return False
    
param_1 = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
param_2 = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
result = my_model_evaluation_journey_f_one(param_1, param_2) # True
print("result: ", result)
