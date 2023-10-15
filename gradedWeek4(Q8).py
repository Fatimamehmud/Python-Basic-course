# that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!


output="a"*35
print(output)

output = ""
#or
for i in range(35):
    output = output + 'a'

print(" '\'"+output+"'\'" )
