from collections.abc import Iterable

my_list = [num for num in range(0, 20)]
print("0~19까지의 정수값을 세팅한다.")
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print("\nListData 의 myList 를 loop 로 직접 순회하며 홀수들을 삭제한다.")
for num in my_list:
    if num % 2 != 0:
        my_list.remove(num)

print(my_list)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

my_list = [num for num in range(0, 20)]
print("\n0~19까지의 정수값을 세팅한다.")
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print("\nListData 의 myList 를 loop 로 직접 순회하지 않고 홀수들을 삭제한다.")
my_set = {*my_list}
del_set = {*my_list[1::2]}
my_set.difference_update(del_set)
print([*my_set])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print("\n삭제한 홀수들을 내림차순으로 출력한다.")
print(sorted([*del_set], reverse=True))  # [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

print("\n삭제한 홀수들을 별도로 저장한 후. 해당 자료구조에서 다시 삭제하면 원본의 자료구조에서는 해당 값이 다시 생성된다.")


def move(start, target, element):
    # element가 iterable이면 update, not iterable이면 remove & add?
    if isinstance(element, Iterable):
        target.update(set(start))
        start.difference_update(set(element))
    else:
        start.remove(element)
        target.add(element)


move(start=del_set, target=my_set, element=19)
print(del_set)  # {1, 3, 5, 7, 9, 11, 13, 15, 17}
print(my_set)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19}

move(start=del_set, target=my_set, element=del_set)
print(del_set)  # set()
print(my_set)  # {0, 2, 4, 6, 8, 9, 10, 7, 12, 5, 14, 1, 16, 3, 18, 19, 11, 13, 15, 17}
