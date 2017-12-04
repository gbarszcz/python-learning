# coding=utf-8
# Korzystając z modułu subprocess napsiz program który tworzy strukturę katalogów podaną w formie:
import subprocess

dirStr = '''
K1
    K2
    K3
        K4
K5
    K6'''
tree = subprocess.check_call("tree /A", shell=True)
# treeStr = str(tree)
# treeStr = treeStr.replace("+", "")
# treeStr = treeStr.replace("---", "")
# treeStr = treeStr.replace("\\", "")
# treeStr = treeStr.replace("|", "")
# print treeStr
