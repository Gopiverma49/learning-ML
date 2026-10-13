from sklearn.linear_model import LinearRegression, LogisticRegression
model=LinearRegression()
model2=LogisticRegression()

X=[[1],[2],[3],[4],[5]]
y1=[40,50,65,75,90]
y=[0,0,1,1,1]

model.fit(X,y1)
model2.fit(X,y)

hrs=float(input("how much hours did u study- "))
predict_mark=model.predict([[hrs]])
predict_pf=model2.predict([[hrs]])[0]
print(predict_mark)
print(predict_pf)

