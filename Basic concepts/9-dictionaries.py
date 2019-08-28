student={
    "name":"Ali",
    "age":"24",
    "location":"Karachi"
}



# Print whole dictionary
print(student)



# access items
# Method 1

x=student['name']
print(x)


# Method 2
y= student.get('age')
print(y)




# Change values
student["age"]="25"



# Add item
student["language"]="English"



# Access through for loop
for i in student:
    print(student[i])
    


# delete last key
student.pop("language")
   



# Print all key name
for i in student:
    print(i)
    




# remove item
del student["age"]

   




# print keys with values
for i,j in student.items():
    print(i,"=",j)



# remove whole dictionary 
del student




# nested dictinary
student={
    "s1":{
        "name":"Ali",
        "age":"24"
    },
    "s2":{
        "name":"Zafar",
        "age":"25"
    }
}
print(student)