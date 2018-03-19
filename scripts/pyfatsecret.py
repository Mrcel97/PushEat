from fatsecret import Fatsecret

fs = Fatsecret('fd1d348919f0451894bd32b2d3de6e5c', '1a36ce0def3949229b8c638dd5838383')

foods = fs.foods_search("Tacos")

print(foods)