"""
Programming In Python - Lesson 4 Exercise 2 (Part 2): File reading and parsing
Code Poet: Anthony McKeever
Start Date: 08/05/2019
End Date: 08/05/2019
"""

languages = set()

f = open("students.txt")
for line in f.readlines():
    if line == "Name: Nickname, languages\n":
        continue
        
    splitted = line.split(":")[-1:]
    tst = str(splitted).split(",")    

    for l in tst:
        print(l)
        if not l[0].isupper:
            languages.add(l.strip())
    
print(languages)