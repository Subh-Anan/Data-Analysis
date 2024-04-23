#!/usr/bin/env python
# coding: utf-8

# # PYTHON ASSIGNMENT (SEPTEMBER 2022) by Rwitorshi Probho Roy (GE 22), Subhanan Maity (FE22) and Ayushi Gupta (EE 22)

# In[42]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r'/Users/rwitorshi/Downloads/plfs for assignment.csv')
print (df)


# In[3]:


df.select_dtypes(object).columns


# # Question 1

# Sampling of 10 percent of the observations from the data.
# 
# 'log_wage'using wage is generated

# In[5]:


subset=df.sample(frac=0.1)
subset['log_wage']=np.log(subset['wage'])
subset.to_csv('sample_log_wage.csv')
subset.dtypes


# # Question 2

# In[17]:


subset.dtypes


# We know integers as well as float numbers constitute numeric variables,hence there are 5 numeric variables and rest i.e 'state', 'sex', 'cwstype' and 'edu_cat' are non numeric variables

# In[6]:


subset.head()


# In[7]:


df.select_dtypes(object).columns


# In[9]:


subset.head(4)


# # Question 3

# Worker type i.e. 'cwstype' has been made numeric by assigning codes its categories. The codes 1,2 and 3 has been assigned to the categories "self employed" , "casual labour" and "regular wage/salaried employees" respectively. 

# In[10]:


subset['cwstype1'] = np.where(subset['cwstype'] == 'self employed',1,0 )
subset['cwstype2'] = np.where(subset['cwstype'] == 'casual labour',2,0 )
subset['cwstype3'] = np.where(subset['cwstype'] == 'regular wage/salaried employees',3,0 )
subset['cwstype_num'] = subset['cwstype1'] + subset['cwstype2'] + subset['cwstype3']
subset.drop(["cwstype1", "cwstype2",'cwstype3'], axis = 1, inplace = True)


# In[11]:


subset.head()


# In a similar manner,non numeric variable education category ie 'edu_cat' is made numeric by assigning codes to its categories. The codes 1,2 and 3 have been assigned to the categories  "below middle","Graduate & above" and "secondary & higher" respectively.

# In[12]:


subset['edu_cat1']=np.where(subset['edu_cat']=='below middle',1,0)
subset['edu_cat2']=np.where(subset['edu_cat']=='Graduate & above',2,0)
subset['edu_cat3']=np.where(subset['edu_cat']=='secondary & higher',3,0)
subset['educat_num']=subset['edu_cat1']+subset['edu_cat2']+subset['edu_cat3']
subset.drop(["edu_cat1","edu_cat2","edu_cat3"],axis=1,inplace=True)
subset.head()
    


# # Question 4
# 
# Frequency and Percentage distribution of the following variables have been provided in a tabular format

# a)State 

# In[13]:


state = subset['state'].value_counts()


# In[14]:


STATE = pd.DataFrame(state)
STATE.columns = ['frequency']
STATE['%age'] = STATE['frequency']/STATE['frequency'].sum(axis = 0)
STATE['%age'] = STATE['%age'].round(4)
STATE['%age'] = STATE['%age']*100
#print(STATE['%age'].sum(axis = 0))
STATE.head()


# b)Sector (1= Rural , 2= Urban)

# In[15]:


sector = subset['sector'].value_counts()


# In[16]:


SECTOR = pd.DataFrame(sector)
SECTOR.columns = ['frequency']
SECTOR['%age'] = SECTOR['frequency']/SECTOR['frequency'].sum(axis = 0)
SECTOR['%age'] = SECTOR['%age'].round(4)
SECTOR['%age'] = SECTOR['%age']*100
#print(SECTOR['%age'].sum(axis = 0))
SECTOR.head()


# c) Sex

# In[63]:


sex = subset['sex'].value_counts()


# In[18]:


