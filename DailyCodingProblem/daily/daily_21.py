"""
Given an array of time intervals (start, end) for
classroom lectures (possibly overlapping), find
the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)],
you should return 2. 
"""
def intersecting(time_1, time_2):
    return (time_2[0] < time_1[0] < time_2[1]) or (time_2[0] < time_1[1] < time_2[1])
    
def available_gap(lecture_class_log, lecture_time):
    for logged_time in lecture_class_log:
        if not intersecting(logged_time, lecture_time):
            return True
    return False

def classrooms_assigned(classroom_lectures):
    lecture_class_log = []
    needed_classrooms = 0
    for lecture_time in classroom_lectures:
        if not lecture_class_log:
            needed_classrooms += 1
            lecture_class_log.append(lecture_time)
        else:
            if not available_gap(lecture_class_log, lecture_time):
                needed_classrooms += 1
                lecture_class_log.append(lecture_time)
    
    return needed_classrooms
                

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = classrooms_assigned

inputs = [
    {'classroom_lectures': [(30, 75), (0, 50), (60, 150)]},
    {'classroom_lectures': [(0, 10), (5, 25), (20, 30)]}
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")