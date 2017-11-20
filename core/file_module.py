import pickle,os

dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_dir=dirname+os.sep+'database'
staff_table=database_dir+os.sep+'staff_table'


def write_to_file(demo_list):
        '''write to file'''
        f=open(staff_table,'wb')
        pickle.dump(demo_list,f)
        f.close()
