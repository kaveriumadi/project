d = {"name":"kavu", "age":22, "color":"orange", "year":1994}
print(d)

d["color"]="green"
print(d)

print(d["color"])

print(d["age"])

print(d.keys())

print(d.values())

print(d.items())

print(len(d))

d.popitem()
print(d)

d.pop("color")
print(d)

d["color"]="orange"
print(d)