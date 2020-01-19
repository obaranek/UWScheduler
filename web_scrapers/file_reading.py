def return_prof_rating(file, prof_name):
    x = open(file, 'r')
    return_rating = ""
    found = False
    line = x.readline()
    while len(line) != 0 and not found:
        if line[:line.find(',')+4] == prof_name:
            found = True
            return_rating = line[-4: ]
        line = x.readline()
    x.close()
    if return_rating == "":
        return "Name not Found"
    else:
        return return_rating


#print(return_prof_rating("ProfRatingFile", "Aziz,Han"))




