import re 
string = "abbbbbbbbbbbbc"
pattern = "ab+c" 

if re.match(pattern,string):
    print("Match Found")
else:
    print('No Match Found')