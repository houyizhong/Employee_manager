#insert employee information
#version:demo

import os,pickle

key_list=['name','age','phone','dept','enroll_date']

def main_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) == 6:
		demo_list=from_table(sql)
		if demo_list:
			demo_dict=insert_func(sql,demo_list)
			if demo_dict:
				result=insert_table_func(demo_dict)
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

def insert_func(right_sql,demo_list):
	'''insert employee info into table'''
	demo_dict={}
	args=right_sql[3]
	values=right_sql[-1]
	args_list=args.split(',')
	values_list=values.split(',')

	def judge_phone():
		for list in demo_list:
			if phone in list:
				pass
			else:
				return True

	if len(args_list) == len(values_list):
		if 'phone' in args_list:
			phone=args_list.index('phone')
			if judge_phone():
				for arg in args_list:
					if arg in key_list:
						print('HIT arg')
						value_index=args_list.index(arg)
						value=values_list[value_index]
						demo_dict[arg]=value
					else:
						print('Sorry,your enter args is invaild!')
						break
			else:
				print('Sorry,you enter phone is exist!')
		else:
			print('Sorry,the phone is UNIQUE')
	else:
		print('Sorry,you enter values is invaild!')
	return demo_dict
	

def insert_table_func(insert_dict):
	'''insert null and staff_id'''
	insert_list=[]

	for num in range(6):
		for i in insert_dict.keys():
			key_index=key_list.index(i)+1
			if key_index == num:
				insert_list.append(i)
			else:
				insert_list.append('NULL')
	
	result=insert_list
	return reslut


enter=input('>>>')
insert_result=main_func(enter)
print(insert_result)
