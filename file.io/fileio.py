import os
if os.path.exists("practice.txt"):
    print("file exist")
else:
    print("file don't exist")

#WRITE AND READ NAME:
name=input("Enter your name:")
with open("practice.txt","w") as file:
    file.write(name)

with open("practice.txt","r") as file:
    saved_name=file.read()

print("hello",saved_name+"!")

#WRITE MULTIPLE LINES:
lines = [
    "hallo\n",
    "ich bin achal\n",
    "ich bin studentin\n",
    "ich wohne in nanded\n",
    "meine hobby ist singen\n",
    "danke\n"
]
# with open("practice.txt","a") as file: 
#     file.writelines(lines)  

with open("practice.txt","r") as file:
    content=file.readlines()

# print(content)

#CLEAR THE FILE:
# with open("practice.txt","w") as file:
#     pass

#COUNT WORDS IN FILE:
# with open("story.txt","x") as file:
#     pass
story=[
    "A small cat saw a big dog in the yard.\n"
    "At first, it felt scared, but then it stood tall.\n"
    "The dog walked away, and the cat felt proud.\n"
    "From that day, the cat knew it could be brave.\n"
]
with open("story.txt","w")as file:
    file.writelines(story)

with open("story.txt","r") as file:
    text=file.read()
    lines=text.split("\n")
    words=text.split()
    characters=len(text)

print("no.of lines:",len(lines))
print("no.of words:",len(words))
print(characters)

#COPY FILE CONTENT:
# with open("destination.txt","x") as file:
#     pass

with open("story.txt","r") as file:
    content=file.readlines()

with open("destination.txt","w+") as file:
    file.writelines(content)#After writelines(), the file pointer is at the end of the file, so when you immediately call read(), it returns an empty string
    file.seek(0)# Move pointer back to the start
    new_content=file.read()
print(new_content)

#APPEND MODE:
clever_rabbit=[
    "Once upon a time, a hungry fox tried to catch a clever rabbit.\n"
    "The rabbit quickly ran into a small hole that was too tiny for the fox.\n"
    "The fox waited outside all day but couldn't reach the rabbit.\n"
    "The rabbit laughed and hopped away safely, proud of its cleverness.\n"
]
# with open("story.txt","a") as file:
#     file.writelines(clever_rabbit)

with open("story.txt","r") as file:
    two_story=file.read()

print(two_story)

# STORE AND READ NUMBERS:
# with open("numbers.txt","x")as file:
#     pass
with open("numbers.txt","w+") as file:
    sum_numbers=0
    for i in range(1,11):
        file.write(f"{i}\n")
        sum_numbers+=i

    file.seek(0)
    content=file.read()
print("Numbers in file:")
print(content)
print("sum of numbers:",sum_numbers)

#REVERSE FILE CONTENT:
# with open("reverse.txt","x") as f:
#     pass
text=[
    " Hello, I am Achal.\n"
    "I love coding.\n"
    "Python is fun!\n"
]
with open("reverse.txt","w+") as f:
    f.writelines(text)#write all lines
    f.seek(0)#moves pointer back to the start
    content=f.read()#now reads the whole content

reversed_text=content[::-1]
print("original text:",content)
print("reversed text :",reversed_text)

#SEARCH IN FILE:
# with open("data.txt","x")as f:
#     pass

sentences=[
    "The sun sets behind the tall mountains.\n",
    "A little bird sang a sweet melody.\n",
    "Knowledge grows when it is shared.\n",
    "A curious child always asks many questions.\n",
]
with open("data.txt","w+") as f:
    f.writelines(sentences)
    f.seek(0)
    content=f.read()
    
search=input("enter word for search:")
words=content.split()
if search in words:
    print("word found:",search)
else:
    print("Oops! Unavailable")

# #JSON FILE HANDLING:
student = {
    "name": "Achal Narwade",
    "roll_no": 101,
    "age": 19,
    "course": "B.Tech Computer Science",
    "subjects": ["Python", "Networking", "Cybersecurity", "Maths"],
    "grades": {
        "Python": "A",
        "Networking": "B+",
        "Cybersecurity": "A",
        "Maths": "B"
    }
}
# import json
# with open("student.json","x") as f:
#     pass
with open("student.json","w")as f:
    json.dump(student,f,indent=4)

with open("student.json","r")as f:
    variable=json.load(f)
print(variable)

#SIMPLE TO-DO LIST
# with open("todo.txt","x") as f:
#     pass
example=[
    "Finish Python homework\n",
    "Revise Networking notes\n",
    "Submit assignment on Google Classroom\n"
]
# with open("todo.txt","a")as file:
#     file.writelines(example)#append hai so bar bar hoga isiliye comment out

choice=input("what do you want? add/delete/view the task:")
match choice.lower():
    case "add":
        task=input("Enter the task to add:")
        with open("todo.txt","a")as file:
            file.write(task+"\n")
        print("Task added!")
    case "delete":
        with open("todo.txt","r+")as file:
            task=file.readlines()
        print("Tasks in file:")
        for i , t in enumerate(task,start=1):
            print(f"{i}. {t.strip()}")#strip removes newline
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(task):
            removed = task.pop(task_no -1)
            with open("todo.txt", "w") as file:  # overwrite file
                file.writelines(task)
            print(f"Removed task: {removed.strip()}")
        else:
            print("Invalid task number!")
    case "view":
        with open("todo.txt", "r") as file:
            content = file.read()
        print("Tasks:\n", content)
    case _:
        print("Invalid choice!")

