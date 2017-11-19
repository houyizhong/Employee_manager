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
				result=insert_table_func(demo_dict,demo_list)
				if len(result) == 6:
					demo_list.append(result)
					write_to_file(demo_list)
				print('You insert staff table:\n {}'.format(result))
					
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
				print(phone)
				print(list)
				return False
			else:
				pass
		return True

	if len(args_list) == len(values_list):
		if 'phone' in args_list:
			phone_index=args_list.index('phone')
			phone=values_list[phone_index]
			if judge_phone():
				for arg in args_list:
					if arg in key_list:
						value_index=args_list.index(arg)
						value=values_list[value_index]
						demo_dict[arg]=value
					else:
						print('Sorry,your enter args is invaild!')
						demo_dict={}
						break
			else:
				print('Sorry,you enter phone is exist!')
		else:
			print('Sorry,the phone is UNIQUE')
	else:
		print('Sorry,you enter values is invaild!')
	return demo_dict
	

def insert_table_func(insert_dict,demo_list):
	'''insert null and staff_id'''
	insert_list=[]
	number=len(demo_list)+1
	insert_list.insert(0,number)

	for i in key_list:
		info_values=insert_dict.get(i,'NULL')
		insert_list.append(info_values)
	
	
	return insert_list


def write_to_file(demo_list):
	'''write to file'''
	f=open('staff_table','wb')
	pickle.dump(demo_list,f)
	f.close()

enter=input('>>>')
insert_result=main_func(enter)
