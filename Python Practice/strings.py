name = "mason eastman"
print(name.title())
print(name.upper())
print(name.lower())
f_name = "mason"
l_name = "eastman"
#f strings
full_name = f"{f_name} {l_name}"
print(full_name.title())
message = f"Hello, my name is {full_name.title()}"
print(message)

language = "  python  "
print(language, "before removing whitespace")
print(language.rstrip().lstrip(),"after removing whitespace before and after")

