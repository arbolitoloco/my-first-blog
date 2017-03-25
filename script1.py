# print("Oi, DjangoGirls!")

# if 3 < 2:
# 	print("Funciona!!!")
# else:
# 	print("3 ao é menor do que 2")

# name = "Sonja"
# if name == "Ola":
# 	print("Hey Ola!")
# elif name == "Sonja":
# 	print("Hey Sonja")
# else:
# 	print("Hey Anonymous")

# def hi():
# 	print("Hi there")
# 	print("How are you?")

def hi(name):
	print("Hi " + name + "!")

hi("Laura")

girls=["Rachel", "Monica", "Phoebe", "Ola", "You"]

for name in girls:
	hi(name)
	print("Next girl")

for i in range(1, 6):
	print(i)
