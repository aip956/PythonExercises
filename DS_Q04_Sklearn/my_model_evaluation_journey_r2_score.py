import pandas as pd
from io import StringIO
from sklearn.metrics import r2_score 

def my_model_evaluation_journey_r2_score(true_data_str, pred_data_str):
    # Split the data into true and predicted data
    # true_data_str, pred_data_str = data.split("&&")
    # print("true_data_str: ", true_data_str)
    # print("pred_data_str: ", pred_data_str)

    # Strip leading/trailing whitespace
    true_data_str = true_data_str.strip()
    pred_data_str = pred_data_str.strip()

    # Convert the strings to DataFrames
    true_data = pd.read_csv(StringIO(true_data_str))
    pred_data = pd.read_csv(StringIO(pred_data_str))

    # Align datasets based on robot_model_name
    merged_data = pd.merge(true_data, pred_data, on="robot_model_name", suffixes=('_true', '_pred'))

    # Make the shapes match by trimming extra rows
    true_vals = merged_data.filter(regex='true$').values.flatten()
    pred_vals = merged_data.filter(regex='pred$').values.flatten()

    # Calc R-sq val
    r2 = r2_score(true_vals, pred_vals)
    print("r2: ", r2)
    return r2

true_data = """robot_model_name,nbr_pieces_head,nbr_pieces_arms,nbr_pieces_legs,nbr_pieces_body\nda Vinci Surgical System,4377,47000,97969,37320\nKITT,90043,73282,18868,45540\nThe Tachikomas,2114,68111,75162,36340\nToyota violin-playing,63730,85704,78717,57020\nGERTY,81519,26677,65519,43420\nMega Man,22714,9740,73137,26380\nRock \u2018Em Sock \u2018Em Robots,87886,67925,58101,53460\nDoraemon,16788,85783,86233,47200\nAwesom-O,7448,54163,33401,23740\nHK-47,46131,58449,92296,49200\nED-209,77228,10734,54945,35720\nBeer-Fetching Robot,59627,81878,23861,41340\nBishop,96414,66998,4115,41880\nThe Energizer Bunny,68804,14932,37880,30400\nH.E.L.P.eR.,78159,8060,63274,37360\nClank,11578,84323,86292,45540\n"""
pred_data = """robot_model_name,nbr_pieces_head,nbr_pieces_arms,nbr_pieces_legs,nbr_pieces_body\nClank,43973,25595,58504,32000\nDaft Punk,96371,61676,31481,47380\nJohnny 5,66511,38385,47953,38200\nThe Robot,58752,89090,51497,49820\nMr. Roboto,94246,12826,74877,45480\nMarvin the Paranoid Android,53874,16704,21492,23000\nLego Mindstorms NXT,483,48426,29257,19540\nRobbie,22657,2013,75082,24920\nAstro Boy,34499,33062,86296,38460\nThe Iron Giant,57496,90149,29823,44360\nOptimus Prime,13205,4869,76120,23540\nRoomba,22875,32377,76437,32920\nDJ Roomba,68704,8287,77907,38720\nCindi Mayweather,17676,41995,68166,31940\nMark Z,85325,88067,64264,59400\nRosie,83044,74974,41489,49860\nCrow T. Robot/Tom Servo,96983,26930,21595,36360\nK-9,35898,69605,83592,47260\nThe Terminator,65268,47748,50964,40980\nThe Maschinenmensch,10278,91180,46682,37020\nASIMO,4955,37023,59065,25260\nGLaDOS,59036,20960,26556,26620\nThe Final Five,83686,46654,71010,50320\nSojourner,56273,199,31862,22080\nData,86581,27309,21246,33780\nR2D2,45064,59797,37373,35540\nBender Bending Rodriguez,61198,51705,13208,31520\nWall-E,66709,19032,72116,39460"""

my_model_evaluation_journey_r2_score(input)

