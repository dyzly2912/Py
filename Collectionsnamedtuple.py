from collections import namedtuple
N = int(input())
Student = namedtuple('Student', input().split())

all_mark = 0

for i in range(N):
    line = input().split()
    current_student = Student(*line)
    all_mark += int(current_student.MARKS)
print(f"{all_mark / N:.2f}")
