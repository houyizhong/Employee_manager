#delete employee fucntion
#version:demo

import os,pickle,file_module

dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_dir=dirname+os.sep+'database'

def main_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) == 5:
		demo_list=from_table(sql)
		if demo_list:
			result=delete_func(sql,demo_list)
			if result:
				file_module.write_to_file(result)
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
         table_file=database_dir+os.sep+table_name
         if os.path.exists(table_file):
                 f=open(table_file,'rb')
                 demo_list=pickle.load(f)
                 f.close()
                 return demo_list
         else:
                 print('Sorry,your enter table is not exist!')
                 return False


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


#enter=input('>>>')
#delete_result=main_func(enter)
