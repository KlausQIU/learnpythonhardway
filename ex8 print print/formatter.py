# -*- coding:utf-8 -*-
formatter = "%s%r%r%r"
print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,True,False)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
     "i had this thing",
     "that you could type up right",
     "but it didn't sing.",
     "so i said goodnight. "
)

print formatter %("中文","1","test","chinese")
