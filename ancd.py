import plotly.express as px
# This dataframe has 244 lines, but 4 distinct values for `day`
df = px.data.tips()
d = []
cc = {"format" : "British Parli" ,"perc" : 20}
bc = {"format" : "LD" , "perc" : 20}
print(cc,bc)
d.append(cc)

fig = px.pie(df, values='cc["perc"]', names='cc["format"]')
fig.show()