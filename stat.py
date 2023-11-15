#statistics, pandas, numpy, scipy, math
import math
import statistics
import numpy as np
import pandas as pd
import scipy.stats

import seaborn as ozzy

ozzy.set_theme(style = "darkgrid") #you can as well use whitegrid

ozzy.set_palette('Set2')

data = pd.read_excel ("Py4Stat.xlsx") # learn how to read CSV files and others

#print (data.info()) #or use (data.info()) this displays data

#print (data.describe())

#print (data.head)   #gives all the values this a property thus it least everything
#print (data.head())  #gives less raws about the data


#print(data[])
# cleaning our data
clean_data = data[['Bio','Che']] = data[['Bio','Che']].apply(lambda x:x.str.split(' ').str[1]) #this tahes the second column

#clean_data = data[['Bio' , 'Che' , 'Phy' , 'Mat' , 'Geo' , 'His' , 'Eng' , 'Adm' , 'Agric' , 'Ara' , 'Cre' , 'Com' , 'Cs' , 'Art']]=data[['Bio' , 'Che' , 'Phy' , 'Mat' , 'Geo' , 'His' , 'Eng' , 'Adm' , 'Agric' , 'Ara' , 'Cre' , 'Com' , 'Cs' , 'Art']].apply(lambda x:x.str.split(' ').str[1])


#print(clean_data.info())
#cleaned data will be stored in variable clean_data 

# data[['Bio','Che']] this is where our new cleaned data will be
#the command is applied on this data[['Bio','Che']] unclean data
# if you want to subset data column by column use [[]]
#lambda takes the range ie x:x (0:42) 


#lambda helps you to eliminate computation errors
# x: talks about range

#clean_data = data[['Bio','Che']] = data[['Bio','Che']].apply(lambda x:x.str.split(' ').str[0])  #this tahes the first column
#print (clean_data)
#print (clean_data.describe)


#3rd november 2023
# we need to do data conversion 

converted_data = clean_data.astype("int")  #line for converting into integer

#finding mean using np
mean_np = np.mean(converted_data)

#print(mean_np)    #so nice thanks ozzy

#using pandas

#print(converted_data.mean()) #whole data
#print(converted_data['Che'].mean())  #for che alone

#print(converted_data.info())

# finding out how data is distributed

#MEAN OR Average

mean_ = statistics.mean(converted_data['Bio'])

#print(mean_)

#4th NOV 2023
#getting mean value, what does it imply

#Getting the mean and maximum values

#print(converted_data.agg(['min', 'max']))

#read about geometric mean and weighted mean

#intresting, lets look at the median

median_ = statistics.median(converted_data['Bio']) #that when your using ascending order
median2_ = statistics.median(converted_data['Bio'][:-1]) #when we arrange data in descending oder

#x = [1,2.5,4,8.0,28.0]


#print(median_)
#print(median2_)

median_low_ = statistics.median_low(converted_data['Bio'][:-1])

#print(median_low_)

median_High_ = statistics.median_high(converted_data['Bio'][:-1])

#print(median_High_)

#ploting data

ozzy.boxplot(converted_data)


#10th November 2023
# How do we find the mode?

#for a single mode
mode_ = statistics.mode(converted_data['Che'])

#print(mode_) #if two number appears to share the mode, this gives youthe error

#to get multiple mode in a given dataset
mode2_ = statistics.multimode(converted_data['Che'])


#print(mode2_)

#lets see what scipy can do

mode3_ = scipy.stats.mode(converted_data['Bio'])

#print(mode3_.mode) #for only mode

#print(mode3_.count) #for the number of times

#lets see what pandas does....

#you can find mode for every column in a dataset
mode4_ = converted_data.mode() 

#print(mode4_)

#THIS MARKS THE END OF CENTRAL TENDENCY 

#IN viability we are looking on how data is spread 

#starting with variance

#variance is the pread of data points away from the average
#sometimes called the sample variance

var_ = statistics.variance(converted_data['Che'])

#print(var_ , mean_np )
# give this data meaning, how do you term the output?????????

standard_dev = math.sqrt(var_) #getting the standard deviation

#print(standard_dev) 

#using pandas to print the mean
var2_ = converted_data.var()

#print(var2_)

#using nampy

var3_ = np.var(converted_data, ddof=1) #ddof means delta degree of freedom
                                        #assignment what does DDOF MEAN here
                                        
#print(var3_)  #it will be related to what your doing 
                # for this example its marks away from the mean

var4_ = converted_data.var()

#print("the variance is :" , var4_)

#saturday 11th november 2023

#standard deviation or sample SD and connect to sample var

#its the postive sqrt of the postive variance

standard_dev = (var4_)**0.5 #using pure python

#print("The stardard deviation is :", standard_dev)

#looking at other libraries

standard_dev2 = statistics.stdev(converted_data['Che'])

#print("The stardard deviation is :", standard_dev2)

standard_dev3 = statistics.stdev(converted_data['Bio'])

#print("The stardard deviation is :", standard_dev3)

#using nampy 

standard_dev4 = np.std(converted_data, ddof = 1)

#print("The stardard deviation is :", standard_dev4)

standard_dev5 = converted_data.std(ddof = 1)

#print("The stardard deviation is :", standard_dev5)

#using pandas library

standard_dev6 = converted_data.std(ddof = 1) # follows the same way as nampy
#print("The stardard deviation is :", standard_dev6)

#LOOKING AT SKEWNESS or SAMPLE SKEWNESS

#MEASURE OFthe  asymmetry of a data sample
#getting negative skewness it means dominant tail on the left

#getting postive skewness it means dominant tail on the right
#if the skewness is close to zero, we consider data to be quite symmetrical

#if your values between -0.5 to 0.5 its symmetrical data
#the best library for this is scipy

skew1_ = scipy.stats.skew(converted_data['Che'], bias = False)

#print("The skew for Che is :", skew1_)

skew2_ = scipy.stats.skew(converted_data['Bio'], bias = False)

#print("The skew for Bio is :", skew2_)
#both data above is symmetrical

#using pandas

skew3_ = converted_data.skew()
print("The skew for  is :", skew3_)

#LOOKING AT THE RANGE































