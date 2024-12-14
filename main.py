import tkinter as tk
from tkinter import messagebox

class EcoStyleMarketplaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoStyle Marketplace")
        self.root.geometry("600x600")
        self.root.config(bg="#2a2a2a")

        self.products = []  # List to store product information
        self.users = {}  # Dictionary to store user data (username: password)
        self.current_user = None  # The logged-in user

        # For now, we initialize with one example user (this would be handled better with a database)
        self.users["user"] = "pass"

        # Start with the first screen to ask login or sign-up
        self.show_start_screen()

    def show_start_screen(self):
        self.clear_window()

        # Start Screen Title
        welcome_label = tk.Label(self.root, text="Welcome to EcoStyle Marketplace!!", font=("Helvetica", 20, "bold"), bg="#2a2a2a", fg="#FFFFFF")
        welcome_label.pack(pady=40)

        # Buttons for Login or Sign Up
        login_button = tk.Button(self.root, text="Log In", font=("Helvetica", 14), bg="#4C9A2A", fg="white", command=self.show_login_screen, relief="solid", bd=3, width=20)
        login_button.pack(pady=20)

        sign_up_button = tk.Button(self.root, text="Sign Up", font=("Helvetica", 14), bg="#8B4513", fg="white", command=self.show_sign_up_screen, relief="solid", bd=3, width=20)
        sign_up_button.pack(pady=10)

    def show_login_screen(self):
        self.clear_window()

        # Login Title
        login_title_label = tk.Label(self.root, text="Login", font=("Helvetica", 20, "bold"), bg="#2a2a2a", fg="#FFFFFF")
        login_title_label.pack(pady=40)

        # Username Entry
        self.username_label = tk.Label(self.root, text="Username:", font=("Helvetica", 14), bg="#2a2a2a", fg="#FFFFFF")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.username_entry.pack(pady=5)

        # Password Entry
        self.password_label = tk.Label(self.root, text="Password:", font=("Helvetica", 14), bg="#2a2a2a", fg="#FFFFFF")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*", width=30)
        self.password_entry.pack(pady=5)

        # Login Button
        login_button = tk.Button(self.root, text="Login", font=("Helvetica", 14), bg="#4C9A2A", fg="white", command=self.login, relief="solid", bd=3, width=20)
        login_button.pack(pady=20)

        # Back Button
        back_button = tk.Button(self.root, text="Back", font=("Helvetica", 14), bg="#FF6347", fg="white", command=self.show_start_screen, relief="solid", bd=3, width=20)
        back_button.pack(pady=10)

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username in self.users and self.users[entered_username] == entered_password:
            self.current_user = entered_username
            self.show_seller_info_screen()
        else:
            messagebox.showerror("Login Error", "Invalid Username or Password!")

    def show_sign_up_screen(self):
        self.clear_window()

        # Sign Up Title
        sign_up_title_label = tk.Label(self.root, text="Sign Up", font=("Helvetica", 20, "bold"), bg="#2a2a2a", fg="#FFFFFF")
        sign_up_title_label.pack(pady=40)

        # New Username Entry
        self.new_username_label = tk.Label(self.root, text="New Username:", font=("Helvetica", 14), bg="#2a2a2a", fg="#FFFFFF")
        self.new_username_label.pack(pady=5)
        self.new_username_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.new_username_entry.pack(pady=5)

        # New Password Entry
        self.new_password_label = tk.Label(self.root, text="New Password:", font=("Helvetica", 14), bg="#2a2a2a", fg="#FFFFFF")
        self.new_password_label.pack(pady=5)
        self.new_password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*", width=30)
        self.new_password_entry.pack(pady=5)

        # Confirm Password Entry
        self.confirm_password_label = tk.Label(self.root, text="Confirm Password:", font=("Helvetica", 14), bg="#2a2a2a", fg="#FFFFFF")
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*", width=30)
        self.confirm_password_entry.pack(pady=5)

        # Sign Up Button
        sign_up_button = tk.Button(self.root, text="Sign Up", font=("Helvetica", 14), bg="#4C9A2A", fg="white", command=self.sign_up, relief="solid", bd=3, width=20)
        sign_up_button.pack(pady=20)

        # Back Button
        back_button = tk.Button(self.root, text="Back", font=("Helvetica", 14), bg="#FF6347", fg="white", command=self.show_start_screen, relief="solid", bd=3, width=20)
        back_button.pack(pady=10)

    def sign_up(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_username in self.users:
            messagebox.showerror("Sign Up Error", "Username already exists!")
            return

        if new_password != confirm_password:
            messagebox.showerror("Sign Up Error", "Passwords do not match!")
            return

        # Save the new user credentials
        self.users[new_username] = new_password
        messagebox.showinfo("Sign Up Success", f"User {new_username} successfully created!")
        self.current_user = new_username
        self.show_seller_info_screen()

    def show_seller_info_screen(self):
        self.clear_window()

        # Seller Info Title
        title_label = tk.Label(self.root, text="Enter Seller Information", font=("Helvetica", 20, "bold"), bg="#4C9A2A", fg="white")
        title_label.pack(pady=20)

        # Seller's Name Entry
        self.name_label = tk.Label(self.root, text="Seller's Name:", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.name_entry.pack(pady=5)

        # Seller's Location Entry
        self.location_label = tk.Label(self.root, text="Location:", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.location_label.pack(pady=5)
        self.location_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.location_entry.pack(pady=5)

        # Seller's Phone Number Entry
        self.phone_label = tk.Label(self.root, text="Phone Number:", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.phone_entry.pack(pady=5)

        # Product Name Entry
        self.product_name_label = tk.Label(self.root, text="Product Name:", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.product_name_label.pack(pady=5)
        self.product_name_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.product_name_entry.pack(pady=5)

        # Product Description Entry
        self.description_label = tk.Label(self.root, text="Product Description:", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.description_entry.pack(pady=5)

        # Product Price Entry
        self.price_label = tk.Label(self.root, text="Product Price (P):", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.price_label.pack(pady=5)
        self.price_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.price_entry.pack(pady=5)

        # Product Availability Entry
        self.availability_label = tk.Label(self.root, text="Availability (In stock):", font=("Helvetica", 14), bg="#4C9A2A", fg="white")
        self.availability_label.pack(pady=5)
        self.availability_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.availability_entry.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(self.root, text="Submit Product", font=("Helvetica", 14), bg="#8B4513", fg="white", command=self.submit_product_info, relief="solid", bd=3, width=20)
        submit_button.pack(pady=20)

    def submit_product_info(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        phone = self.phone_entry.get()
        product_name = self.product_name_entry.get()
        description = self.description_entry.get()
        price = self.price_entry.get()
        availability = self.availability_entry.get()

        # Check for empty fields
        if not all([name, location, phone, product_name, description, price, availability]):
            messagebox.showerror("Input Error", "Please enter all required information.")
            return

        # Add product to the list
        product = {
            "seller_name": name,
            "location": location,
            "phone": phone,
            "product_name": product_name,
            "description": description,
            "price": price,
            "availability": availability
        }
        self.products.append(product)

        messagebox.showinfo("Product Added", "Product has been successfully added!")
        self.show_next_option_screen()

    def show_next_option_screen(self):
        self.clear_window()

        # Next Option Title
        next_option_title_label = tk.Label(self.root, text="What would you like to do next?", font=("Helvetica", 20, "bold"), bg="#4C9A2A", fg="white")
        next_option_title_label.pack(pady=40)

        # Option Buttons
        add_another_button = tk.Button(self.root, text="Add Another Product", font=("Helvetica", 14), bg="#4C9A2A", fg="white", command=self.show_seller_info_screen, relief="solid", bd=3, width=20)
        add_another_button.pack(pady=10)

        view_products_button = tk.Button(self.root, text="View Products", font=("Helvetica", 14), bg="#8B4513", fg="white", command=self.show_products_screen, relief="solid", bd=3, width=20)
        view_products_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", font=("Helvetica", 14), bg="#FF6347", fg="white", command=self.root.quit, relief="solid", bd=3, width=20)
        exit_button.pack(pady=10)

    def show_products_screen(self):
        self.clear_window()

        # Products Title
        products_title_label = tk.Label(self.root, text="Products List", font=("Helvetica", 20, "bold"), bg="#4C9A2A", fg="white")
        products_title_label.pack(pady=20)

        # List of Products
        if self.products:
            for product in self.products:
                product_info = f"Seller: {product['seller_name']}\nLocation: {product['location']}\nPhone: {product['phone']}\nProduct: {product['product_name']}\nDescription: {product['description']}\nPrice: ${product['price']}\nAvailability: {product['availability']}\n"
                product_label = tk.Label(self.root, text=product_info, font=("Helvetica", 12), bg="#2a2a2a", fg="#FFFFFF", anchor="w", justify="left")
                product_label.pack(pady=10, padx=20)
        else:
            message_label = tk.Label(self.root, text="No products added yet.", font=("Helvetica", 14), bg="#2a2a2a", fg="#FFFFFF")
            message_label.pack(pady=20)

        # Back Button
        back_button = tk.Button(self.root, text="Back", font=("Helvetica", 14), bg="#FF6347", fg="white", command=self.show_next_option_screen, relief="solid", bd=3, width=20)
        back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = EcoStyleMarketplaceApp(root)
    root.mainloop()
