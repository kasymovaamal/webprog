num = [10, 20, 30, 40, 50]
num. append (60)
num.insert(1, 15)
num. remove(30)
num. reverse()
num.sort()
print (num)

print(num[:3])
print(num[-2:])
print(num[::-1])

student = {"name": "darina", "age": 18, "grade": "A"}
student ["subject"] = "Math"
student ["grade"] = "A+"
student. pop ("age" )
print(student.keys ())
print(student. values ())
print(student.items ())

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection (set2)
difference_set = set1.difference(set2)
print(union_set)
print(intersection_set)
print(difference_set)