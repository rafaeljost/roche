import os

delimiters = "-", "_"
string = "AOC15P_PMR Notice_2017-02_1.pdf"

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)


splitted_string = split(delimiters, string)

joined_string = '/'.join(splitted_string)

print (joined_string)    

#Program Title
print ("Opt1!")

#necessary imports
import datefinder
    

#Module 1: filter date out of a string


def filter_date(string):    
   
    # a generator will be returned by the datefinder module. I'm typecasting it to a list. Please read the note of caution provided at the bottom.
    matches = list(datefinder.find_dates(string))

    if len(matches) > 0:
        # date returned will be a datetime.datetime object. here we are only using the first match.
        date = matches[0]
        print (date)
    else:
        print ('No dates found')
        
    return

filter_date(joined_string)

