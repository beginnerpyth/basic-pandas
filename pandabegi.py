import pandas as pd
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"],index=["x","y","o"])
print(df.head())
print(df)
print(df.tail(2))
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
print(df.nunique())
print(df["A"].unique())
print(df.shape)
print(df.size)
musashino=pd.read_csv("pand.csv")
print(musashino.sample(10,random_state=1))#so it does to make the output same like in numpy where seed=1
#print(musashino.head())
#results=pd.read_parquet('results.parquet')
#olympics=pd.read_excel("olympics-data.xlsx",sheet_name="results")
#print(olympics)
#print(musashino.loc[0:3,['Date','Pulse']])#it allows us to locate rows and column we use index as row and name as column
#print(musashino.iloc[:,0])#the rows and column is same as numpy using index value
#musashino.index=musashino["Date"]#now the index has been hanged into date and its data
musashino.loc[27,'Maxpulse']=22
print(musashino)
print(musashino.sample(10,random_state=1))
musashino.loc[1:3,['Pulse']]=25
print(musashino.head(10))
print(musashino.iat[0,1])
print(musashino.iloc[0:3,[0,3]])
