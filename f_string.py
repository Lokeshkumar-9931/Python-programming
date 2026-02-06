letter="hey my name is {0} and I am from {1}"  #formating
country="India"
name="Lokesh"
print(letter.format(name,country))
print(f"Hey my name is {name} and i am from {country}")
price=49.35312
text=f"my price is {price:.3f}"
print(text)
print(f"{2*30}")
print(type(f"{2*30}"))
print(f"Hey my name is {{{name}}} and i am from {{country}}")