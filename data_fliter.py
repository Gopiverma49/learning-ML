import pandas as pd

data ={
    "name":['gopi','kapil','jarvis','aman','sushil'],
    "age":[12,None,34,12,None],
    "salary":[120,235,None,122,None]
}

dp=pd.DataFrame(data)
print(dp)

# print(dp.isnull().sum())
# dp_drop=dp.dropna()
# print(dp_drop)

dp['age'] = dp['age'].fillna(dp['age'].mean())
dp['salary'] = dp['salary'].fillna(dp['salary'].mean())

print(dp)