#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]


# In[4]:


# Calculation profit (revenue - expenses)
profit = list([])

for i in range (0, len(revenue)):
    profit.append(revenue[i]-expenses[i])
profit


# In[6]:


#Calculating tax (profit x 30%)
tax = [round(i*0.3,2) for i in profit]
tax


# In[8]:


# profit after tax
profit_aft_tax = list([])

for i in range(0,len(profit)):
    profit_aft_tax.append(profit[i] - tax[i])
profit_aft_tax


# In[11]:


# profit margin aftr tax
profit_margin = list([])

for i in range(0,len(profit)):
        profit_margin.append(profit_aft_tax[i]/revenue[i])
profit_margin = [round((i*100),2)for i in profit_margin]
profit_margin


# In[12]:


#profit margin after tax
profit_margin = list([])

for i in range(0,len(profit)):
        profit_margin.append(profit_aft_tax[i]/revenue[i])
    
profit_margin = [round((i*100),2) for i in profit_margin]
profit_margin


# In[13]:


#profit After tax mean
mean_pat = sum(profit_aft_tax) / len(profit_aft_tax)
mean_pat


# In[14]:


good_months = list([])
for i in range(0,len(profit)):
    good_months.append(profit_aft_tax[i]>mean_pat)
good_months


# In[15]:


bad_months = list([])
for i in range(0,len(profit)):
    bad_months.append(profit_aft_tax[i]<mean_pat)
bad_months


# In[19]:


best_month=list([])
for i in range(0,len(profit)):
    best_month.append(profit_aft_tax[i]==max(profit_aft_tax))
best_month


# In[20]:


worst_month=list([])
for i in range(0,len(profit)):
    worst_month.append(profit_aft_tax[i]==min(profit_aft_tax))
worst_month


# In[21]:


#convert all calculations to units of one thousand dollars
revenue_1000=[round(i/1000,2)for i in revenue]
expenses_1000=[round(i/1000,2)for i in expenses]
profit_1000=[round(i/1000,2)for i in profit]
profit_aft_tax_1000=[round(i/1000,2)for i in profit_aft_tax]

revenue_1000=[round(i/1000,2)for i in revenue_1000]
expenses_1000=[round(i/1000,2)for i in expenses_1000]
profit_1000=[round(i/1000,2)for i in profit_1000]
profit_aft_tax_1000=[round(i/1000,2)for i in profit_aft_tax_1000]


# In[26]:


#print results
print("Revenue :")
print(revenue_1000)
print("Expenses :")
print(expenses_1000)
print("Profit :")
print(profit_1000)
print("Profit after tax :")
print(profit_aft_tax_1000)

print("Good months :")
print(good_months)
print("Bad months :")
print(bad_months)
print("Best months :")
print(best_month)
print("Worst months :")
print(worst_month)


# In[ ]:




