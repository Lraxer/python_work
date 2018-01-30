class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(str(self.restaurant_name) + " is open now!")


restaurant_1 = {'name': 'lancoffee', 'cuisine_type': 'Italian'}
restaurant_2 = {'name': 'mancoffee', 'cuisine_type': 'Chinese'}
restaurant_3 = {'name': 'wancoffee', 'cuisine_type': 'French'}

restaurants = [restaurant_1, restaurant_2, restaurant_3]

for exam in restaurants:
    restaurant = Restaurant(exam['name'], exam['cuisine_type'])
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
