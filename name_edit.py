'''
    This function takes in a name from the UWFlow webscrape and formats it for rateMyProf scraper
'''

def name_transfer(name_uwflow):
    name = name_uwflow.split('_')
    last_name = name[-1].capitalize() # gets the last element of the split
    #last_name = last_name
    first_name = name[0]
    first_name = first_name.capitalize()
    if last_name[1] == "'":
        last_name = last_name[0:2] + last_name[2].upper() + last_name[3:]
    #first_name_lst = list(first_name)
    first_name_initial = first_name[0:3]
    name_rmp = last_name + ',' + first_name_initial

    return name_rmp

#print(name_transfer('timothy_brecht'))