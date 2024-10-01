"""
Evaluate the model prediction model for a data set using confusion matrix method.

n the field of machine learning and specifically the problem of statistical classification, a confusion matrix, also known as an error matrix, is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix). Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class (or vice versa). The name stems from the fact that it makes it easy to see if the system is confusing two classes (i.e. commonly mislabeling one as another).

It is a special kind of contingency table, with two dimensions ("actual" and "predicted"), and identical sets of "classes" in both dimensions (each combination of dimension and class is a variable in the contingency table).

Create a function my_model_evaluation_journey_confusion_matrix which will calculate the Confusion Matrix for a predicted model.

You will receive two arguments: true data and predicted data. Both of them are integers.

"""

from sklearn.metrics import confusion_matrix

def my_model_evaluation_journey_confusion_matrix(true_data_str, pred_data_str):
    try:
        # Do both lists have the same length?
        if len(true_data_str) != len(pred_data_str):
            return False
        cm = confusion_matrix(true_data_str, pred_data_str)
        print("cm: ", cm)
        return True
    except Exception as e:
        print("An error occurred: ", e)
        return False

true_data = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
pred_data = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
result = my_model_evaluation_journey_confusion_matrix(true_data, pred_data) # True
print("result: ", result)
