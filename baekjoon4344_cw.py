case_num = input()
case_num = int(case_num)

for i in range(case_num):
  info = input()
  info = info.split()
  
  student_num = int(info[0])
  score_list = list(map(int, info[1:]))
  avg = sum(score_list)/student_num
  count = 0
  for score in score_list:
    if score > avg:
      count += 1
  print(f'{count/student_num*100:.3f}%')