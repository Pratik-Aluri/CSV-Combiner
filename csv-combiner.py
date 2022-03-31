import os
import sys
import pandas as pd
import unittest

    
def get_name(path):
    #inbuilt function to get name of the file
    filename = os.path.basename(path)
    return filename

def csv_comb(df1, csv_files):
    i=1
    while i<len(csv_files):
        df2 = pd.read_csv(csv_files[i])
        #adding in filename to csv file
        df2['filename'] = get_name(csv_files[i])
        df1 = pd.concat([df1,df2])
        i+=1
    return df1

def main():
    csv_files = []
    print(sys.argv)
    i=1
    #looping through command line arguments
    while i<len(sys.argv):
        if os.path.isfile(sys.argv[i]):
            #checking if valid path and file and then appending.
            if sys.argv[i].endswith('.csv'):
                csv_files.append(sys.argv[i])
                print(sys.argv[i])
        i+=1

    #base for combining other csv files
    df = pd.read_csv(csv_files[0])
    df['filename'] = get_name(csv_files[0])

    #Calling csv_comb if there are more files
    if len(csv_files) > 1:
        df = csv_comb(df, csv_files)
    #Set index to email_hash
    df = df.set_index(df.columns[0])

    #Convert dataframe to 'combined.csv' into the same directory
    new_csv = df.to_csv()
    print(new_csv)

if __name__ == "__main__":
    main()