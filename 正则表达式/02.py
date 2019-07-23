
import re
# s = '<html><body><h1>hello world<h1><body><html>'
# #
# # print(s.find('<h1>'))
# # print(re.split(r'(?<=<h1>)\w+(?=<h1>)',s))
# p1 = r'(?<=<h1>).+?(?=<h1>)'
# p2 = r'(?<=<h1>).+(?=<h1>)'
#
# pattern1 = re.compile(p1)
# pattern2 = re.compile(p2)
#
# matcher1 = re.search(p1,s)
# matcher2 = re.search(p2,s)
#
# matcher11 = re.search(r'(?<=<h1>).+?(?=<h1>)',s)
# matcher22 = re.search(r'(?<=<h1>).+(?=<h1>)',s)
#
# print(matcher11.group(0))
# print(matcher22.group(0))
#
# '''
# python和正则表达式均区分大小写
# '''
#
# print(matcher1.group(0))
#
# print(matcher2.group(0))
#

# key = r'lywang@mmednet.com'
# pp = r'.+@.+\..+'
#
# mm = re.compile(pp)
#
# print(mm.findall(key))

# key = r'lalala<hTml>hello<//htmL>heiheihei'
#
# pp = r'<[Hh][Tt][Mm][Ll]>.+<//[Hh][Tt][Mm][Ll]>'
#
# mm = re.compile(pp)
# print(mm.findall(key))


key = 'mrk192.168.1.1'
pp = r'(\d{1,3}\.){3}\d{1,3}'
# pp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# pp = r'(\d{1,3}\.){3}\d{1,3}'
mm = re.search(pp,key)
print(mm.group(0))
# mm = re.compile(pp)
# mmm = mm.search(key)
# print(mm.gr)
# print(mm.match(key))
# print(mm.search(key))
# mm = re.search(pp,key)
#
# print(mm.group(0))