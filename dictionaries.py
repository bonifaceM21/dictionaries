print('python dictionaries')
car={
"brand":"ford",
"model":"mustang",
"year":1964
}
print(car)

if"model"in car:
  print("yes,'model'is one of the keys in this dict dictionary")
 
car["year"]=2018
print(car)

car["color"]=["blue","pink","yellow","red"]
print(car)

car.pop("model")
print(car)
car.popitem()
print(car)
del car["model"]
print(car)

for brand in car:
  print(brand)
for year in car.values():
  print (year)
