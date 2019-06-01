#strings in class str
quote_1 = 'singleq'
quote_2 = "doubleq"
print(quote_1, quote_2)
a_1 = "quote \"within\""
#use backslash to use same quote within one quote

#raw strings
raw = r'line1\nline2\nline3'
print(raw)
rawbackslash = r'\\ '
print(rawbackslash)

#escape
pr = 'line1\tline2\tline3'
line = '\nl1\nl2\nl3'
print(pr, line)
backslash = '\\ '
print('backslash ',backslash)

#sequence objects
#concatenation +
print('_' * 40)
#repetition *
sub_text = 'This is a test'
#len(sub_text)
print('length = ', len(sub_text))
#min(sub_text)
print('min = ', min(sub_text))
#max(sub_text)
print('max =' ,max(sub_text))
#in or not in to check if one string is part of another string

#methods
#str.count("e") returns number of e
#str.index("e")
#uses 0 based indexing
#str.index("e", 3, 18) returns position of e between pos 3 and 18
#find instead of index is a better method
#str.find("X") will return -1 instead of raising index error
#str.startswiht("e")
#str.endswith("!\"")
#str.upper() or str.lower()

csv = 'a,b,c'
print('csv.split(",") will return', csv.split(","))
print('",".join(["a", "b", "c"]) returns', ",".join(["A", "b", "c"]))

#inspection functions
#str.isalpha() will be true if entire str is only alphabetic
#str.isdigit() will be true if only characters 0 to 9


