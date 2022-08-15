name = "Bob"
name2 = "Jhon"
greeting = "Hello, {}"
greeting2 = "Hello, {} {}"

with_name = greeting.format(name)
with_name2 = greeting2.format(name, name2)

print(with_name2)