import numpy as np

array = np.array([1.57,2.48,3.93,4.33])
print("\n array printed")
print(array)

print("\n np.ceil() function")
result = np.ceil(array)
print(result)

print("\n np.floor() function")
result = np.floor(array)
print(result)

print("\n np.round() function")
result = np.round(array)
print(result)

print("\n decimal place round()")
result = np.round(array, 1)
print(result)

print("\n sqrt() function")
result = np.sqrt(array)
print(result)

arr = np.arange(10)
print(arr)
print()

print("\n exp() function")
result = np.exp(arr)
print(result)

x = [5,4]
y = [6,3]

print("\n np.maximum() function")
result = np.maximum(x,y)
print(result)

print('-'* 50)

array1 = np.array(([-1.1,2.2,3.3,4.4]))
print("\n array1 printed")
print(array1)

array2 = np.array(([-1.1,2.2,3.3,4.4]))
print("\n array2 printed")
print(array2)

print("\n np.abs() function")
result = np.abs(array1)
print(result)

print("\n np.sum() function")
result = np.sum(array1)
print(result)

print("\n np.compare() function")
result = np.equal(array1, array2)
print(result)

print("\n np.sum() and np.equl() function")
print("\n True is 1, False is 0 counting")
result = np.sum(np.equal(array1, array2))
print(result)

print("\n average function")
result = np.mean(array2)
print(result)

arrX = np.array([[1,2],[3,4]], dtype= np.float64)
arrY = np.array([[5,6],[7,8]], dtype= np.float64)

print("\n arr of elements")

print("power")
print(arrX ** arrY)

print("square ")