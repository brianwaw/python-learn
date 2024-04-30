def get_formatted_name(first_name,last_name,middle_name=''):
    full_name=f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician=get_formatted_name('brian','waweru')
print(musician)

#in the above example there is a value that is being returned. a variable has to be defined that
#will allow the returned value to be stored.

#we can add a middle name in a way that if one doesn't have one he/she can avoid it by using the
#knowledge on default argument value
#def get_formatted_name(first_name,last_name,middle_name='')