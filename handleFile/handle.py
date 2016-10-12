#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import shutil

# 获取文件的参数
# 文件和目录的创建
# 文件还是目录
# 文件的遍历
# 获取文件名
# 文件的复制


print "脚本名：", sys.argv[0]
for i in range(1, len(sys.argv)):
    print "参数", i, sys.argv[i]


def getHandleDirectory(*args):
    """
get the destination directory ,handle directory and the file type need to handle.
    :param args:
    :return:
    """
    arguments = []
    for s in args:
        arguments.append(s)
    return arguments


def copyfileswithfiletype(file_path, target_directory, file_type):
    """
    将某个文件下的所有某个类型的文件复制到目标目录。
    :param file_path: 需要处理的目录。
    :param target_directory: 复制文件到目标目录
    :param file_type: 文件类型，如jar,zip
    """
    lines = os.listdir(file_path)
    for line in lines:
        line1 = os.path.join(file_path, line)
        if os.path.isfile(line1) and line1.endswith(file_type):
            print line1
            shutil.copy(line1, target_directory)
        elif os.path.isdir(line1):
            copyfileswithfiletype(line1, target_directory, file_type)


handlefile = "E:\\apache-tomcat-9.0.0.M1"
target = "d:\\epub"
copyfileswithfiletype(handlefile, target, "jar")
