import pickle,sys,os

demo_list=[[1,'Alex Li','22','1803601111','IT','2013-04-01'],[2,'Jack Wang','30','18613305112','HR','2015-05-03'],[3,'Nick Cave','25','18962295184','Sales','2015-04-06']]

dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_dir=dirname+os.sep+'database'
staff_table=database_dir+os.sep+'staff_table'

def main():
	f=open(staff_table,'wb')
	pickle.dump(demo_list,f)
	f.close()
	print('Initialize done!')
	return 'Initialize done!'
