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


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Deve retornar 87.5
print(calculate_average_grade("Bob"))  # Deve retornar 75.0
print(calculate_average_grade("Charlie"))  # Aluno inexistente, deve imprimir a mensagem e retornar None
print(calculate_average_grade("Alice"))  # Deve retornar 87.5 novamente
