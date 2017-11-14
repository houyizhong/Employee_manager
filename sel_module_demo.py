#select function module 

import pickle,os

key_list=['name','age','phone','dept','enroll_date']
judge_list=['>','<','=','like']
demo_dict={}

def select_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) == 8:
		demo_list=from_table(sql)
		if demo_list:
			demo_list=where(sql,demo_list)
			if demo_list:
				result=sel_inner_func(sql,demo_list)
			else:
				result='ERROR'
		else:
			result='ERROR'
	else:
		result='ERROR'

	return result

def sel_inner_func(right_sql,demo_list):
	'''if sql is 8 characters length and return demo_list or part of demo_list'''
	args=right_sql[1]
	args_list=args.split(',')
	if args == '*':
		return demo_list[:]
	else:
		for i in args_list:
			raw_sel_list=[]
			if i in key_list:
				demo_dict[i]=raw_sel_list
				key_index=key_list.index(i)+1
				for list in demo_list:
					raw_sel_list.append(list[key_index])
			else:
				print('Sorry,your enter is invaild!')
		return demo_dict

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

	if args in key_list:
		if judge in judge_list:
			key_index=key_list.index(args)+1
			
			if judge == '=':
				
			return demo_list
		else:
			print('Sorry,"{}" is not a legal args'.format(judge))
			return False
	else:
		print('Sorry,"{}" is not a legal args'.format(args))
		return False

enter=input('>>>')
sel_result=select_func(enter)
print(sel_result)
