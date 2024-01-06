#  дано масив (лист)  [1, 43, 6, 22, 756]
# написать функцию, которая возвращает лист в обратном порядке

NAME = "pr3"

arr_1 = [1, 43, 6, 22, 756]

def revers_1 (arr):
    arr.reverse()
    return arr


def revers_2 (arr):
    temp = []
    for i in range (len(arr)-1, -1, -1):
        temp.append(arr[i])
    return temp

if __name__ == "__main__":
    print(revers_1(arr_1))
    print(revers_2(arr_1))