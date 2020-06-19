def information_value(df,column,target):

    #Number of bins you want to split your distribution into
    number_of_bins = 5

    #Initial setting of IV to 0 to be summed
    IV = 0

    #IV multiplier is for when multiple bins are joined together because the upper boundary = lower boundary
    #We need to account for these equal bins missed out by adding in their IV to the total
    IV_multiplier = 1

    #Calculation of the total number of goods and bads
    total_goods = df.loc[df[target] == 0].shape[0]
    total_bads = df.loc[df[target] == 1].shape[0]

    #Break the column up into equal parts of 5% intervals
    lower_boundary = df[column].min()
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

            #Sum of IV
            #IV = sum of[(%non_target - %target)*WOE]
            IV = IV + (non_targets_percent-targets_percent)*WOE*IV_multiplier

            #Making the lower boundary equal to the upper boundary for the next iteration
            lower_boundary = upper_boundary
            IV_multiplier = 1          

        else:

            IV_multiplier = IV_multiplier + 1

    return IV