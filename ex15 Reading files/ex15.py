from sys import argv
script,filename = argv
txt = open(filename)

print "here's your file %r."%filename
print txt.read()


print "type the filename again,please."
file_again = raw_input("your filename:")
txt_again =open(file_again)

print txt_again.read()