from os import listdir
from os.path import isfile, join
import os
import shutil
from datetime import datetime
import logging


def sort_files_in_a_folder(mypath):
	'''
		A function to sort the files in a folder
		into their respective categories 
	'''
	try:
	
		now = datetime.now()
		str_now = now.strftime("%d-%m-%Y_%H_%M_%S")
		
		logging.basicConfig(filename='cleanfolder.log',level=logging.INFO)
		
		files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

		file_type_variation_list=[]
		folder_list=[]
		filetype_to_folder_dict={}
	
	
		for file in files:	
			
			try:
				filetype=file.split('.')[1]
			except IndexError:
				logging.error(str_now + ' Bad File Extension:' + mypath +'/'  +file, exc_info=True)
				continue
			
			if filetype not in  file_type_variation_list:
				file_type_variation_list.append(filetype)
				new_folder_name=mypath+'/'+ filetype + '_folder'
				filetype_to_folder_dict[str(filetype)]=str(new_folder_name)
				if os.path.isdir(new_folder_name)==True:  #folder exists
					continue
				else:	
					os.mkdir(new_folder_name)	

		for file in files:
			src_path=mypath+'/'+file
			
			try:
				filetype=file.split('.')[1]
			except IndexError:
				continue
			
			if filetype in filetype_to_folder_dict.keys():
				dest_path=filetype_to_folder_dict[str(filetype)]
				dest_file=dest_path +'/' + file 
				if os.path.isfile(dest_file)==True:
					os.rename(dest_file, dest_file + '_' + str_now)
					shutil.move(src_path,dest_path)
				else:	
					shutil.move(src_path,dest_path)
				print(src_path + '>>>' + dest_path)
				
	except Exception as e:
		logging.error(str_now +"Exception Occured", exc_info=True)
			

if __name__=="__main__":

	try:
		mypath='//dtnas1hq/users/leonard.santoro'
		sort_files_in_a_folder(mypath)
		
		mypath='//dtnas1hq/users/leonard.santoro//Project Docs'
		sort_files_in_a_folder(mypath)
		
		mypath='//dtnas1hq/users/leonard.santoro//Personal'
		sort_files_in_a_folder(mypath)
		
		mypath='C://Users//leonard.santoro//Downloads'
		sort_files_in_a_folder(mypath)
		
		print('File Cleaner Completed')
		
	except Exception as e:
		now = datetime.now()
		str_now = now.strftime("%d-%m-%Y_%H_%M_%S")
		logging.error(str_now +'Exception Occured', exc_info=True)