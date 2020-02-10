#!/usr/bin/python3

# -*- coding: UTF-8 -*-
import sys
import fileinput


file_a = ""
file_b = ""
output_contents = []

def put_title(filename1, filename2):
    str = "type " + "name".ljust(30) + "|" + filename1.center(15) + "|" + filename2.center(15) + "|" + "attribute"
    output_contents.append(str)

def put_line(tmplist, position):
    if position == 0:
        str = tmplist[0] + ' ' + tmplist[1].ljust(30) + "|" + tmplist[3].center(15) + '|' + "N\A".center(15) + '|' + tmplist[4];
    else:
        str = tmplist[0] + ' ' + tmplist[1].ljust(30) + "|" + "N\A".center(15) + "|" + tmplist[3].center(15) + "|" + tmplist[4];
    output_contents.append(str)

def put_line_with_other_value(tmplist, value):
    str = tmplist[0] + ' ' + tmplist[1].ljust(30) + "|" + tmplist[3].center(15) + "|" + value.center(15) + "|" + tmplist[4];
    output_contents.append(str)

def show_output(out):
    index = 0
    while index < len(out):
        print(out[index])
        index += 1

def get_line_by_name(name, filename):
    tmplist = []
    index = 0
    file = open(filename)
    for line in file:
        tmplist = line.split()
        if len(tmplist) != 5:
             continue
        index += 1
        if tmplist[1] == name:
            file.close()
            return line
    file.close()
    return None

#filter flag name only in one file
def filter_flag_name(filename1, filename2):
    tmplist = []

    file = open(filename1)
    for line in file:
        tmplist = line.split()
        if len(tmplist) != 5:
             continue
        result = get_line_by_name(tmplist[1], filename2)
        if result == None:
            put_line(tmplist, 0)
    file.close()

    file = open(filename2)
    for line in file:
        tmplist = line.split()
        if len(tmplist) != 5:
            continue
        result = get_line_by_name(tmplist[1], filename1)
        if result == None:
            put_line(tmplist, 1)
    file.close()
    return

#filter flag in both a and b, but different value
def filter_flag_value(filename1, filename2):
    tmplist = []
    otherlist = []
    result = ""

    file = open(filename1)
    for line in file:
        tmplist = line.split()
        if len(tmplist) != 5:
            continue
        result = get_line_by_name(tmplist[1], filename2)
        if result != None:
            otherlist = result.split()
            if (otherlist[1] == tmplist[1]) and (result != line):
                put_line_with_other_value(tmplist, otherlist[3])
    file.close()

def main():
    """
     通过sys模块来识别参数demo, http://blog.csdn.net/ouyang_peng/
    """
    #print('参数个数为:', len(sys.argv), '个参数。')
    #print('参数列表:', str(sys.argv))
    #print('脚本名为：', sys.argv[0])
    #for i in range(1, len(sys.argv)):
    #    print('参数 %s 为：%s' % (i, sys.argv[i]))
    file_a = "aaa.txt"
    file_b = "bbb.txt"
    output = "output.txt"

    put_title(file_a, file_b)
    filter_flag_name(file_a, file_b)
    filter_flag_value(file_a, file_b)
    show_output(output_contents)


if __name__ == "__main__":
    main()