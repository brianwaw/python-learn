# to check whether a location is already added in the list, we use the 'in'
locations=['nairobi', 'nakuru', 'Njoro', 'kitengela']
location='nakur'
if location not in locations:
    print(f"that location is not in the database {location.title()}")
