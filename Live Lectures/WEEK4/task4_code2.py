from faker import Faker

fake = Faker()

names = []

for _ in range(100):
	names.append(fake.name())

for name in names:
	print(name);