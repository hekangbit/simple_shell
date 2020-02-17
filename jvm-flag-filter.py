#!/usr/bin/python3

# -*- coding: UTF-8 -*-
import sys
import fileinput


file_a = ""
file_b = ""
output_contents = []

def put_title(filename1, filename2):
    str = "type".ljust(8) + "|" + "name".ljust(45) + "|" + filename1.center(30) + "|" + filename2.center(30) + "|" + "    class".ljust(35) + '|'
    output_contents.append(str)
    output_contents.append(" ")

def put_line(tmplist, position):
    
    if position == 0:
        str = tmplist[0].ljust(8) + "|" + tmplist[1].ljust(45) + "|" + tmplist[3].center(30) + '|' + "None".center(30) + '|' + tmplist[4].center(30) + '|'
    else:
        str = tmplist[0].ljust(8) + "|" + tmplist[1].ljust(45) + "|" + "None".center(30) + "|" + tmplist[3].center(30) + "|" + tmplist[4].center(30) + '|'

    output_contents.append(str)

def put_line_with_other_value(tmplist, value):
    str = tmplist[0].ljust(8) + "|" + tmplist[1].ljust(45) + "|" + tmplist[3].center(30) + "|" + value.center(30) + "|" + tmplist[4].center(30) + '|'
    output_contents.append(str)

def show_output(out):
    index = 0
    while index < len(out):
        print(out[index])
        index += 1

def get_line_by_name(name, filename):
    tmplist = []
    file = open(filename)
    for line in file:
        line = line.strip()
        tmplist = line.split()

        if len(tmplist) <= 3:
             continue
        if tmplist[2] != '=':
             continue
        if tmplist[1] == name:
            file.close()
            return line
    file.close()
    return None

#filter flag name only in one file
def filter_flag_name(filename1, filename2):
    tmplist = []
    index = 0
    file = open(filename1)
    for line in file:
        line = line.strip()
        tmplist = line.split()

        if len(tmplist) <= 3:
             continue
        if tmplist[2] != "=":
             continue
        if tmplist[3][0] == "{":
            tmplist.insert(3, "__")
        index = 5
        while index < len(tmplist):
            tmplist[4] = tmplist[4] + " " + tmplist[index]
            index += 1

        result = get_line_by_name(tmplist[1], filename2)
        if result == None:
            put_line(tmplist, 0)
    file.close()

    tmplist = []
    file = open(filename2)
    for line in file:
        line = line.strip()
        tmplist = line.split()

        if len(tmplist) <= 3:
             continue
        if tmplist[2] != "=":
             continue
        if tmplist[3][0] == "{":
            tmplist.insert(3, "__")
        index = 5
        while index < len(tmplist):
            tmplist[4] = tmplist[4] + " " + tmplist[index]
            index += 1

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
    index = 0

    file = open(filename1)
    for line in file:
        line = line.strip()
        tmplist = line.split()

        if len(tmplist) <= 3:
             continue
        if tmplist[2] != "=":
             continue
        if tmplist[3][0] == '{':
            tmplist.insert(3, "__")
        index = 5
        while index < len(tmplist):
            tmplist[4] = tmplist[4] + " " + tmplist[index]
            index += 1

        result = get_line_by_name(tmplist[1], filename2)

        if result != None:
            otherlist = result.split()

            if len(otherlist) <= 3:
                continue
            if otherlist[2] != "=":
                continue
            if otherlist[3][0] == '{':
                otherlist.insert(3, "__")
            index = 5
            while index < len(otherlist):
                otherlist[4] = otherlist[4] + " " + otherlist[index]
                index += 1

            if (otherlist[1] == tmplist[1]) and (result != line):
                put_line_with_other_value(tmplist, otherlist[3])
    file.close()

def main():
    """
     通过sys模块来识别参数
    """
    #print('参数个数为:', len(sys.argv), '个参数。')
    #print('参数列表:', str(sys.argv))
    #print('脚本名为：', sys.argv[0])
    #for i in range(1, len(sys.argv)):
    #    print('参数 %s 为：%s' % (i, sys.argv[i]))
    #file_a = "aaa.txt"
    #file_b = "bbb.txt"
    #output = "output.txt"
    file_a = sys.argv[1]
    file_b = sys.argv[2]

    put_title(file_a, file_b)
    filter_flag_name(file_a, file_b)
    filter_flag_value(file_a, file_b)
    show_output(output_contents)


if __name__ == "__main__":
    main()
