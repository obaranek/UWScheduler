'''
    This file scrapes RateMyProf and puts all the prof data in a text file
'''

import requests
import json
import math


class RateMyProfFileCreator:
    def __init__(self, schoolid):
        self.UniversityId = schoolid
        self.professorlist = self.createprofessorlist()
        #print(self.professorlist[0])
        self.create_file()

    def createprofessorlist(
            self):  # creates List object that include basic information on all Professors from the IDed University
        tempprofessorlist = []
        num_of_prof = self.GetNumOfProfessors(self.UniversityId)
        num_of_pages = math.ceil(num_of_prof / 20)
        i = 1
        while (i <= num_of_pages):  # the loop insert all professor into list
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                i) + "&filter=teacherlastname_sort_s+asc&query=%3A&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                self.UniversityId))
            temp_jsonpage = json.loads(page.content)
            temp_list = temp_jsonpage['professors']
            tempprofessorlist.extend(temp_list)
            i += 1
        return tempprofessorlist

    def GetNumOfProfessors(self, id):  # function returns the number of professors in the university of the given ID.
        page = requests.get(
            "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                id))  # get request for page
        temp_jsonpage = json.loads(page.content)
        num_of_prof = temp_jsonpage[
                          'remaining'] + 20  # get the number of professors at William Paterson University
        return num_of_prof

    def create_file(self):
        file = open(r"../control/ProfRatingFile", "w")

        for prof in self.professorlist:
            prof_first_name = prof['tFname']
            prof_last_name = prof['tLname']

            name_rmp = prof_last_name + ',' + prof_first_name[0]

            rating = prof['overall_rating']
            if rating == "N/A":
                rating = "NA"

            prof_file_record = name_rmp + '|' + rating+"\n"

            file.write(prof_file_record)

        file.close()


UWaterloo = RateMyProfFileCreator(1490)