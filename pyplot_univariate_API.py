import matplotlib.pyplot as plt  
import pandas as pd  
data = {"salary":[25000,30000,90000,50000,70000,0]}
df = pd.DataFrame(data)
#print(df)
#plt.plot(df["salary"],color = 'red',marker = '*',linestyle = ':',linewidth =2)
#plt.grid()
#plt.show()
#plt.hist(df["salary"])
#plt.show()
#plt.boxplot(df["salary"])
#plt.show()
df["dept"] = ['hr','it','finance','hr','finance','it']
"""plt.plot(df["salary"])
plt.show()"""

#for numerical we can use boxplot, lineplot and histogram but for visulaising string col we can use pie chart
count = df["dept"].value_counts()
print(count)
"""plt.pie(count)
plt.show()"""

plt.bar(count.index,count,color = ['green','blue','purple'])  # we can visulasie the data using barplot
plt.show()

# it is caleed univariate analysis where one col is visulaed at a time either categorically or numercially
