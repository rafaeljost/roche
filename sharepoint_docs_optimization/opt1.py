print "Hello World!"

import datefinder

input_string = "monkey 2010-07-10 love banana"
# a generator will be returned by the datefinder module. I'm typecasting it to a list. Please read the note of caution provided at the bottom.
matches = list(datefinder.find_dates(input_string))

if len(matches) > 0:
    # date returned will be a datetime.datetime object. here we are only using the first match.
    date = matches[0]
    print date
else:
    print 'No dates found'