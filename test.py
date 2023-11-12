import ctypes


# 定义结构体
class MyStructure(ctypes.Structure):
    _fields_ = [
        ('field1', ctypes.c_int),
        ('field2', ctypes.c_float),
        ('field3', ctypes.c_char_p)
    ]


# 创建结构体数组
my_array = (MyStructure * 3)()

# 为数组元素赋值  
my_array[0].field1 = 123
my_array[1].field2 = 3.14
my_array[2].field3 = b"Hello"

# 打印数组内容  
for i in range(3):
    print("Element", i)
    print("field1:", my_array[i].field1)
    print("field2:", my_array[i].field2)
    print("field3:", my_array[i].field3)