```python
#9 �� ����� ������ �����, �������� ������ ��������� ���� �����
numbers = [1, 3, 4, 9, 10]
print(list(map(lambda x: x * x, numbers)))
#10 �� ����� ������ ���������, ��������, [(1, 1), (2, 3), (5, 3)]. ����� ��� �����, ������� ����������� ������ y = 5 * x - 2.
# �� ������ �������� ������� �� ����� ����� � ���������� �� ���� ����� �� ������ ��������� (0, 0)
coords = [(1, 1), (2, 2), (3, 3), (4, 4), (-1, -1), (-1, 5)]
result_square_distance = {point: point[0] ** 2 + point[1] ** 2 for point in coords if point[0] < 0 and point[1] < 0}
print(result_square_distance)
#11 �������� � ������� ��� ������ ����� �� 2 �� 27. �� ������ ������.
list_square = [x * x for x in range(2, 28) if x % 2 == 0]
print(list_square)
#12 �� ����� ������ �� ��������� ����� �� ���������. ����� ���������� �� ����� ��������� ����� �� ������ ��������� (0, 0) � ������ ��������
points = [(0, 2), (2, 2), (3, 4)]
max_distance = max(point for point in points)
print(max_distance)
#13 �� ����� ��� ������ ����� nums_first = [1, 2, 3, 5, 8] � nums_second = [2, 4, 8, 16, 32]. �������� ���� ���� � ������, [(3, -1), (6, -2), (11, -5), ...]
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
result_list = list(map(lambda x, y: (x + y, x - y), nums_first, nums_second))
print(result_list)
#14 �� ����� ������ ����� �� �����, ��������, ['43141', '32441', '431', '4154', '43121']. ����� ������ �������� ���� �����. ����� �������� ����� � ������ �� �����, �� ���� ������������ ������� ������ �����, �� ��� ������������� ��� ������ ��������.
array = ['43141', '32441', '4', '4154', '43121']
new_array = []
result_array = []
for i in range(len(array)):
    if int(array[i])**2 % 2 == 0:
        new_array.append(int(array[i]))
        result_list = list(map(lambda x: x * x, new_array))
print(result_list)
#15
input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""
new = input_str.split(',')
#new = input_str.split('\n')
key_name = new[0].split(',')
print(key_name)
```
