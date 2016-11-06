import datetime
import time
import models
# 
# # for year=CurrentYear
# #	visitType=New
# 	person=PwC
# 	timeStamp in CurrentQuartile
# 	centre = SomeCentre
# 
quartile = 1
year = datetime.datetime.now().year
person = 'PwC'
visitType = 'New'


visitType
person
quartile
year
location
region


# 
low = datetime.datetime(year=year, month=(quartile-1)*3+1, day=1)
lowTime = time.mktime(low.timetuple())
# 
high = datetime.datetime(year=year, month=quartile*3+1, day=30)
highTime = time.mktime(high.timetuple())
# 
#member=StaffMember(name='Sam',staffGroup='CSS',location='Bratislava',region='Slovakia')
# 
#record1 = Record.objects.filter(visitType = visitType, person = person, location = member.location, region = member.region, timeStamp >= lowTime, timeStamp <= highTime)
# 
# print record1
# 
# # for year=CurrentYear-1
# 	visitType=New
# 	person=PwC
# 	timeStamp in CurrentQuartile - 1 year
# 	centre = SomeCentre
# 
# 
# # calculate percentage ration (new PwCs percentage increase)
# 
# 	# the same, just with person=Carer
# 	visitType=New
# 	person=Carer
# 	timeStamp in CurrentQuartile
# 	centre = SomeCentre
# 
# 
# 
# # total visits in certain quartile
# count(record)
# 	centre = SomeCentre
# 	timeStamp in CurrentQuartile
# 
# # total visits in certain quartile - 1 year
# 
# # percentage growth of total visits
# 
# 
# 


for each cancer_site
person=PwC
visit_type=New
quartile=Some


for each core activity
total delivered
percentage of total


RECORDS such that
	centre=SomeCentre
	year=SomeYear
	location=SomeLocation
	region=SomeRegion
