student_records = {}

def add_student(name, age = {}, courses = []):
  if name in student_records:
    print(f"Student '{name}' alredy exists.")
  else:
    student_records[name]= {"age": age, "grades": set(), "courses": courses}

    print(f"Student '{name}' added successfully.")
    return student_records

def add_grade(name, grade):
  if name not in student_records:
    print(f"Student '{name}' not found.")
    return student_records
  else:
    student_records[name]["grades"].add(grade)
    print(f"Grade {grade} added for student '{name}'.")
    return student_records

def is_enrolled(name, course):
  if name not in student_records:
    print(f"Student '{name}' not found.")
    return False
  else:
    if course in student_records[name]["courses"]:
      return True
    else:
      return False

def calculate_average_grade(name):
  if name not in student_records:
    print(f"Student '{name}' not found.")
    return None
  else:
    if student_records[name]["grades"] == {}:
      return 0
    else:
      media = float(0)
      for elemento in student_records[name]["grades"]:
        media += elemento
      return (media/len(student_records[name]["grades"]))

def list_students_by_course(course):
  list_name = []
  for element in student_records:
    if course in student_records[element]["courses"]:
      list_name.append(element)
  return list_name

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
