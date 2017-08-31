#!/usr/bin/env python
if True:
	print "true"
else:
	print "false"

def daynamicprint(str,* others):
	print "daili print:",str;
	print others

daynamicprint("123123")
daynamicprint(str = "kkkkk");
daynamicprint("123","123312","sddsf")

def print4me(str1 ,str2="default"):
	print str1;
	print str2;


print4me("param1");
print4me("parma1","prarm2")
