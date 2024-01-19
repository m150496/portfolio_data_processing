# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:43:13 2020

@author: Milan
"""
# Milan Cukovic
# 01531871

# a) 


    
    
filename = 'WetterDaten2018.csv'
    
def read_data(filename,columns=['T3','RH3']): # titles insterted in the input list columns
    
    import numpy as np
    from datetime import datetime
    
    filename = open(filename,'r') # open file
    
    lines = filename.readlines() #read all the lines including header

    new_list = [] # The list of all the data we need
    
    header = lines[0].split(';') # separating the titles from each other, ; is the border
    relevant_columns = [0] # The list with numbers as indices of the titles' columns.
    # timestamp column should always be taken into account, that's why 0 is automatically inserted
    for i in range(len(columns)): # counting elements in the columns list
        
        for k in range(len(header)): # counting titles indices in the table
            
            if columns[i]==header[k]: # if the input element in the columns is equal to the title in the table,
                
                relevant_columns.append(k) # indices of the table column with that title is added to the 
                # relevant_columns.
    # This for-loop allows the function to analyze not only data from 'T3' and 'RH3' columns,
    # but also any other column the user wants
                
    
    categories = lines[1].split(';') # Splitting first measurements from each other
    t0 = datetime.fromisoformat(categories[0]) # First time measured is t0
    # datetime.fromisoformat converts the string into datetime format
    
    for k in range(1,len(lines)): # counting each line

        categories = lines[k].split(';') # splitting columns and ; is the separator
        t1 = datetime.fromisoformat(categories[0]) # puting corresponding time in datetime format
        categories[0] = str((t1 - t0).total_seconds()/3600) # All the time measured is relative to the time t0
        # That's why t1-t0 and since the task is to express it in hours 
        # and I couldn't find the hours option I converted it into seconds 
        # and divided it by 3600 as there are 3600 seconds in one hour.
        
        new_line = [] # The new list of the converted float/int elements from each row of the original table
        
        for j in relevant_columns: # counting the elements of the columns we need
            
            if categories[j] != '---': # if the symbol is not ---
                
                new_line.append(eval(categories[j])) # the element is converted into float/int with eval
                # and added to ne_line
                
            else: # if the symbol is ---
                
                new_line.append(np.NaN) # it is substituted with nan and added to  new_line
            
        new_list.append(new_line) # new_line is added to new_list and the procedure is repeated with next row
        
    return np.array(new_list) # when all loops are finished new_list has become the nested list which is converted into array
# Reason: in numpy arrays more mathematical operations are possible, than in lists

T3_HR3_data = read_data(filename,columns=['T3','RH3'])

#b)
        
def annual_average(filename,columns=['T3','RH3']):
    
    import numpy as np
    from datetime import datetime
    
    filename = open(filename,'r')
    
    lines = filename.readlines()

    new_list = []
    
    header = lines[0].split(';')
    relevant_columns = []
    
    for i in range(len(columns)):
        
        for k in range(len(header)):
            
            if columns[i]==header[k]:
                
                relevant_columns.append(k)
                
    
    categories = lines[1].split(';')
    t0 = datetime.fromisoformat(categories[0])  
    
    for k in range(1,len(lines)):

        categories = lines[k].split(';')
        t1 = datetime.fromisoformat(categories[0])
        categories[0] = str((t1 - t0).total_seconds()/3600)
        
        new_line = []
        
        for j in relevant_columns: 
            
            if categories[j] != '---':
                
                new_line.append(eval(categories[j])) 
                
            else:
                
                new_line.append(np.NaN) 
            
        new_list.append(new_line) 
        
    Array = np.array(new_list)
################################### Until this point, absolutely the same code as in the previous function#####################   
########## The only difference is that index of the timestamp column (0) is not included, because time is not needed in this function
    
    means = np.zeros((len(relevant_columns))) # one dimensional array skeleton of future means
    
    for j in range(len(relevant_columns)): # counting all columns needed
        
        means[j] = np.nanmean(Array[:,j]) # calculating an average of each column and inserting it into means
        # That's why we need numpy library, to calculate mean of all elements.
        # nans are not included into mean calculation. This is the difference between np.mean and np.nanmean, as np.mean sends
        # an error if some nans are included
        
    return means

anual_average_T3_HR3 = annual_average(filename,columns=['T3','RH3'])

# b)
def monthly_average(filename,columns=['T3','RH3']):
    
    import numpy as np
    from datetime import datetime
    
    filename = open(filename,'r')
    
    lines = filename.readlines()
    
    header = lines[0].split(';')
    relevant_columns = []
    
    for i in range(len(columns)):
        
        for k in range(len(header)):
            
            if columns[i]==header[k]:
                
                relevant_columns.append(k)
####################################### same code as in previous functions until this point#########################                  
    months= [] # future nested list of data for each month
    for i in range(12): # There are 12 months in total 
        
        months.append([]) # one list for each month
    for k in range(1,len(lines)): # counting each line, header is avoided

        categories = lines[k].split(';') # splitting into columns, ; is the border
        Date = datetime.strptime(categories[0], "%Y-%m-%d %H:%M:%S") # converting into datetime format
        categories[0] = str(Date.month) # extracting the month from the Date
        
        for j,i in zip(range(1,13),range(len(months))): # counting from 1 to 12
            # as well as counting the list in months list
            # The reason why two indices are included, because python counts
            # from 0 when it comes to nested list and 0th month does not exist
            
            if categories[0]==str(j): # if the month number in the table is equal to
                # the month number
                
                months[i].append(categories) # categories list is added to the ith list (jth month) in the nested list
    # When the loop is done (when all lines in the table are appended to the corresponding lists ), elimination of 
    # '---' and empty rows ('\n') starts.
    for i in range(len(months)): # selecting "month" indices
        for k in range(len(months[i])): # selecting the "sample in a month" indices
            for j in range(len(months[i][k])): # selecting "measurement in the sample" indices
                
                if months[i][k][j] != '---' and months[i][k][j] != '\n':
                    
                    months[i][k][j]= eval(months[i][k][j]) # converting everything what doesn't belong to '---' and empty lists into float/int
                    
                else: # if it is the case
                    
                    months[i][k][j]=np.NaN # give it nan
    

    array_months = []              
    for i in range(len(months)):
        
        
        array_months.append(np.array(months[i])) # putting into array each month data
            
    means = np.zeros((12,len(columns))) # skeleton for all mean values in each month
    
    for i in range(len(months)):
        for j in range(len(columns)):
            # calculating the mean (which doesn't involve nans) of all data in each month in each column
            means[i][j] = np.nanmean(array_months[i][:,relevant_columns[j]]) # relevant_columns[j] is the indices of the input title in the table
    

    return means

# c)

import matplotlib.pyplot as plt

mittelwert = monthly_average(filename,columns=['Timestamp','T3','RH3']) # activating the function monthly_average
t_month = mittelwert[:,0] # months of the measurement sample
avg_T3 = mittelwert[:,1] # average of each month sample in category T3
avg_RH3 = mittelwert[:,2] # average of each month sample in category RH3
plt.plot(t_month, avg_T3, 'r.', t_month, avg_RH3, 'b.') # actual plotting
label = ['Mittelwert der Lufttemperatur (T3)','Mittelwert der Luftfeuchtigkeit (RH3)',] # labeling each curve in the legend
plt.xlabel('Monat') # x axis description
plt.ylabel('Monatsmittelwert') # y axis description
plt.title('Der Monatsmittelwert von jedem Monat') # title
plt.legend(label,shadow='true',fontsize=12) # actual legend