# Imports
import pandas as pd
import seaborn as srn
import statistics as sts

# Data import
dataset = pd.read_csv("Churn.csv", sep=";")

# Vizualize
dataset.head()

# Size
dataset.shape

# First problem is give names for the columns
dataset.columns = ["Id","Score","State","Kind","Age","property","Balance","Products","hasCreditCard","Active","Salary","Out"]

dataset.head()

# Explore datas using categories, search errors in the datas each categories

# States
group_by_states =  dataset.groupby(['States']).size()
print(group_by_states)

# Plot these datas
group.plot.bar(color = 'gray')

# Kind
group_by_kind = dataset.groupby(['Kind']).size()

# Plot these datas
group_by_kind.plotbar(color = 'pink')

# Explore columns 

# Score
dataset['Score'].describe()

# Score BoxPlot
srn.boxplot(dataset['Score']).set_title('Score')

# Score histogram
srn.distplot(dataset['Score']).set_title('Score')

# Age
dataset['Age'].describe()

# Age BoxPlot
srn.boxplot(dataset['Age']).set_title('Age')

# Age histogram
srn.distplot(dataset['Age']).set_title('Age')

# Balance

dataset['Balance'].describe()

# Balance BoxPlot
srn.boxplot(dataset['Balance']).set_title('Balance')

# Balance Histogram
srn.distplot(dataset['Balance']).set_title('Balance')

# Salary
dataset['Salary'].describe()

# Salary BoxPlot
srn.boxplot(dataset['Salary']).set_title('Salary')

# Salary Histogram
srn.distplot(dataset['Salary']).set_title('Salary')

# Count Null values
# Kind & Salary

dataset.isnull().sum()





