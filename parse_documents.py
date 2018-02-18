from tika import parser, config
import os, io

def get_parsed_documents():
	listFiles = os.listdir('./resume')
	for file in listFiles:
		parsed = parser.from_file('./resume/' + file, xmlContent=False)
		print('Parsing: ' + file)
		io.open('./parsed_content/' + file.split('.')[0] + '.txt', 'w', encoding='utf-8').write(parsed['content'])

if __name__ == "__main__":
	get_parsed_documents()