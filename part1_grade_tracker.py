#task1
raw_students = [
  {"name": " ayesha SHARMA ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
  {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
  {"name": " Priya Nair ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
  {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
  {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned = []

for s in raw_students:
  name = s["name"].strip().title()
  roll = int(s["roll"])
  marks = [int(x.strip()) for x in s["marks_str"].split(",")]

  # check valid name
  valid = True
  for part in name.split():
    if not part.isalpha():
      valid = False

  if valid:
    print("Valid name")
  else:
    print("Invalid name")

  print("==============================")
  print(f"Student : {name}")
  print(f"Roll No : {roll}")
  print(f"Marks   : {marks}")
  print("==============================")

  cleaned.append({"name": name, "roll": roll, "marks": marks})

# print for roll 103
for s in cleaned:
  if s["roll"] == 103:
    print(s["name"].upper())
    print(s["name"].lower())


#task2
student_name = "Ayesha Sharma"
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
  ("Ayesha Sharma", [88, 72, 95, 60, 78]),
  ("Rohit Verma", [55, 68, 49, 72, 61]),
  ("Priya Nair", [91, 85, 88, 94, 79]),
  ("Karan Mehta", [40, 55, 38, 62, 50]),
  ("Sneha Pillai", [75, 80, 70, 68, 85]),
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
essay = " python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used."

clean = essay.strip().lower()

print(clean.title())

count = clean.count("python")
print("Count:", count)

new_text = clean.replace("python", "Python 🐍")
print(new_text)

sentences = clean.split(". ")

for i in range(len(sentences)):
  s = sentences[i].strip()
  if not s.endswith("."):
    s += "."
  print(str(i+1) + ".", s)
