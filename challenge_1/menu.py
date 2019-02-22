class MenuItem:
    def __init__(self, meal_number: int, meal_name: str, price : float, description: str, ingredients: list):
        self.meal_number = meal_number
        self.meal_name = meal_name
        self.price = price
        self.description = description
        self.ingredients = ingredients