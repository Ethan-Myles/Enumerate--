import string 

#What is the enumerate function?
def enumerate(iterable, start=0): 
    i = start 
    for value in iterable: 
        yield i, value 
        i += 1

#With a list
chapters = ["The Cyclone",
"The Council with the Munchkins",
"How Dorothy saved the Scarecrow",
"The road through the forest"]

i = 0 
for chapter in chapters: 
    i += 1 
    print(f'{i}: {chapter}')

for i, chapter in enumerate(chapters): 
    print(f'{i}: {chapter}')

for i, chapter in enumerate(chapters,1): 
    chapters[i-1] = chapter.upper()
    print(f'{i}: {chapters[i-1]}')

#The tuple being yielded by the enumerate object
fruit = ['apple', 'banana', 'grape']
iterator = enumerate(fruit)    
print(next(iterator))
print(next(iterator))

#Reading a file
with open("file.txt", "r", encoding="utf-8") as file:

    line_number = 1 
    for line in file: 
        print(f"Line {line_number}: {line.strip()}") 
        line_number += 1

    for line_number, line in enumerate(file, 1): 
        print(f"Line {line_number}: {line.strip()}")

#In a dictionary comprehension
dict = {letter: number for number, letter in enumerate(string.ascii_lowercase,1)}