SEX = pd.DataFrame(sex)
SEX.columns = ['frequency']
SEX['%age'] = SEX['frequency']/SEX['frequency'].sum(axis = 0)
SEX['%age'] = SEX['%age'].round(4)
SEX['%age'] = SEX['%age']*100
#print(SEX['%age'].sum(axis = 0))
SEX.head()


# d) Workertype ie 'cwstype'

# In[19]:


cwstype = subset['cwstype'].value_counts()


# In[20]:


CWSTYPE = pd.DataFrame(cwstype)
CWSTYPE.columns = ['frequency']
CWSTYPE['%age'] = CWSTYPE['frequency']/CWSTYPE['frequency'].sum(axis = 0)
CWSTYPE['%age'] = CWSTYPE['%age'].round(4)
CWSTYPE['%age'] = CWSTYPE['%age']*100
#print(CWSTYPE['%age'].sum(axis = 0))
CWSTYPE.head()


# In[21]:


subset['cwstype'].unique()


# e) Education Category

# In[22]:


edu_cat = subset['edu_cat'].value_counts()


# In[23]:


EDU_CAT = pd.DataFrame(edu_cat)
EDU_CAT.columns = ['frequency']
EDU_CAT['%age'] = EDU_CAT['frequency']/EDU_CAT['frequency'].sum(axis = 0)
EDU_CAT['%age'] = EDU_CAT['%age'].round(4)
EDU_CAT['%age'] = EDU_CAT['%age']*100
#print(EDU_CAT['%age'].sum(axis = 0))
EDU_CAT.head()


# # Question 5
# 

# In[24]:


subset.dtypes


# Wage and log_wage are the only continuous type variables in the dataset

# # Question 6
# 
# Mentioned below are the mean, median and quartile distribution of the only continous type variable ie wage

# In[64]:


subset.wage.describe()


# # Question 7
# 
# A tabular comparison of states and their wages have been made below

# The name of each state has been displayed first along with the number of states 

# In[27]:


subset['state'].unique()


# In[28]:


subset['state'].nunique()


# Statewise comparison of wage in increasing order has been made below 

# In[29]:


state_wage = subset.groupby('state')['wage'].mean()
state_wage =  state_wage.sort_values()
state_wage = pd.DataFrame(state_wage)
print(state_wage)


# On an average, workers of Delhi have been earning the most while workers of Madhya Pradesh have been earning the least

# # Question 8

# Education level of each state has been indexed below

# In[32]:


state_educat_num = subset.groupby('state')['educat_num'].mean()
state_educat_num =  state_educat_num.sort_values()
state_educat_num = pd.DataFrame(state_educat_num)
print(state_educat_num)


# Workers of Delhi are most educated while workers of Lakshwadeep are the least educated according to the table containing state and their education level

# # Question 9

# Earnings are compared on the following basis

# a) Rural vs Urban

# In[35]:


rural_wage = subset[subset['sector'] == 1]
rural_wage = pd.DataFrame(rural_wage)
rural_wage.wage.describe()


# In[36]:


urban_wage = subset[subset['sector'] == 2]
urban_wage = pd.DataFrame(urban_wage)
urban_wage.wage.describe()


# It is observed that Mean of Urban Wage is greater than that of Rural Wage, SD of Urban Wage > Rural wage and Maximum and Minimum value of Wage for both sectors is same i.e 1 & 30,000 respectively

# b) Male vs Female
# 

# In[37]:


male_wage = subset[subset['sex'] == 'male']
male_wage = pd.DataFrame(male_wage)
male_wage.wage.describe()


# In[38]:


female_wage = subset[subset['sex'] == 'female']
female_wage = pd.DataFrame(female_wage)
female_wage.wage.describe()


# From the above table, we can see that on an average(mean), male workers earn higher than female workers. Moreover, female workers not only get low wage, but also the standard deviation is very high. Maximum earnings of male & female workers are 30k and 12k respectively. 

# 

# c)Different worker types (using ‘workertype’)

# In[39]:


