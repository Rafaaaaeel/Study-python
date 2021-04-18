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

# - Now tratment the datas - 

median = sts.median(dataset['Salary'])

# Change the Null values by median
dataset["Salary"].fillna(median, inplace=True) # inplace change only the data group

# Verify if rest Null values
dataset['Salary'].isnull().sum() # before 7 now 0

# Kind, doesn't have patterning and Null values
group_by_kind = dataset.groupby(['Kind']).size()

# All Null values
dataset['Kind'].isnull().sum()

# Fill by the common value
dataset['Kind'].fillna('Male', inplace=True)

# Verify again null values
dataset['Kind'].isnull().sum() # before 8 now 0

# Patterning by domain

dataset.loc[dataset['Kind'] == 'M', 'Kind'] == "Male"
dataset.loc[dataset['Kind'].isin(['Won', 'W']), 'kind'] = 'Woman'

# Vizualing results

group_by_kind = dataset.groupby(['Kind']).size()

# Age outline

dataset['Age'].describe()

# Vizualizing problem size
dataset.loc[(dataset['Age'] < 0) | (dataset['Age'] > 120)]

median = sts.median(dataset['Age'])

# Replace
dataset.loc[(dataset['Age'] < 0) | (dataset['Age'] > 120), 'Age'] = median

# Verify again
dataset.loc[(dataset['Idade'] > 0) | ( dataset['Idade'] < 120)]

# Duplicate values, search by id
dataset[dataset.duplicated(['Id'], keep=False)]

# Remove by ID
dataset.drop_duplicates(subset="Id", keep="first", inplcae=True)

# Verify again
dataset[dataset.duplicated(['Id'], keep=False)]

# States out patterning
group_by_states = dataset.groupby(['States']).size()

# Assigning common value
dataset.loc[dataset['States'].isin(['RP','SP','TF']), 'States'] = 'RS'

# Verify again
group_by_states = dataset.groupby(['States']).size()

# Salary OutLiers, whereas clause two default values
desv = sts.stdev(dataset['Salary'])

# Checking if has a true criterion
dataset.loc[dataset['Salary'] >= 2 * desv]

# Updatating salary by median, calculating
median = sts.median(dataset['Salary'])

# Atributes
dataset.loc[dataset['Salary'] >= 2 * desv, 'Salary'] = median

# Checking again
dataset.loc[dataset['Salary'] >= 2 desv]

dataset.head()
dataset.shape # (988,12)







