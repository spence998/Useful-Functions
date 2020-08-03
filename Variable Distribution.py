import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def variable_distribution(df,column,target,bins,quantile):
	x_1 = df.loc[df[target] == 1,column]
	x_0 = df.loc[df[target] == 0,column]

	#Filtering out missing values
	x_1 = [x for x in x_1 if str(x) != 'nan']
	x_0 = [x for x in x_0 if str(x) != 'nan']

	#Calculating the values in the 
	x_1_max_value = np.quantile(x_1,1-quantile)
	x_1_min_value = np.quantile(x_1,quantile)
	x_0_max_value = np.quantile(x_0,1-quantile)
	x_0_min_value = np.quantile(x_0,quantile)

	plt.figure(figsize=[10,9])
	plt.hist(x_1,bins=30,range=(x_1_min_value,x_1_max_value),label=str(target + ' = 1'),normed=1,color='blue',alpha=0.5)
	plt.hist(x_0,bins=30,range=(x_0_min_value,x_0_max_value),label=str(target + ' = 0'),normed=1,color='red',alpha=0.5)
	plt.suptitle(column)
	plt.ylabel('Normalised frequency')
	plt.xlabel('values')
	plt.legend(loc='upper right')
	plt.show()


df = pd.read_csv('train.csv')
variable_distribution	(df=df
						,column='Fare'
						,target='Survived'
						,bins=10
						,quantile=0.01 #What ratio of the distribution you want to remove 
									  #eg. 5 removes the top and bottom 5%
						)
