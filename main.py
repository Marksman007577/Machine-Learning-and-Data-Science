import numpy as np

num_list = [[5, 10, 15], [20, 25, 30], [35, 40, 45]]

arr = np.array(num_list)
arr1 = arr[:2, :2]
arr2 = arr[1:3, :2]
arr3 = arr[:2, 1:3]
arr4 = arr[1:3, 1:3]
arr5 = np.sqrt(arr)
arr6 = np.log(arr)
arr7 = np.sum(arr, axis=0)
arr8 = np.sum(arr, axis=1)
print(arr)
print("")
print(arr1)
print("")
print(arr2)
print("")
print(arr3)
print("")
print(arr4)
print("")
print(arr5)
print("")
print(arr6)
print("")
print(arr7)
print("")
print(arr8)