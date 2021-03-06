#select function module 

import pickle,os,file_module
dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_dir=dirname+os.sep+'database'

key_list=['name','age','phone','dept','enroll_date']
judge_list=['>','<','=','like']

def main_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) == 8:
		demo_list=from_table(sql)
		if demo_list:
			demo_list2=where(sql,demo_list)
			if demo_list2:
				print('Find list:{}\n'.format(demo_list2))
				result=set_func(sql,demo_list2)
				if result:
					print('Update list:{}\n'.format(result))
					file_module.write_to_file(demo_list)
					print('Update done!')
			else:
				result='Sorry,do not find!'
		else:
			result='ERROR'
	else:
		print('Sorry,you enter lenght is not correct!')
		result='ERROR'

	return result

def set_func(right_sql,demo_list):
	'''if sql is 8 characters length and return demo_list or part of demo_list'''
	
	args=right_sql[3]
	if args.find('=') != -1:
		args_list=args.split('=')
		key_args=args_list[0]
		values_args=args_list[1]

		if key_args in key_list:
			key_index=key_list.index(key_args)+1
			for list in demo_list:
				list.pop(key_index)
				list.insert(key_index,values_args)
			return demo_list
		else:
			print('Sorry,your enter key invaild.')
	else:
		print('Sorry,your enter set invalid.')

def from_table(right_sql):
	'''read table'''
	table_name=right_sql[1]
	table_file=database_dir+os.sep+table_name
	if os.path.exists(table_file):
		f=open(table_file,'rb')
		demo_list=pickle.load(f)
		f.close()
		return demo_list
	else:
		print('Sorry,your enter table is not exist!')
		return False

def where(right_sql,demo_list):
	'''where ...'''
	args=right_sql[5]
	judge=right_sql[6]
	values=right_sql[7]

	def update_after_where_func():
		candidate_list=[]
		filter_list=[]
		for list in demo_list:
			candidate_list.append(list[key_index])
			if judge == '=':
				if values == candidate_list[-1]:
					filter_list.append(list)
			elif judge == '>':
				if values.isdigit() and candidate_list[-1].isdigit():
					int_values=int(values)
					determine_values=int(candidate_list[-1])
					if determine_values > int_values:
						filter_list.append(list)
				else:
					print('Your enter {} is not a digit!'.format(args))
			elif judge == '<':
				if values.isdigit() and candidate_list[-1].isdigit():
					int_values=int(values)
					determine_values=int(candidate_list[-1])
					if determine_values < int_values:
						filter_list.append(list)
				else:
					print('Your enter {} is not a digit!'.format(args))
			elif judge == 'like':
				if candidate_list[-1].find(values):
					filter_list.append(list)
				else:
					pass
			else:
				print('select after where function is worry!')
				return False
		return filter_list

	if args in key_list:
		if judge in judge_list:
			key_index=key_list.index(args)+1
			demo_list=update_after_where_func()
			return demo_list
		else:
			print('Sorry,"{}" is not a legal args'.format(judge))
			return False
	else:
		print('Sorry,"{}" is not a legal args'.format(args))
		return False


#enter=input('>>>')
#update_result=main_func(enter)
