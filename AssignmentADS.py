# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 02:54:05 2022

@author: user
"""
#importing modules
import pandas as pd
import matplotlib.pyplot as plt

#Read file into data frame and printing data frame
data = pd.read_csv("PopulationGrowth.csv")
print(data)

#Function for plotting Line plot
def lineFunction():
    
   """"Plotting four countries with labels"""
   plt.figure()
   plt.plot(data["Country Name"],data["1970"],label="1970")
   plt.plot(data["Country Name"],data["1980"],label="1980")
   plt.plot(data["Country Name"],data["1990"],label="1990")
   plt.plot(data["Country Name"],data["2000"],label="2000")
   
   #Setting labels and showing the legends
   plt.xlabel("Country")
   plt.ylabel("Population Growth")
   plt.legend()
   plt.savefig("LinePlot.png")#Saving the line plot
   plt.show()
lineFunction() #Calling the defined function for Line Plot

#Function for plotting Bar Graph
def barFunction():
    
    """Plotting two countries with labels"""
    plt.figure()
    plt.bar(data["Country Name"],data["1970"],label="1970",alpha=0.4,
            color="red")
    plt.bar(data["Country Name"],data["2000"],label="2000",alpha=0.4,
            color="blue")
    
    #Setting labels and showing the legends
    plt.xlabel("Country")
    plt.ylabel("Population Growth")
    plt.savefig("BarChart.png")#Saving bar graph
    plt.legend()
    plt.show()
barFunction() # Calling the defined function for Bar Plot


#Function for plotting Pie Chart
def pieChart():
    
    """Plotting pie chart for the year 1962"""
    plt.pie(data["1962"],autopct='%1.1f%%',startangle=120)
    plt.legend(bbox_to_anchor = (1,1),labels=data["Country Name"])
    plt.savefig("PieChart.png")
    plt.show()
pieChart()#Calling defined function for Pie Chart