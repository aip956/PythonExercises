'''
my_data_transform.py

'''
import csv
from io import StringIO

# def my_data_transform(data):
#     lines = data.split("\n")
#     header = lines[0].split(",")
#     result = [header]


#     for line in lines[1:]:
#         if not line:
#             continue
#         # row = line.split(',')
#         # Use  the csv module for parsing
#         row = next(csv.reader(StringIO(line)))
#         # skip line if empty columns
#         if len(row) < len(header):
#             continue
#         # convert age to integer
#         age = int(row[5])
#         if 1 <= age <= 20:
#             row[5] = '1->20'
#         elif 21 <= age <= 40:
#             row[5] = '21->40'
#         elif 41 <= age <= 65:
#             row[5] = '41->65'
#         elif 66 <= age <= 99:
#             row[5] = '66->99'
#         else:
#             row[5] = 'unknown'

#         # Time of day
#         order_time = int(row[-1].split()[1].split(':')[0])
#         if  6 <= order_time <= 12:
#             row[-1] = 'morning'
#         elif 12 <= order_time <= 18:
#             row[-1] = 'afternoon'
#         elif 18 <= order_time:
#             row[-1] = 'evening'
#         else: row[-1] = 'unknown'

#         result.append(row)
    

#     if result[-1] == ['']:
#         result.pop()

#     return result


def my_data_transform(csv):
    lines = csv.strip().split('\n')
    # Added the header line to the transformed lines
    transformed_lines = [lines[0]]

    for line in lines[1:]: #Skip header line
        fields = line.split(',')

        # Transform email to domain only
        email = fields[4].split('@')[-1]
        fields[4] = email

        # Extract age from the line
        age = fields[5]
        if age.isdigit():
            age = int(age)
        # Categorize
            if 1 <= age <= 20:
                fields[5] = '1->20'
            elif 21 <= age <= 40:
                fields[5] = '21->40'
            elif 41 <= age <= 65:
                fields[5] = '41->65'
            elif 66 <= age <= 99:
                fields[5] = '66->99'
        else:
            fields[5] = 'Unknown'

        # Time of day
        order_datetime = fields[-1].strip()
        order_time = int(order_datetime.split()[1].split(':')[0])

        if  6 <= order_time <= 12:
            fields[-1] = 'morning'
        elif 12 <= order_time <= 18:
            fields[-1] = 'afternoon'
        elif 18 <= order_time < 24:
            fields[-1] = 'evening'
        else: fields[-1] = 'unknown'
        # Append line into transformed_lines
        transformed_lines.append(','.join(fields))
    # print(transformed_lines)
    return transformed_lines

print(my_data_transform("Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"))

'''
input:
"Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\n
    Male,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\n
    Male,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\n
    Female,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\n
    Female,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\n
    Male,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"
    
this is the expected output:
 Expected Return Value  
["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At", 
"Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon", 
"Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon", 
"Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon", 
"Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning", 
"Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]                                                                                                         

['Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At', 'Male,Carl,Wilderman,carl,yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon', 'Male,Marvin,Lind,marvin,hotmail.com,66->99,Detroit,Chrome Android,2,afternoon', 'Female,Shanelle,Marquardt,shanelle,hotmail.com,21->40,Las Vegas,Chrome,1,afternoon', 'Female,Lavonne,Romaguera,lavonne,yahoo.com,66->99,Seattle,Chrome,2,morning', 'Male,Derick,McLaughlin,derick,hotmail.com,41->65,Chicago,Chrome Android,1,afternoon']


My output:        
["Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At",
"Male,Carl,Wilderman,carl,wilderman_carl@yahoo.com,21->40,Seattle,Safari iPhone,2,afternoon",
"Male,Marvin,Lind,marvin,marvin_lind@hotmail.com,66->99,Detroit,Chrome Android,2,afternoon",
"Female,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21->40,Las Vegas,Chrome,1,afternoon",
"Female,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,66->99,Seattle,Chrome,2,morning",
"Male,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,41->65,Chicago,Chrome Android,1,afternoon"]    
'''    