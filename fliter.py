import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data={
    'study_hrs':[1,2,3,4,5],
    'score':[40,50,60,70,80]
}

df= pd.DataFrame(data)

ss=StandardScaler()
ssd=ss.fit_transform(df)
print(pd.DataFrame(ssd, columns=['study_hrs','score']))
