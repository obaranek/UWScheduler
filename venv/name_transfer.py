def name_transfer(name_uwflow):
    name = name_uwflow.split('_')
    last_name = name[len(name) - 1]
    last_name = last_name.capitalize()
    first_name = name[0]
    first_name = first_name.capitalize()
    first_name_lst = list(first_name)
    first_name_initial = first_name_lst[0]
    name_rmp = last_name + ', ' + first_name_initial
    return name_rmp

print(name_transfer("timothy_brecht"))