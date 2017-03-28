#!/usr/bin/env python3
import sys
import re
import argparse
from urllib.request import urlopen


def help():
    """
    Help function to tell the user what to do
    """
    print("Usage is: ./hw6 <file input>")

def findErrors():
    """
    This function finds the top 25 errors
    """
    #Compile the regex  
    m = re.compile(r".*/.*")

    #Create an array
    store_error_data = []

    #Create the dictionary
    error_dict = {}

    #Get file
    url =  "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"
   
   #Find the errors and put them in the dictionary
    with urlopen(url) as errors:
        for find_error in errors:
            store_error_data.append(find_error.decode("utf-8"))
        
        #Match the errors
        for lines in store_error_data:
            line_errors = lines.split()
            for words in line_errors:
                match_line = m.match(words)
                if match_line:
                    
                    #If there is a match increment the count
                    if match_line.group() in error_dict:
                        error_dict[match_line.group()] += 1
                    else:
                        error_dict[match_line.group()] = 1
                    break   
        
        #Print the errors
        print("***** Top 25 errors *****")
        sorted_error_dict = sorted(error_dict, key=error_dict.get, reverse=True) 
        for i in sorted_error_dict:
            print(error_dict[i], i)

def main():
    """
    Call help Function
    """
    
    #Call the findErrors function
    findErrors()
    

if __name__=="__main__":
   
    #Parse the arguments if there is any
    parser = argparse.ArgumentParser()
    parser.add_argument("ArgumentName", help="Help")
    args = parser.parse_args()

    if args.ArgumentName != "":
        #Call main
        main()
    elif args.ArgumentName == "":
        print("")
    exit(0)
