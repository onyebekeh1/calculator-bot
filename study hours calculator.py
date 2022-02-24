days = 24
print("input number of days you intend to study")
timeframe = int(input())
time = timeframe * days#timeframe of study multiplied by 24hours a day
print(time)
print(" what is the estimated hours you intend to complete the course materials")
course = int(input())#total time of course materials
print(str(course ) + " is the total time for course materials")
study_time_daily = int(input("number of hour designated for study")) 
other_bhiz = days - study_time_daily 
print(other_bhiz)
busy = other_bhiz * timeframe#total time for other bhis equals 24hrs minus amount of time devoted for study multiplied by timeframe of study
print(busy)
study = time - busy#study time timeframe of study minus total time for all bhiz
print(str(study) + " is study hours")
