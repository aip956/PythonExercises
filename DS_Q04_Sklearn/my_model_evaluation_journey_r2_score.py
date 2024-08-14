import pandas as pd
from io import StringIO
from sklearn.metrics import r2_score 

def my_model_evaluation_journey_r2_score(data):
    # Split the data into true and predicted data
    true_data_str, pred_data_str = data.split("&&")
    print("true_data_str: ", true_data_str)
    print("pred_data_str: ", pred_data_str)

    # Strip leading/trailing whitespace
    true_data_str = true_data_str.strip()
    pred_data_str = pred_data_str.strip()

    # Convert the strings to DataFrames
    true_data = pd.read_csv(StringIO(true_data_str))
    pred_data = pd.read_csv(StringIO(pred_data_str))

    # Are DFs same shape?
    if true_data.shape != pred_data.shape or not all(true_data.columns == pred_data.columns):
        raise ValueError("Not same shape")
    
    # Extract relevant colums for calc
    true_vals = true_data.drop(columns=["robot_model_name"])
    pred_vals = pred_data.drop(columns=["robot_model_name"])

    # Calc R-sq val
    r2 = r2_score(true_vals, pred_vals)
    print("r2: ", r2)
    return r2

input = """
robot_model_name,nbr_pieces_head,nbr_pieces_arms,nbr_pieces_legs,nbr_pieces_body\n
da Vinci Surgical System,4377,47000,97969,37320\n
KITT,90043,73282,18868,45540\n
The Tachikomas,2114,68111,75162,36340\n
Toyota violin-playing,63730,85704,78717,57020\n
ERTY,81519,26677,65519,43420\nMega Man,22714,9740,73137,26380\n
Rock \u2018Em Sock \u2018Em Robots,87886,67925,58101,53460\n
Doraemon,16788,85783,86233,47200\n
Awesom-O,7448,54163,33401,23740\n
HK-47,46131,58449,92296,49200\n
ED-209,77228,10734,54945,35720\n
Beer-Fetching Robot,59627,81878,23861,41340\n
Bishop,96414,66998,4115,41880\n
The Energizer Bunny,68804,14932,37880,30400\n
H.E.L.P.eR.,78159,8060,63274,37360\n
Clank,11578,84323,86292,45540\n"
 && 
 "robot_model_name,nbr_pieces_head,nbr_pieces_arms,nbr_pieces_legs,nbr_pieces_body\n
 Clank,43973,25595,58504,32000\n
 Daft Punk,96371,61676,31481,47380\n
 Johnny 5,66511,38385,47953,38200\n
 The Robot,58752,89090,51497,49820\n
 Mr. Roboto,94246,12826,74877,45480\n
 Marvin the Paranoid Android,53874,16704,21492,23000\n
 Lego Mindstorms NXT,483,48426,29257,19540\n
 Robbie,22657,2013,75082,24920\n
 Astro Boy,34499,33062,86296,38460\n
 The Iron Giant,57496,90149,29823,44360\n
 Optimus Prime,13205,4869,76120,23540\n
 Roomba,22875,32377,76437,32920\n
 DJ Roomba,68704,8287,77907,38720\n
 Cindi Mayweather,17676,41995,68166,31940\n
 Mark Z,85325,88067,64264,59400\n
 Rosie,83044,74974,41489,49860\n
 Crow T. Robot/Tom Servo,96983,26930,21595,36360\n
 K-9,35898,69605,83592,47260\n
 The Terminator,65268,47748,50964,40980\n
 The Maschinenmensch,10278,91180,46682,37020\n
 ASIMO,4955,37023,59065,25260\n
 GLaDOS,59036,20960,26556,26620\n
 The Final Five,83686,46654,71010,50320\n
 Sojourner,56273,199,31862,22080\n
 Data,86581,27309,21246,33780\n
 R2D2,45064,59797,37373,35540\n
 Bender Bending Rodriguez,61198,51705,13208,31520\n
 Wall-E,66709,19032,72116,39460"""
my_model_evaluation_journey_r2_score(input)

