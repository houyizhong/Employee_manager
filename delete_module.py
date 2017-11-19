#delete employee fucntion
#version:demo

import os,pickle

def main_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) == 5:
		demo_list=from_table(sql)
		if demo_list:
			result=delete_func(sql,demo_list)
			if result:
				write_to_file(result)
				print('Delete done!')
			else:
				result='ERROR'
		else:
			result='ERROR'
	else:
		print('Sorry,you enter lenght is not correct!')
		result='ERROR'
	return result

def from_table(right_sql):
	'''read table'''
	table_name=right_sql[2]
	if os.path.exists(table_name):
		f=open(table_name,'rb')
		demo_list=pickle.load(f)
		f.close()
		return demo_list
	else:
		print('Sorry,your enter table is not exist!')
		return False


def write_to_file(demo_list):
	'''write to file'''
	f=open('staff_table','wb')
	pickle.dump(demo_list,f)
	f.close()

def delete_func(right_sql,demo_list):
	delete_id=right_sql[-1]
	delete_id=delete_id.split(',')

	for id in delete_id:
		if id.isdigit():
			id=int(id)
			if 0 < id <= len(demo_list):
				id=id - 1
				demo_list.pop(id)
				return demo_list
			else:
				print('Sorry,you enter id is not exist')
		else:
			print('Sorry,you enter id invaild')


enter=input('>>>')
delete_result=main_func(enter)
