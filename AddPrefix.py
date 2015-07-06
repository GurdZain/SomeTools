#coding:utf-8
import argparse

def Add(file1, prefix):
	file1 = open(file1,'r')
	end_file = open('new.txt','w')

	file_list = file1.readlines()
	file_len = len(file_list)
	for x in xrange(0, file_len):
		file_list[x] = prefix + '_' + file_list[x]

	end_file.writelines(file_list)

	file1.close()
	end_file.close()


def parse_argv():
	parser = argparse.ArgumentParser()
	parser.add_argument('file1', type=str, help='file name')
	parser.add_argument('prefix', type=str, help='you want to add prefix')

	return parser.parse_args()

if __name__ == '__main__':
	args = parse_argv()
	file1 = args.file1
	prefix = args.prefix

	Add(file1, prefix)