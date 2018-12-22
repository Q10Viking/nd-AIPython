files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)

'''
8188
Traceback (most recent call last):
  File "d:/AI-Py/part02/scripting/example_6.py", line 3, in <module>
OSError: [Errno 24] Too many open files: 'some_file.txt'
'''