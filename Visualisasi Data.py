#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
# reading the database 
data = pd.read_csv("data_bank.csv")
# printing the top 10 rows 
display(data.head (10))


# In[44]:


import pandas as pd 
import matplotlib.pyplot as plt
# reading the database 
data = pd.read_csv("data_bank.csv")

# Scatter plot with day against tip 
plt.scatter (data['education'], data['age'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels 
plt.xlabel('Education')
plt.ylabel('Age')

# Saving the figure.
plt.savefig("ScatterPlot1.jpg")

plt.show()


# In[43]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data_bank.csv")

# Scatter plot with day against tip 
plt.scatter(data['age'], data['day'], c=data['duration'], 
            s=data['campaign'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Age')
plt.ylabel('Duration')

plt.colorbar()

# Saving the figure.
plt.savefig("ScatterPlot3.jpg")

plt.show()


# In[42]:


import pandas as pd 
import matplotlib.pyplot as plt
# reading the database 
data = pd.read_csv("data_bank.csv")

# Scatter plot with day against tip 
plt.plot(data['duration']) 
plt.plot(data['day'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y labels 
plt.xlabel('Duration')
plt.ylabel('Day')

# Saving the figure.
plt.savefig("ScatterPlot2.jpg")

plt.show()


# In[29]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data_bank.csv")

# Bar chart with day against tip 
plt.bar(data['age'], data['duration'])

plt.title("Bar Chart")

# Setting the X and Y labels 
plt.xlabel('Age') 
plt.ylabel('Duration')

# Adding the Legends 
plt.show()


# In[41]:


import pandas as pd 
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data_bank.csv")

# histogram of total_bills 
plt.hist(data['marital'])

plt.title("Histogram")

# Saving the figure.
plt.savefig("Histogram.jpg")

# Adding the Legends 
plt.show()


# In[40]:


import matplotlib.pyplot as plt 
import pandas as pd

# Reading the tips.csv file 
data = pd.read_csv('data_bank.csv')

# initializing the data
marital = ['married', 'single', 'divorced',] 
age = [23, 30, 22]

# plotting the data 
plt.pie(age, labels=marital)

# Adding title to the plot 
plt.title("Status Marital")

# Saving the figure.
plt.savefig("Piechart.jpg")

plt.show()


# In[39]:


import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("data_bank.csv")

# Bar chart with day against tip 
plt.bar(data['age'], data['duration'])

# Saving the figure.
plt.savefig("Barchart.jpg")


# In[ ]:




