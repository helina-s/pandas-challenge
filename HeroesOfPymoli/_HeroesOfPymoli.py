#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import pandas as pd

#load file
pymoli_data = os.path.join(r"/Users/Munit/Desktop/pandas-HW/pandas-challenge/Resources/purchase_data.csv")


# In[2]:


#read file & store in pandas data frame
pymoli_df=pd.read_csv(pymoli_data)
pymoli_df.head()


# In[5]:


players= len(pymoli_df["SN"].value_counts())
players

total_players=[players]
total_players_df = pd.DataFrame(total_players, columns= ["Total Players"])
total_players_df

unique_items = pymoli_df["Item ID"].nunique()
unique_items

average_price = pymoli_df["Price"].mean()
average_price

total_purchase = len(pymoli_df["Purchase ID"].value_counts())
total_purchase

total_revenue=pymoli_df["Price"].sum()
total_revenue

#Purchasing Analysis Table
purchase_analysis_df = pd.DataFrame([{"Number of Unique Items": unique_items, "Average Price": average_price,"Number of Purchases": total_purchase, "Total Revenue": total_revenue}])
purchase_analysis_df["Average Price"] = purchase_analysis_df["Average Price"].map("${:,.2f}".format)
purchase_analysis_df["Total Revenue"] = purchase_analysis_df["Total Revenue"].map("${:,.2f}".format)
purchase_analysis_df


# In[6]:


#gender demographics
pymoli_2_df = pymoli_df.drop_duplicates(subset="SN")
gender_demo_df = pd.DataFrame(pymoli_2_df["Gender"].value_counts())
gender_demo_df

percent_of_players = (pymoli_df["Gender"].value_counts()/pymoli_df["Gender"].count())*100
percent_of_players

gender_demo_df["Percentage of Players"] = percent_of_players
gender_demo_df["Percentage of Players"] = gender_demo_df["Percentage of Players"].map("{:,.2f}%".format)
gender_demo_df

#rename column
renamed_df = gender_demo_df.rename(columns={"Gender": "Total Count"})
renamed_df


# In[8]:


#purchasing analyisis by gender
gender_grouped_pymoli_df = pymoli_df.groupby(["Gender"])
gender_grouped_pymoli_df
gender_grouped_pymoli_df["Purchase ID"].count()

total_purchase = gender_grouped_pymoli_df["Price"].sum()
total_purchase.astype

average_purchase = gender_grouped_pymoli_df["Price"].mean()
average_purchase

avg_total_per_person = total_purchase/gender_grouped_pymoli_df["Purchase ID"].count()

#gender_grouped_pymoli_df["Purchase ID"].count()
avg_total_per_person #?????

#purchasing analysis by gender (summary table)
summary_gender_data_df = pd.DataFrame(gender_grouped_pymoli_df["Purchase ID"].count())
summary_gender_data_df["Average Purchase Price"] = average_purchase 
summary_gender_data_df["Average Purchase Price"] = summary_gender_data_df["Average Purchase Price"].map("${:,.2f}".format)
summary_gender_data_df["Total Purchase Value"] = total_purchase 
summary_gender_data_df["Total Purchase Value"] = summary_gender_data_df["Total Purchase Value"].map("${:,.2f}".format)
summary_gender_data_df["Avg Total Purchase per Person"] = avg_total_per_person 
summary_gender_data_df["Avg Total Purchase per Person"] = summary_gender_data_df["Avg Total Purchase per Person"].map("${:,.2f}".format)
summary_gender_data_df


# In[9]:


#age demographics
age_bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 9999]
#create the names for the four bins
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

age_grouped_pymoli_df = pymoli_df
age_grouped_pymoli_df["Age Group"] = pd.cut(age_grouped_pymoli_df["Age"], age_bins, labels=group_names)
age_grouped_pymoli_df

age_grouped_pymoli_df = age_grouped_pymoli_df.groupby("Age Group")

total_count_age = age_grouped_pymoli_df["SN"].nunique()
total_count_age

percent_by_age = (total_count_age/players)*100
percent_by_age = percent_by_age.map("{:,.2f}%".format)
percent_by_age

#save new dataframe in a new variable
age_summary_df = pd.DataFrame(age_grouped_pymoli_df.nunique())
age_summary_df

