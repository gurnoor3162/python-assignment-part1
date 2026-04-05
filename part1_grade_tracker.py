#task 1

raw_students = [
  {"name": "  AyesHa", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
  {"name": "ROhit", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
  {"name": " PriyA ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
  {"name": "KAran", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
  {"name": "SnEha", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
  name = student["name"].strip().title()
  roll = int(student["roll"])
  marks = [int(x.strip()) for x in student["marks_str"].split(",")]

  valid = True
  for part in name.split():
    if not part.isalpha():
      valid = False

  if valid:
    print(name, "- Valid name")
  else:
    print(name, "- Invalid name")

  print("================================")
  print("Student :", name)
  print("Roll No :", roll)
  print("Marks  :", marks)
  print("================================")

  cleaned_students.append({"name": name, "roll": roll, "marks": marks})

#printing name
for student in cleaned_students:
  if student["roll"] == 103:
    print(student["name"].upper())
    print(student["name"].lower())


#task2

student_name = "Ayesha"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

for i in range(len(subjects)):
  m = marks[i]

  if m >= 90:
    grade = "A+"
  elif m >= 80:
    grade = "A"
  elif m >= 70:
    grade = "B"
  elif m >= 60:
    grade = "C"
  else:
    grade = "F"

  print(subjects[i], ":", m, "->", grade)

total = sum(marks)
avg = round(total / len(marks), 2)

print("Total marks:", total)
print("Average marks:", avg)

max_mark = max(marks)
min_mark = min(marks)

print("Highest scoring subject:", subjects[marks.index(max_mark)], max_mark)
print("Lowest scoring subject:", subjects[marks.index(min_mark)], min_mark)


#while loop for new subjects
new_count = 0

while True:
  sub = input("Enter subject name (or 'done'): ")
  if sub == "done":
    break

  try:
    m = float(input("Enter marks: "))
    if m < 0 or m > 100:
      print("Invalid marks")
      continue
  except:
    print("Invalid input")
    continue

  subjects.append(sub)
  marks.append(m)
  new_count += 1

print("New subjects added:", new_count)

new_avg = round(sum(marks) / len(marks), 2)
print("Updated average:", new_avg)


#task3

class_data = [
  ("Ayesha", [88, 72, 95, 60, 78]),
  ("Rohit", [55, 68, 49, 72, 61]),
  ("Priya", [91, 85, 88, 94, 79]),
  ("Karan", [40, 55, 38, 62, 50]),
  ("Sneha", [75, 80, 70, 68, 85]),
]

results = []

print("\nName | Average | Status")
print("------------------------")

for name, marks in class_data:
  avg = round(sum(marks) / len(marks), 2)

  if avg >= 60:
    status = "Pass"
  else:
    status = "Fail"

  print(name, "|", avg, "|", status)
  results.append((name, avg, status))

passed = 0
failed = 0

for r in results:
  if r[2] == "Pass":
    passed += 1
  else:
    failed += 1

topper = results[0]
for r in results:
  if r[1] > topper[1]:
    topper = r

class_avg = round(sum([r[1] for r in results]) / len(results), 2)

print("Number passed:", passed)
print("Number failed:", failed)
print("Topper:", topper[0], topper[1])
print("Class average:", class_avg)


#task4

essay = " python is a versatile language. it is object oriented, functional, and procedural programming. python is widely used."

clean = essay.strip().lower()

print(clean.title())

count = clean.count("python")
print("Count:", count)

new_text = clean.replace("python", "Python")
print(new_text)

# split sentences
sentences = clean.split(". ")
print("Sentences list:", sentences)

for i in range(len(sentences)):
  s = sentences[i].strip()
  if not s.endswith("."):
    s += "."
  print(str(i+1) + ".", s)
