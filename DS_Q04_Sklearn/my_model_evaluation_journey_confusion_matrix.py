"""
Evaluate the model prediction model for a data set using confusion matrix method.

n the field of machine learning and specifically the problem of statistical classification, a confusion matrix, also known as an error matrix, is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix). Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class (or vice versa). The name stems from the fact that it makes it easy to see if the system is confusing two classes (i.e. commonly mislabeling one as another).

It is a special kind of contingency table, with two dimensions ("actual" and "predicted"), and identical sets of "classes" in both dimensions (each combination of dimension and class is a variable in the contingency table).

Create a function my_model_evaluation_journey_confusion_matrix which will calculate the Confusion Matrix for a predicted model.

You will receive two arguments: true data and predicted data. Both of them are integers.

"""
import pandas as pd
from io import StringIO
from sklearn.metrics import confusion_matrix

def my_model_evaluation_journey_confusion_matrix(true_data_str, pred_data_str):
    # Convert strings to DataFrames
    df_true = pd.read_csv(StringIO(true_data_str))
    print("20df_true: ", df_true)
    df_pred = pd.read_csv(StringIO(pred_data_str))

    # Drop the robot_model_name column
    df_true = df_true.drop("robot_model_name", axis="columns")
    print("46df_true: ", df_true)
    df_pred = df_pred.drop("robot_model_name", axis="columns")

    # Find the common columns between true and predicted data
    common_columns = df_true.columns.intersection(df_pred.columns)
    if common_columns.empty:
        # print("No common columns found")
        return False
    
    # Select only the common columns
    df_true = df_true[common_columns]
    df_pred = df_pred[common_columns]

    # Make the DFs the same number of rows
    min_len = min(len(df_true), len(df_pred)) # Get the minimum length
    df_true = df_true.iloc[:min_len] # Trim the first DF
    df_pred = df_pred.iloc[:min_len] # Trim the second DF
    print("df_true: ", df_true)
    print("df_pred: ", df_pred)
    print("min_len: ", min_len)

    # Calculate the confusion matrix
    cm = confusion_matrix(df_true, df_pred) # Calculate the confusion matrix
    print("cm: ", cm)
    return True

true_data = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
pred_data = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
my_model_evaluation_journey_confusion_matrix(true_data, pred_data) # True

