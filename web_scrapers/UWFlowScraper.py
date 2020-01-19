from datetime import datetime, timedelta

import re
import json
import requests

from model.Section import Section

# Takes in a course code and returns a list of Section objects in a list with all the info for the course

def get_info_objects(course):
    section_object_list = []

    url = 'https://uwflow.com/course/' + course
    txt = requests.get(url).text
    data = json.loads(re.findall(r'window.pageData.courseObj = (\{.*?});', txt)[0])

    #print(json.dumps(data, indent=4))  # <-- uncomment this to see all data

    for section in data['sections']:
        dayList = []
        timeList = []
        roomList = []


        if section['section_type'] == 'LEC' and \
                section['campus'] != 'ONLNR ONLINE' and section['enrollment_total'] < section['enrollment_capacity'] and \
                not (section['meetings'][0]['start_seconds'] is None) \
                and not (section['meetings'][0]['prof_id'] is None):

            professor = return_prof_name(section['meetings'][0]['prof_id'])
            class_id = section['class_num']

            if len(section['meetings']) == 1:
                section_number = section['section_num']
                days = section['meetings'][0]['days']
                time = return_class_time(section['meetings'][0]['start_seconds'], section['meetings'][0]['end_seconds'])
                room = str(section['meetings'][0]['building']) + " " + str(section['meetings'][0]['room'])
                length = len(days)
                for i in range(length):
                    timeList.append(time)
                    roomList.append(room)

                formatted_time = format_time_optimisation(days, timeList)
                courseID = section['course_id']
                temp_section = Section(section_number, formatted_time, professor, 0,
                                                   class_id, room, courseID) #initially sets the prof rating to 0, this is changed later
                section_object_list.append(temp_section)


            else:
                for meeting in section['meetings']:
                    section_number = section['section_num']
                    day = meeting['days'][0]
                    time = return_class_time(meeting['start_seconds'], meeting['end_seconds'])
                    room = str(meeting['building']) + " " + str(meeting['room'])
                    dayList.append(day)
                    timeList.append(time)
                    roomList.append(room)

                formatted_time = format_time_optimisation(dayList, timeList)
                courseID = section['course_id']
                temp_section = Section(section_number, formatted_time, professor, 0,
                                       class_id, room, courseID) #initially sets the prof rating to 0, this is changed later
                section_object_list.append(temp_section)

    return section_object_list


def format_time_optimisation(days, timeList):
    time_final = ""
    for i in range(len(days)):
        time_final += days[i] + " " + timeList[i] + ", "
    return time_final[: -2]

def return_prof_name(name):
    if name is None:
        prof_name = "_"
    else:
        prof_name = name
    return prof_name


def return_class_time(start_time, end_time):
    class_time = (datetime.fromtimestamp(start_time) + timedelta(hours=5)).strftime("%H:%M:%S")[0:5] \
                 + " - " + (datetime.fromtimestamp(end_time) + timedelta(hours=5)).strftime("%H:%M:%S")[0:5]

    return class_time


#a = get_info_objects("math136")
#print(a[0].get_course_name())