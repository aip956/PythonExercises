# Create a function which receive a pandas dataframe and 
# returns a datafrom without NaN values.
# dropna() drops the rows where at least one element is missing.


import pandas as pd
from io import StringIO

def my_pandas_journey_drop_nan_values(data):
    df = pd.read_csv(StringIO(data))
    print("Data frame without NaN values: ", df.dropna())
    return df.dropna()

data1 = "Index,State,Y2002,Y2003,Y2004,Y2005,Y2006,Y2007,Y2008,Y2009,Y2010,Y2011,Y2012,Y2013,Y2014,Y2015\nA,Alabama,1296530,1317711,1118631,1492583,1107408,1440134,1945229,1944173,1237582,1440756,1186741,1852841,1558906,1916661\nA,Alaska,1170302,1960378,1818085,1447852,1861639,1465841,1551826,1436541,1629616,1230866,1512804,1985302,1580394,1979143\nA,Arizona,1742027,1968140,1377583,1782199,NaN,1109382,1752886,1554330,1300521,1130709,1907284,1363279,1525866,1647724"
my_pandas_journey_drop_nan_values(data1)

data2 = "Index,State,Y2002,Y2003,Y2004,Y2005,Y2006,Y2007,Y2008,Y2009,Y2010,Y2011,Y2012,Y2013,Y2014,Y2015\nA,D,Delaware,1330403,1268673,1706751,1403759,1441351,1300836,1762096,1553585,1370984,1318669,1984027,1671279,1803169,1627508\nD,District of Columbia,1111437,1993741,1374643,1827949,1803852,1595981,1193245,1739748,1707823,1353449,1979708,1912654,1782169,1410183\nF,Florida,1964626,1468852,1419738,1362787,NaN,1278550,NaN,1818438,NaN,1497051,1131928,1107448,1407784,1170389"
my_pandas_journey_drop_nan_values(data2)