summary_age_table = pd.DataFrame({"Total Count": total_count_age, "Percentage of Players": percent_by_age})
summary_age_table


# In[10]:


#purchasing analysis by age
age_analysis_df = pd.DataFrame(age_grouped_pymoli_df["Purchase ID"].count())
age_analysis_df

avg_price_age = age_grouped_pymoli_df["Price"].mean()
avg_price_age

total_purchase_age = age_grouped_pymoli_df["Price"].sum()
total_purchase_age

avg_total_per_person_age = (total_purchase_age)/(age_grouped_pymoli_df["Purchase ID"].count())
avg_total_per_person_age

age_analysis_df["Average Purchase Price"] = avg_price_age
age_analysis_df["Average Purchase Price"] = age_analysis_df["Average Purchase Price"].map("${:,.2f}".format)
age_analysis_df["Total Purchase Value"] = total_purchase_age
age_analysis_df["Total Purchase Value"] = age_analysis_df["Total Purchase Value"].map("${:,.2f}".format)
age_analysis_df["Avg Purchase Total Per Person"] = avg_total_per_person_age
age_analysis_df["Avg Purchase Total Per Person"] = age_analysis_df["Avg Purchase Total Per Person"].map("${:,.2f}".format)
age_analysis_df

#rename first column under another variable
age_analysis_summary_df = age_analysis_df.rename(columns={"Purchase ID": "Purcase Count"})
age_analysis_summary_df


# In[11]:


#use original data to find the top spendors
top_spendors_orig_df = pd.DataFrame(pymoli_df)
top_spendors_orig_df.head()

#top spenders: group original data by SN
top_spendors_SN_df = pymoli_df.groupby("SN")
top_spendors_SN_df.count()

top_spendors_df = pd.DataFrame(top_spendors_SN_df["Purchase ID"].count())
top_spendors_df

total_purchase_SN = top_spendors_SN_df["Price"].sum()
total_purchase_SN

avg_purchase_SN = top_spendors_SN_df["Price"].mean()
avg_purchase_SN = avg_purchase_SN.map("${:,.2f}".format)
avg_purchase_SN

#summary table
top_spendors_df["Average Purchase Price"] = avg_purchase_SN
top_spendors_df["Total Purchase Value"] = total_purchase_SN
top_spendors_df

#rename columns of summary table
top_spendors_summary_df = top_spendors_df.rename(columns= {"Purchase ID":"Purchase Count"})
top5_spendors_df = top_spendors_summary_df.sort_values("Total Purchase Value", ascending=False)
top5_spendors_df.head()
#add $ to the Total Purchase Value
top5_spendors_df["Total Purchase Value"] = total_purchase_SN.map("${:,.2f}".format)
top5_spendors_df.head()


# In[12]:


#most popular items: group by Item & Item Name
popular_item_orig_df = pd.DataFrame(pymoli_df)
popular_item_orig_df.head()
popular_item_grp_df = pymoli_df.groupby(["Item ID" , "Item Name"])
popular_item_grp_df

popular_item_df = pd.DataFrame(popular_item_grp_df["Purchase ID"].count())
popular_item_df

item_price = popular_item_grp_df["Price"].mean()
item_price = item_price.map("${:,.2f}".format)
item_price

total_purchase_item = popular_item_grp_df["Price"].sum()
total_purchase_item

#assign columns for summary table
popular_item_df["Item Price"] = item_price
popular_item_df["Total Purchase Value"] = total_purchase_item
popular_item_df

popular_item_summary_df = popular_item_df.rename (columns= {"Purchase ID": "Purchase Count"})
popular_item_summary_df

#sort and format total purchase count
popular_5_items_df = popular_item_summary_df.sort_values("Purchase Count", ascending=False)
popular_5_items_df.head()
popular_5_items_df["Total Purchase Value"] = total_purchase_item.map("${:,.2f}".format)
popular_5_items_df.head()


# In[13]:


#most profitable items
profitable_items_df = popular_item_summary_df.sort_values("Total Purchase Value", ascending=False)
profitable_items_df.head()
profitable_items_df["Total Purchase Value"] = total_purchase_item.map("${:,.2f}".format)
profitable_items_df.head()


# In[ ]:




