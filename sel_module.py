#select function module 

import pickle,os

key_list=['name','age','phone','dept','enroll_date']
judge_list=['>','<','=','like']

def select_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) == 8:
		demo_list=from_table(sql)
		if demo_list:
			demo_list=where(sql,demo_list)
			if demo_list:
				result=sel_inner_func(sql,demo_list)
				if len(result) != 2:
					print('Error!Something worry...')
				else:
					sel_result=result[0]
					sel_len=result[1]
					print(sel_result)
					print('Find {} items'.format(sel_len))
			else:
				result='Sorry,do not find!'
		else:
			result='ERROR'
	else:
		print('Sorry,you enter lenght is not correct!')
		result='ERROR'

	return result

def sel_inner_func(right_sql,demo_list):
	'''if sql is 8 characters length and return demo_list or part of demo_list'''
	demo_dict={}
	len_list=0
	args=right_sql[1]
	args_list=args.split(',')
	if args == '*':
		len_list=len(demo_list)
		return demo_list[:],len_list
	else:
		for i in args_list:
			raw_sel_list=[]
			if i in key_list:
				demo_dict[i]=raw_sel_list
				key_index=key_list.index(i)+1
				for list in demo_list:
					raw_sel_list.append(list[key_index])
				len_list=len_list+len(raw_sel_list)
			else:
				print('Sorry,your enter is invaild!')
				break
		return demo_dict,len_list

def from_table(right_sql):
	'''read table'''
	table_name=right_sql[3]
	if os.path.exists(table_name):
		f=open(table_name,'rb')
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

	def select_after_where_func():
		candidate_list=[]
		filter_list=[]
		for list in demo_list:
			candidate_list.append(list[key_index])
			if judge == '=':
				if values == candidate_list[-1]:
					filter_list.append(list)
			elif judge == '>':
				if values.isdigit() and candidate_list[-1]:
					int_values=int(values)
					determine_values=int(candidate_list[-1])
					if determine_values > int_values:
						filter_list.append(list)
				else:
					print('Your enter {} is not a digit!'.format())
			elif judge == '<':
				if values.isdigit() and candidate_list[-1]:
					int_values=int(values)
					determine_values=int(candidate_list[-1])
					if determine_values < int_values:
						filter_list.append(list)
				else:
					print('Your enter {} is not a digit!'.format(values))
			elif judge == 'like':
				if candidate_list[-1].find(values) != -1:
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
			demo_list=select_after_where_func()
			return demo_list
		else:
			print('Sorry,"{}" is not a legal args'.format(judge))
			return False
	else:
		print('Sorry,"{}" is not a legal args'.format(args))
		return False

#enter=input('>>>')
#raw_sel_result=select_func(enter)
