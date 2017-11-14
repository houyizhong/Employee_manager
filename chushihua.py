import pickle

demo_list=[[1,'Alex Li','22','1803601111','IT','2013-04-01'],[2,'Jack Wang','30','18613305112','HR','2015-05-03'],[3,'Nick Cave','25','18962295184','Sales','2015-04-06']]

f=open('staff_table','wb')
pickle.dump(demo_list,f)
f.close()
