class Seller:
    def __init__(self, name, location, phone, product, description, availability, price):
        self.name = name
        self.location = location
        self.phone = phone
        self.product = product
        self.description = description
        self.availability = availability
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Phone: {self.phone}")
        print(f"Product: {self.product}")
        print(f"Description: {self.description}")
        print(f"Availability: {self.availability}")
        print(f"Price: ${self.price}")
        print("=" * 40)
