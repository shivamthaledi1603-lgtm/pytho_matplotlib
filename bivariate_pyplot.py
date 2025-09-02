import matplotlib.pyplot as plt
import pandas as pd
data = {"salary":[25000,30000,40000,50000,60000]}
df = pd.DataFrame(data)
df["salary"]=[25000,30000,40000,50000,60000]
df["age"] =[22,23,25,30,35]
"""print(df.head())
plt.plot(df["salary"],df["age"],color ='red',marker ='o',linestyle=':')
plt.show( )"""

# scatter plot
"""plt.scatter(df["salary"],df["age"],color ='purple', linestyle =':')
plt.show()"""


# bar chart
plt.bar(df["age"],df["salary"],color='green')
plt.show()

