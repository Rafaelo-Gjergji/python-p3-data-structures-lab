spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food_dict in spicy_foods:
        peppers = '🌶' * food_dict['heat_level']
        print(f"{food_dict['name']} ({food_dict['cuisine']}) | Heat Level: {peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            peppers = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")

def get_average_heat_level(spicy_foods):
    total = 0
    for food_dict in spicy_foods:
        total += food_dict['heat_level']
    return total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print("Names of Spicy Foods:", get_names(spicy_foods))
print("Spiciest Foods:", get_spiciest_foods(spicy_foods))
print("Printing All Spicy Foods:")
print_spicy_foods(spicy_foods)
print("Spicy Food by Cuisine:", get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print("Spiciest Foods:")
print_spiciest_foods(spicy_foods)
print("Average Heat Level:", get_average_heat_level(spicy_foods))
new_spicy_food = {"name": "Kimchi", "cuisine": "Korean", "heat_level": 7}
print("Updated Spicy Foods:", create_spicy_food(spicy_foods, new_spicy_food))