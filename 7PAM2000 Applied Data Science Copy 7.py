#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing required libraries
import pandas as _pds
import matplotlib.pyplot as _matplt
from matplotlib.figure import Figure
import numpy as nmp


# In[2]:


#loading the csv file contatining data of traffic on the roads of Great Britain
data_traffic = _pds.read_csv("https://storage.googleapis.com/dft-statistics/road-traffic/downloads/data-gov-uk/region_traffic_by_road_type.csv", encoding ="latin-1")
data_traffic


# In[3]:


#checking if there are any null values
data_traffic.isnull().sum()


# In[4]:


#displaying information about the dataset
data_traffic.info()


# In[5]:


#renaming the headers of dataset for easy usage
new_names = {"ï»¿year": "Year", "Region_name": "Region Name", "road_category_name": "Road Category Name", "total_link_length_km": "Link Length in KM", "total_link_length_miles": "Link Length in Miles", "all_motor_vehicles": "Motor Vehicles"}
data_traffic.rename(columns =new_names, inplace =True )


# In[6]:


#dropping irrelevant rows and taking data of only 2021 for displaying clean charts
data_traffic.drop(data_traffic.index[0:1403], axis=0, inplace = True)
data_traffic.head(20)


# In[7]:


#converting the values inside the column which is "Motor Vehicles" into integers
data_traffic["Motor Vehicles"] = data_traffic["Motor Vehicles"].map(int)


# In[8]:


#grouping the data using 3 columns and taking the sum of all values
final_traffic_data = data_traffic.groupby(["Year", "Region Name", "Road Category Name"]).sum()
final_traffic_data


# In[12]:


"""Here a fucntion has been defined to create a line chart having multiple lines. This function takes 3 arguments. First is the dataset which has
to be fed. Second and third are the column names in format string which need to be plotted. Please note that the datatype of values in these columns
must be integers or digits. The criteria has been fixed as "Region Name". 
"""
def line_chart_plotting(frame, column1, column2):
    A = frame.groupby(['Region Name'])[column1].mean()
    B = frame.groupby(['Region Name'])[column2].mean()
    #plotting the data
    _matplt.plot(A)
    _matplt.plot(B)
    _matplt.xticks(rotation=90)
    #defining the legened, its title and its position
    _matplt.legend([column1,column2], title="Roads",  bbox_to_anchor=(1.50, 1.0))
    #defining the labels
    _matplt.xlabel("Region Name")
    _matplt.ylabel("Length of Roads")
    #giving title to thye whole chart
    _matplt.title("Length of Roads in different areas of Great Britain")
    _matplt.show()
#calling the function
line_chart_plotting(final_traffic_data,"Link Length in Miles","Link Length in KM")


# In[10]:


"""In this function, a histogram will be drawn whenever it is called. The argument it takes are color to be used and column to be plotted.
"""
def plotting_histogram(col, observation):
    #definign the size of histogram
    _matplt.figure(figsize=(20,10))
    #plotting a histogram with color col
    data_traffic[observation].hist(color = col)
    #defining the labels
    _matplt.ylabel("Total", fontsize=15)
    _matplt.xlabel(observation, fontsize=15)
    #defining the title and its fontsize
    _matplt.title("Number of records in {}".format(observation), fontsize = 18)
    #defining the legend and its fontsize
    _matplt.legend([observation], title="Different {}".format(observation), fontsize=15)
#calling the function
plotting_histogram("orange", "Region Name")


# In[11]:


"""This function will plot a pie chart whenever called.
It only takes one argument which is dataset. It plots a simple pie chart and gives legend and label to it.
"""
def plotting_pie_chart(set_):
    #creating a list of labels
    road_categories = ['TM', 'PM', 'TA', 'PA', 'M']
    ax, fig = _matplt.subplots(figsize =(5,5))
    #plotting a pie chart using mean of motor vehicles 
    _matplt.pie(set_.groupby(["Road Category Name"])["Motor Vehicles"].mean(), labels = road_categories, startangle = 90)
    #definign legend and its location
    ax.legend(road_categories, loc ="lower left")
    #giving title to the figure
    fig.set_title("Total cars based on road category", fontsize = 15)
#calling the function
plotting_pie_chart(data_traffic)

