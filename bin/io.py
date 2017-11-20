#staff table io
#version:demo
import os,sys

dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
core_dir=dirname+os.sep+'core'
sys.path.append(core_dir)

import insert_module,update_module,delete_module,sel_module,chushihua

while True:
	enter=input('>>>')

	if enter.startswith('select') or enter.startswith('SELECT'):
		result=sel_module.select_func(enter)
	elif enter.startswith('insert') or enter.startswith('INSERT'):
		result=insert_module.main_func(enter)
	elif enter.startswith('update') or enter.startswith('UPDATE'):
		result=update_module.main_func(enter)
	elif enter.startswith('delete') or enter.startswith('delete'):
		result=delete_module.main_func(enter)
	elif enter == 'chushihua':
		result=chushihua.main()
	elif enter == 'q':
		break
	else:
		print('Sorry,you enter invalid!Please try again...')

