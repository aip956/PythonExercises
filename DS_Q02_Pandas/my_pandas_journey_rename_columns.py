# Create a function which receive a pandas dataframe, 
# a need_to_be_renamed and into_what as parameter and 
# returns data frame with the column need_to_be_renamed 
# rename with into_what.

import pandas as pd
from io import StringIO

def my_pandas_journey_rename_columns(data, col_name, new_col_name):
    df = pd.read_csv(StringIO(data))
    df.rename(columns={col_name: new_col_name}, inplace=True)
    print("Data frame: ", df)
    return df


data1 = "Index,State,Y2002,Y2003,Y2004,Y2005,Y2006,Y2007,Y2008,Y2009,Y2010,Y2011,Y2012,Y2013,Y2014,Y2015\nA,Alabama,1296530,1317711,1118631,1492583,1107408,1440134,1945229,1944173,1237582,1440756,1186741,1852841,1558906,1916661\nA,Alaska,1170302,1960378,1818085,1447852,1861639,1465841,1551826,1436541,1629616,1230866,1512804,1985302,1580394,1979143\nA,Arizona,1742027,1968140,1377583,1782199,1102568,1109382,1752886,1554330,1300521,1130709,1907284,1363279,1525866,1647724\nA,Arkansas,1485531,1994927,1119299,1947979,1669191,1801213,1188104,1628980,1669295,1928238,1216675,1591896,1360959,1329341\nC,California,1685349,1675807,1889570,1480280,1735069,1812546,1487315,1663809,1624509,1639670,1921845,1156536,1388461,1644607"
column = "Y2002"
new_column = "Year 2002"
my_pandas_journey_rename_columns(data1, column, new_column)

data2 = "Index,State,Y2002,Y2003,Y2004,Y2005,Y2006,Y2007\nA,D,Delaware,1330403,1268673,1706751,1403759,1441351"
column = "Index"
new_column = "IndexIndexIndexIndex"
my_pandas_journey_rename_columns(data2, column, new_column)