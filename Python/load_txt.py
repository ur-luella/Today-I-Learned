# encoding이 다른 경우 open할 때 encoding 옵션도 추가해주기
# 주로 'euc-kr'로 해결됨
with open('directory/file_name.txt', 'r') as f:
  lines = f.readlines()
