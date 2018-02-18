import requests
import zipfile,os, io

def download_zip_files(path):
	resume_list = open('Resumes_List.txt').read()
	resume_list = resume_list.split('\n')
	print(len(resume_list))
	for resume in resume_list:
		print('Downloading resume ' + resume)
		r = requests.get(resume)
		z = zipfile.ZipFile(io.BytesIO(r.content))
		z.extractall('resume')

def extract_zip_files(path):
	resume_list = open('Resumes_List.txt').read()
	resume_list = resume_list.split('\n')
	for resume in resume_list:
		zip_files = zipfile.ZipFile(os.path.join('./resume', resume.split('/')[-1]),'r')
		zip_files.extractall('resume')
		zip_files.close()

def download_extract_resumes():
	path = '.'
	# download all the files in resume directory
	download_zip_files(path)
	# extract_zip_files(path)

if __name__ == '__main__':
	download_extract_resumes()