self_employed_wage = subset[subset['cwstype'] == 'self employed']
self_employed_wage = pd.DataFrame(self_employed_wage)
self_employed_wage.wage.describe()


# In[40]:


regular_wage= subset[subset['cwstype'] == 'regular wage/salaried employees']
regular_wage= pd.DataFrame(regular_wage)
regular_wage.wage.describe()


# In[52]:


casual_labour_wage= subset[subset['cwstype'] == 'casual labour']
#casual_labour_wage= pd.DataFrame(casual_labour_wage)
casual_labour_wage.wage.describe()


# From the table, it is clear that regular wage workers' average salary is the highest, followed by self employed and casual labour respectively.

# 

# d)Different education categories provided in the table
# 

# In[65]:


below_middle_wage= subset[subset['edu_cat'] == 'below middle']
#below_middle_wage= pd.DataFrame(below_middle_wage)
below_middle_wage.wage.describe()


# In[66]:


Secondary_and_higher_wage= subset[subset['edu_cat'] == 'Secondary & higher']
#Secondary_and_higher_wage= pd.DataFrame(Secondary_and_higher_wage)
Secondary_and_higher_wage.wage.describe()


# In[67]:


Graduate_and_above_wage= subset[subset['edu_cat'] == 'Graduate & above']
#Graduate_and_above_wage= pd.DataFrame(Graduate_and_above_wage)
Graduate_and_above_wage.wage.describe()


# Clearly, wage paid is positively correlated to the qualification of workers. While graduate people get paid as high as 300k, below middle workers can earn a maximum of 90k only. The average salaries of graduate people is ovbiousy the highest. 

# 

# e)Three age groups

# i) 15 to 29 years

# In[60]:


age1_wage= subset[(subset['age'] >= 15) & (subset['age'] <= 29) ]
age1_wage.wage.describe()


# ii)30 to 58 years

# In[62]:


age2_wage= subset[(subset['age'] >= 30) & (subset['age'] <= 58) ]
age2_wage.wage.describe()


# iii)59 and above
# 

# In[61]:


age3_wage= subset[subset['age'] >59 ]
age3_wage.wage.describe()


# Workers in the age group 30 to 58, on an average get highest wage, and these are the maximum in number. On the other hand, people above age 59 are least in number, and their average salary is also the lowest. However, people in the group above 59 have highest maximum wage, may be due to their pensions or returns of savings.

# 

# # Question 10

# Kernel Density Plots for log_wage is made for the following

# a)Male and Female

# In[55]:


sns.kdeplot(data=subset, x="log_wage", hue="sex")


# It is a bimodal distribution where the kurtosis oflog wage male exceeds that of female

# 

# b)Urban and Rural

# In[56]:


sns.kdeplot(data=subset, x="log_wage", hue="sector")


# It is a bimodal distribution where the kurtosis of log wage of rural sector exceeds that of urban sector

# c)Urban-Male and Rural-Male
# 

# In[57]:


sns.kdeplot(data=male_wage, x="log_wage", hue="sector")


# It is a bimodal distribution where the kurtosis of log wage of rural male exceeds that of urban male

# 

# d)Urban-Female and Rural-Female

# In[58]:


sns.kdeplot(data=female_wage, x="log_wage", hue="sector")


# It is a bimodal distribution where the kurtosis of log wage of rural female is more than that of urban female

# 

# # Question 11

# Wage generally follows LOG-NORMAL DISTRIBUTION
# And
# Statistical distribution of log_wage is Normal Distribution generally

# # Question 12
# 
# Normality Test of 'log_wage'

# In[69]:


import math
from scipy.stats import lognorm
import matplotlib.pyplot as plt
np.random.seed(1)
lognorm_dataset=lognorm.rvs(s=.5,scale=math.exp(1),size=146783)
plt.hist(lognorm_dataset,edgecolor='black',bins=20)


# This is a distribution which is positively skewed and hence the distribution does not assume a normal form
