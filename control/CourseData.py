from web_scrapers import file_reading
from name_edit import *
from web_scrapers.UWFlowScraper import *

course_list1 = ["math136", "cs135", "math138", "clas104", "stat230"]


def get_data(course_list1):

    list_of_courses = []  # contains lists of lists of sections

    for course in course_list1:
        course_data = get_info_objects(course)
        #print(course_data)
        #print(len(course_data))

        list_of_sections = []

        for section in course_data:
            prof_name = section.get_prof_name()
            formatted_name = name_transfer(str(prof_name))
            rating = file_reading.return_prof_rating("ProfRatingFile", formatted_name)
            section.set_prof_rating(rating)
            #my_tuple = tuple + (rating, )
            list_of_sections.append(section)

        list_of_courses.append(list_of_sections)

    return list_of_courses

#print(len(get_data(course_list1)))