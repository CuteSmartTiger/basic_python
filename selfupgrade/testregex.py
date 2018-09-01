import re
#
# line = "D::\liuhhufjd"
# matchObj = re.match(r'^[a-zA-Z]:(\\([0-9a-zA-Z]))*', line, re.U|re.I)
# matchObj = re.match(r'^[a-zA-Z]:(((\\(?! )[^/\.:*?<>\""|\\]+)+\\?)|(\\)?)\s*$', line, re.U|re.I)
# regex = re.match(r'^[a-zA-Z]:(((\\(?! )[^/\.:*?<>\""|\\]+)+\\?)|(\\)?)\s*$', line, re.U|re.I)


# regex = r'^[a-zA-Z]:(((\\(?! )[^/\.:*?<>\""|\\]+)+\\?)|(\\)?)\s*$'
# string_types = (basestring, )

# if isinstance(regex, string_types):
#     print "ok"
# if regex:
#     print "match!!"
#
# print type("d:\liuhu")

# locationRegex = Regexp(r'^[a-zA-Z]{1}:{1}(\([0-9a-zA-Z]+))+',default_flags,lazy_gettext('Please input right url '))


# L=['d','f','r','g']
# print ",".join(L)

# x=raw_input("d:\liuhu\\")
x=r'"d:\\liuhu\\" sdf\\afdv\ %s'%("liuhu")
# test2 = "D:\liuhu\\"

# print test2[-2:-1]
# print test2
# print type(test2)
# try:
#     print x
# except SyntaxError:
#     x+="\\"
#     print x
# if x[-1]=="\\":
#     print x
# else:
#     x+="\\"
#     print x
print x