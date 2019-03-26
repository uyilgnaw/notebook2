
'''
    插入排序的算法描述是一种简单直观的排序算法。他的工作原理是通过构建有序序列
    对于未排序数据，在已排序序列中从后向前小奥妙，找到相应位置并插入

'''

def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        pre_index = i - 1

        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index  -=1

        arr[pre_index + 1] = current
    return arr

if __name__ == '__main__':
    result = insertion_sort([1,5,0,32,2,6,8,4])
    print(result)