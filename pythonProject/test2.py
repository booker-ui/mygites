import os

l = []
for root, dirs, files in os.walk(r'F:\pythonProject'):
    for file in files:
        path = os.path.join(root, file)
        if os.path.getsize(path) >= 10 * 1024 :
            l.append(path)
print(l)
