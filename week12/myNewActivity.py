#%%
'''
Inputting missing values
1. Calculate and report the total number of missing values in the 
    dataset (i.e. the total number of rows with NAs)
2. Devise a strategy for filling in all of the missing values in the dataset
3. Create a new dataset that is equal to the original dataset but with 
    the missing data filled in.
4. Make a histogram of the total number of steps taken each day and 
    Calculate and report the mean and median total number of steps taken per day.
'''
#%%
import csv

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    
    wr = open("newActivity.csv","w")
    wr.write(str(header[0])+","+str(header[1])+","+str(header[2]))
    wr.write("\n")
    
    n=0
    for row in reader:
        if(row[0]=='NA'):
            row[0] = 0
            n+=1
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2]))
        wr.write("\n")
    wr.close()
    
    print("The total number of missing values in the dataset is ",n)
    print("New dataset created")

    #plot the histogram
#%%