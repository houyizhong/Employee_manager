#select function module 

demo_list=[1,'Alex Li','22','1803601111','IT','2013-04-01']
key_list=['name','age','phone','dept','enroll_date']
args_list=[]
raw_sel_list=[]

def select_func(sql):
	'''judge sql is correct length'''
	sql=sql.split(' ')
	if len(sql) <8 or len(sql) > 11:
		print('error')
	else:
		result=sel_inner_func(sql)
	return result

def sel_inner_func(right_sql):
	if len(right_sql) == 8:
		'''if sql is 8 characters length and return demo_list or part of demo_list'''
		if right_sql[1] == '*':
			return demo_list
		elif right_sql[1] in key_list:
			key=right_sql[1]
			key_index=key_list.index(key)+1
			return demo_list[key_index]
		else:
			pass
	elif len(right_sql) >= 9:
		'''if sql is more than 8 characters length and return raw_sel_list'''
		for args in right_sql:
			if args == 'from':
				break
			args_list.append(args)
			#print(args_list)
		key_set=set(args_list[1:])
		key_list_set=set(key_list)
		if key_set.issubset(key_list_set):
			for i in key_set:
				key_index=key_list.index(i)+1
				raw_sel_list.append(demo_list[key_index])
			return raw_sel_list
		else:
			pass
	
	'''
	elif len(right_sql) == 9:
		if right_sql[1] in key_list and right_sql[2] in key_list:
			print('HIT-TWO-KEY')
			key1=right_sql[1]
			key2=right_sql[2]
			key1_index=key_list.index(key1)+1
			key2_index=key_list.index(key2)+1
			return demo_list[key1_index],demo_list[key2_index]
	elif len(right_sql) == 10:
		if right_sql[1] in key_list and right_sql[2] in key_list and right_sql[3] in key_list:
			print('HIT-THREE-KEY')
			key1=right_sql[1]
			key2=right_sql[2]
			key3=rigght_sql[3]
			key1_index=key_list.index(key1)+1
			key2_index=key_list.index(key2)+1
			key3_index=key_list.index(key3)+1
			return demo_list[key1_index],demo_list[key2_index],demo_list[key3_index]
	elif len(right_sql) == 11:
		pass
	'''

enter=input('>>>')
sel_result=select_func(enter)
print(sel_result)
