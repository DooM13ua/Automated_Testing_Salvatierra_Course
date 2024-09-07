# 01
name = "Bob"

print(f"Hello, {name}.")

name = "Rolf"

print(f"Hello, {name}.")

# 02
print("--------------------------------------------------")

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format("Rolf")

print(with_name)

#03
print("--------------------------------------------------")

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)