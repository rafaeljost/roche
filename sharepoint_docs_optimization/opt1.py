#Program Title
print ("Opt1!")

#necessary imports
import datefinder
    

#Module 1: filter date out of a string

input_string = "monkey 2010-07-10 love banana"

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

filter_date(input_string)



