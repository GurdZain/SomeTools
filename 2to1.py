#coding:utf-8

import argparse

def addfile(file1, file2):
	first_file  = open(file1, 'r')
	second_file = open(file2, 'r')
	end_file    = open('new.txt', 'w')

	first  = first_file.readlines()
	second = second_file.readlines()

	second_len = len(second)
	for x in range(0, second_len):
		if second[x] in first:
			print second[x]
			continue
		else:
			first.append(second[x])

	end_file.writelines(first)
	end_file.close()
	first_file.close()
	second_file.close()

def parse_argv():
	parser = argparse.ArgumentParser()
	parser.add_argument('file1', type=str, help='first file')
	parser.add_argument('file2', type=str, help='second file')

	return parser.parse_args()

if __name__ == '__main__':
	args = parse_argv()
	file1 = args.file1
	file2 = args.file2
	addfile(file1, file2)


