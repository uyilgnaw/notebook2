

'''
    选择排序是一种简单直接的排序算法。他的工作原理是每一次从待排序的数据元素中选出最小
    或最大的一个元素，存放在序列的起始位置，称为选择排序

'''

def selection_sort(arr):
    for i in range(len(arr) - 1): # 控制最外层循环次数

        min_index = i # 将第一个元素设为起始最小元素序号

        for j in range(i + 1,len(arr)): # 第二层循环将假设的最小元素与后面所有元素进行比较
            if arr[j] < arr[min_index]:# 如果假设最小元素序号的值不是最小
                min_index = j # 则更新最小元素的序号

        arr[min_index],arr[i] = arr[i],arr[min_index]# 将更新后的最小元素与假设最小元素位置互换

    return arr

if __name__ == '__main__':
    result = selection_sort([1,4,6,7,3,5,0])
    print(result)
