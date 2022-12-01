d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
print(d1['id'])
print(d2)
print(d3)
print(d4)
print(d5)
print(d1['name'])
print(len(d1))
for item in d1.items():
    print(item[0],item[1])
for key, value in d1.items():
    print(key, value)
for key in d2:
    print(key)
for value in d2.values():
    print(value)
d1.clear()
print(d1)
d6=d3.copy()
print(d6)
for key,value in d6.items():
    print(key,value)
# d5.fromkeys()
print(d4.get("name"))
print(d2.get('i', 1940))
print(d5.items())
print(d2)
print(d2.pop('name'))
print(d2)
print(d3.values())
print(d3.keys())


