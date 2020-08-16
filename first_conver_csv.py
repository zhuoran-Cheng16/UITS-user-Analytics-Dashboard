from csvtotable import convert

import pandas as pd

from pandas import DataFrame as df

path=u'custom-assets-report.csv'

file=open(path, errors='ignore')



data=pd.read_csv(file,usecols=['Asset Tag', 'Model', 'Serial', 'Active Directory Last Logon', 'Username'])
#data.columns = ['id','deviceID','time','user']
data.to_csv(path_or_buf='file2.csv',index=False)



