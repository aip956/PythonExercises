'''
Evaluate the model prediction model for a data set using accuracy score method.

Accuracy is one metric for evaluating classification models. Informally, accuracy 
is the fraction of predictions our model got right. Formally, accuracy has the 
following definition: 
Accuracy = Number of correct predictions Total number of predictions.

Create a function my_model_evaluation_journey_accuracy_score which will calculate 
the Accuracy Score for a predicted model.

You will receive two arguments: true data and predicted data. Both of them are integers.

Function prototype (python)

"""
:type  param_1: {Integer[]}
"""
:type  param_2: {Integer[]}
:rtype: boolean
"""
def my_model_evaluation_journey_accuracy_score(param_1, param_2):

'''

from sklearn.metrics import accuracy_score

def my_model_evaluation_journey_accuracy_score(true_data_list, pred_data_list):
    try:
        # Do both lists have the same length?
        if len(true_data_list) != len(pred_data_list):
            return False
        accuracy = accuracy_score(true_data_list, pred_data_list)
        print("accuracy: ", accuracy)
        return True
    except Exception as e:
        print("An error occurred: ", e)
        return False
    
true_data = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
pred_data = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
result = my_model_evaluation_journey_accuracy_score(true_data, pred_data) # True
print("result: ", result)
