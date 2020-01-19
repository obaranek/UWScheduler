import statistics
from model.Section import  Section

def normalize_rating(list_of_sec):
    count = 0
    total = 0
    lst = []
    for sec in list_of_sec:
        lst.append(sec.__prof_rating)
    mean = statistics.mean(lst)
    stdev = statistics.stdev(lst)

    for sec in list_of_sec:
        sec._prof_rating = (sec._prof_rating - mean)/stdev

    return list_of_sec

c1 = 35
c2 = 30
c3 = 25
c4 = 10
c5 = 5

#input: a Section
#output: a list of string


def list_of_time(course_sec):
    time = course_sec.get_time()
    time_by_day = time.split(', ')
    time_list = []
    for day in time_by_day:
        lst = day.split()
        weekday = lst[0]
        strattime = lst[1]
        endtime = lst[3]
        strattime_list = strattime.split(':')
        starttime_num = float(strattime_list[0]) + float(strattime_list[1])/60
        endtime_list = endtime.split(':')
        endtime_num = float(endtime_list[0]) + float(endtime_list[1])/60
        time_interval = starttime_num
        while time_interval < endtime_num:
            time_list.append(weekday + ' ' + str(time_interval))
            time_interval = time_interval + 0.5
    return time_list


#input: 5 lists of Sections
#output: a list of Section
def optimize(course_1, course_2, course_3, course_4, course_5):
    occupied_time = []
    score = None
    best_sec_for_course_1 = None
    best_sec_for_course_2 = None
    best_sec_for_course_3 = None
    best_sec_for_course_4 = None
    best_sec_for_course_5 = None

    for sec1 in course_1:
        occupied_time = occupied_time + list_of_time(sec1)
        for sec2 in course_2:
            conflict_2 = False
            time2 = list_of_time(sec2)
            for time_interval2 in time2:
                if time_interval2 in occupied_time:
                    conflict_2 = True
                    break
            if conflict_2:
                continue
            occupied_time = occupied_time + time2
            for sec3 in course_3:
                conflict_3 = False
                time3 = list_of_time(sec3)
                for time_interval3 in time3:
                    if time_interval3 in occupied_time:
                        conflict_3 = True
                        break
                if conflict_3:
                    continue
                occupied_time = occupied_time + time3
                for sec4 in course_4:
                    conflict_4 = False
                    time4 = list_of_time(sec4)
                    for time_interval4 in time4:
                        if time_interval4 in occupied_time:
                            conflict_4 = True
                            break
                    if conflict_4:
                        continue
                    occupied_time = occupied_time + time4
                    for sec5 in course_5:
                        conflict_5 = False
                        time5 = list_of_time(sec5)
                        for time_interval5 in time5:
                            if time_interval5 in occupied_time:
                                conflict_5 = True
                                break
                        if conflict_5:
                            continue
                        #print(sec1,sec2,sec3,sec4,sec5)
                        if (score is None) or (c1 * sec1.get_prof_rating() + c2 * sec2.get_prof_rating() + c3 * sec3.get_prof_rating() + c4 * sec4.get_prof_rating() + c5 * sec5.get_prof_rating()) > score:
                            score = (c1 * sec1.get_prof_rating() + c2 * sec2.get_prof_rating() + c3 * sec3.get_prof_rating() + c4 * sec4.get_prof_rating() + c5 * sec5.get_prof_rating())
                            best_sec_for_course_1 = sec1
                            best_sec_for_course_2 = sec2
                            best_sec_for_course_3 = sec3
                            best_sec_for_course_4 = sec4
                            best_sec_for_course_5 = sec5
    sec1_lst = {'course_name': best_sec_for_course_1.get_course_name(), 'section_number': best_sec_for_course_1.get_section_number(), 'prof_name': best_sec_for_course_1.get_prof_name(), 'time': best_sec_for_course_1.get_time()}
    sec2_lst = {'course_name': best_sec_for_course_2.get_course_name(), 'section_number': best_sec_for_course_2.get_section_number(), 'prof_name': best_sec_for_course_2.get_prof_name(), 'time': best_sec_for_course_2.get_time()}
    sec3_lst = {'course_name': best_sec_for_course_3.get_course_name(), 'section_number': best_sec_for_course_3.get_section_number(), 'prof_name': best_sec_for_course_3.get_prof_name(), 'time': best_sec_for_course_3.get_time()}
    sec4_lst = {'course_name': best_sec_for_course_4.get_course_name(), 'section_number': best_sec_for_course_4.get_section_number(), 'prof_name': best_sec_for_course_4.get_prof_name(), 'time': best_sec_for_course_4.get_time()}
    sec5_lst = {'course_name': best_sec_for_course_5.get_course_name(), 'section_number': best_sec_for_course_5.get_section_number(), 'prof_name': best_sec_for_course_5.get_prof_name(), 'time': best_sec_for_course_5.get_time()}
    final = {"courses": [sec1_lst, sec2_lst, sec3_lst, sec4_lst, sec5_lst]}
    return final
