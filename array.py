import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr1)
# #
# # import numpy as np
# # arr2 = np.array(42)
# # print(arr2)
# #
# # import numpy as np
# arr3 = np.array([1, 2, 3, 4, 5, 6, 7])
# # print(arr3)
# #
# # import numpy as np
# arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# # print(arr4)
#
# import numpy as np
# arr5 = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]])
# print(arr5)
# print(arr1[0])
# print(arr1[2])
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print("2nd element of 1st row:",arr[0,1])
# print("5nd element of 2nd row:",arr[1,4])
# print(arr3[1:5])
# print(arr3[:4])
# print(arr4[0:1,0:2])
arr5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr5)
print(arr5[0,:])
print(arr5[:,0])
print(arr5[0,:2])
print(arr5[0:,:2])
print(arr5[0:,1:3])
print(arr5[0:,2:4])
print(arr5[1:,3:])