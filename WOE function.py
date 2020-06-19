import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt

def information_value(df,column,target):
    #Number of bins you want to split your distribution into
    number_of_bins = 20
    
    #Initial setting of IV to 0 to be summed
    IV = 0

    #Calculation of the total number of goods and bads
    total_goods = df.loc[df[target] == 0].shape[0]
    total_bads = df.loc[df[target] == 1].shape[0]

    #Break the column up into equal parts of 5% intervals
    lower_boundary = df[column].min()
    barchart_x_boundaries.append(lower_boundary)
    
    for bin_number in range(number_of_bins):     

        #Calculation of the boundaries
        upper_boundary = np.percentile(df[column], (bin_number+1)*(100/number_of_bins))

        if upper_boundary != lower_boundary:
            #Sum of non-targets in the boundary
            non_targets = df.loc[(df[column]>= lower_boundary) & (df[column] < upper_boundary) & (df[target] == 0)].shape[0]
            non_targets_percent = (non_targets/total_goods)

            #Sum of targets in the boundary
            targets = df.loc[(df[column]>= lower_boundary) & (df[column] < upper_boundary) & (df[target] == 1)].shape[0]
            targets_percent = (targets/total_bads)

            #Calculation of WOE
            #WOE = ln(%goods/%bads)
            WOE = math.log(non_targets_percent/targets_percent)

            barchart_y_values.append(WOE)
            barchart_x_boundaries.append(upper_boundary)

            #Making the lower boundary equal to the upper boundary for the next iteration
            lower_boundary = upper_boundary
            
    return barchart_y_values,barchart_x_boundaries


folder_location = "c:\\Users\\"
df = pd.read_csv(folder_location + "", index_col = "")


barchart_y_values,barchart_x_boundaries = information_value(df=,column=,target=)
print('barchart_y_values')
print(barchart_y_values)

barchart_x_values = []
for i in range(len(barchart_y_values)):
    barchart_x_values.append(i+1)

print("")
print('barchart_x_boundaries')
print("")

for i in range(len(barchart_x_boundaries)-1):
    print("{} boundary:         lower bounary = {:2.2}                          upper boundary = {:2.2}".format(i+1,barchart_x_boundaries[i],barchart_x_boundaries[i+1]))

plt.bar(barchart_x_values, barchart_y_values)
plt.show()