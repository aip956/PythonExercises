'''
my_data_process.py
Our function will group the data and it will become 
a Hash of hash. (Wow.)
Example:
"{'Gender': {'Male': 22, 'Female': 21}, 'Email': {'yahoo.com': 3, 'hotmail.com': 2}, ...}"

We will discard the column FirstName, LastName, UserName and Coffee Quantity from our output.


'''

import json
def my_data_process(data):
    #Join the list of string into a single string
    data_string = "\n".join(data)

    lines = data_string.split("\n")
    header = lines[0].split(",")
    # Columns to exclude
    exclude_columns = ["FirstName","LastName","UserName","Coffee Quantity"]
    
    #Indexes of columns to exclude
    exclude_indexes = [header.index(col) for col in exclude_columns]

    # Exclude columns from header
    header = [col for col in header if col not in exclude_columns]

    # print(header)
    result = {col: {} for col in header}
    
    # for col in header:
    #     result[col] = {}
    # print("29result: ", result)
    
    for line in lines[1:]:
        if not line:
            continue
        row = line.split(",")
        # print("row: ", row)

        # Exclude values based on indexes
        row = [value for i, value in enumerate(row) if i not in exclude_indexes]
        
        if len(row) != len(header):
            continue

        for col, value in zip(header, row):
            
            if value not in result[col]:
                result[col][value] = 1
            else:
                result[col][value] += 1
    # Convert to json
    json_result = str(result).replace(", ", ",").replace(": ",":").replace("'", '"')
 

    # Replace single quotes with double
    # json_result = json_result.replace(",", '"')

    return json_result

input = [
    "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", 
    "Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", 
    "Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", 
    "Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", 
    "Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", 
    "Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]
print(my_data_process(input))