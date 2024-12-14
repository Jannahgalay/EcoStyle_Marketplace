FINAL PROJECT DOCUMENTATION
EcoStyle Marketplace
CS121: ADVANCED COMPUTER PROGRAMMING

Submitted By:
Galay, Jannah Mae G.
IT – 2106

Project Overview

The EcoStyle Marketplace is an online platform designed specifically for sellers of sustainable fashion, allowing them to easily register, manage, and showcase eco-friendly clothing, accessories and other eco-friendly things. With increasing consumer demand for sustainable and eco-conscious products, there is a growing need for a specialized platform that allows sellers to reach an audience interested in fashion that aligns with environmental values. This system solves the problem of fragmented marketplaces by providing a centralized, user-friendly platform where sellers can effectively list their products made from recyclable or environmentally friendly materials.
The system's primary goal is to create a digital space where sellers can seamlessly manage their product information, track inventory, and interact with their product listings, without the complexity of a traditional e-commerce platform. By focusing solely on sellers, this system enhances the ability of sustainable brands to grow their presence in the marketplace, empowering them to contribute to the global movement towards sustainable fashion.
System Boundaries:
Included Features:
Seller Registration & Authentication: The system allows new users to sign up and create an account. Existing users can log in using their credentials.
Product Management: Sellers can add new products, update existing ones, and delete products they no longer wish to list. Each product entry includes essential details such as product name, description, price, availability, and contact information.
Seller Dashboard: After logging in, sellers are presented with a dashboard to view their products and manage their listings. This includes a feature to view products, with an organized display of product details.
Error Handling and User Validation: To ensure data integrity, the system checks for missing or incorrect information during registration and product submission.
Excluded Features:
Buyer Interaction: This version of the system is solely focused on the seller's needs. It does not include any features for buyers, such as product searches, purchasing functionality, or order management.
Payment Processing: The platform does not handle financial transactions or integrate with payment gateways at this stage.
Shipping and Delivery Management: The system does not track shipments or manage delivery logistics, which will be handled separately by the sellers.
Target Users:
The primary users of the EcoStyle Marketplace are sellers who specialize in sustainable fashion, looking to list their eco-friendly products in a dedicated online marketplace. These sellers are typically individuals or small businesses that prioritize environmentally conscious fashion choices, including products made from recyclable or renewable materials. The platform caters specifically to those who want to reach an audience interested in sustainable fashion, offering them an easy-to-use space to manage and showcase their products. While the platform does not include features for buyers, it is designed to meet the needs of sellers by providing streamlined registration, product listing, and inventory management tools. 
Measurable Outcomes:
Specific: The goal is to create a platform where sellers can register, input, and manage eco-friendly products. The system will provide them with tools to efficiently update and track product listings.
Measurable: The system aims for a milestone where at least 100 active sellers have successfully registered and listed products within six months of launching the platform.
Achievable: The user interface is designed to be intuitive, requiring minimal technical knowledge from the sellers. Clear instructions, robust error handling, and simple forms will ensure that all users, regardless of technical skill, can use the platform effectively.
Relevant: The system aligns with the increasing global focus on sustainability in fashion. By providing a dedicated marketplace for eco-friendly fashion, the system will help sellers reach an audience that values sustainability and wants to make responsible fashion choices.
II. PYTHON CONCEPTS AND LIBRARIES

Tkinter is the standard Python interface to the Tk GUI (Graphical User Interface) toolkit. It is the most commonly used library for creating desktop applications with graphical interfaces in Python. Tkinter provides a wide range of widgets (like labels, buttons, text fields, etc.) that allow developers to design and implement interactive and visually appealing user interfaces. Tkinter is particularly well-suited for creating small to medium-sized applications where ease of use and rapid development are priorities. 
For example, in the EcoStyle Marketplace project, Tkinter is being used to build the graphical user interface (GUI) where sellers can input and view their information, making it a key component for the interactive features of the system.
Key Features of Tkinter:
Widgets: Tkinter provides various widgets such as buttons, labels, entry fields, frames, and listboxes that allow users to interact with the application.
Layouts: It supports different layout managers like pack(), grid(), and place() to control the arrangement of widgets within a window.
Event Handling: Tkinter allows users to bind actions to events such as mouse clicks or key presses. This helps create interactive applications.
Cross-Platform: Tkinter is available on Windows, macOS, and Linux, enabling developers to create cross-platform applications without modifying the code.
Customization: Tkinter allows for widget customization with properties like color, font, size, and style, providing flexibility in application design.

III. SUSTAINABLE DEVELOPMENT GOALS
Sustainable Development Goal12 (SDG12):  Ensure Sustainable consumption and production patterns.

The topic chosen in this project is Responsible consumption and production, it focuses on promoting the efficient use of resources, reducing environmental impact, and encouraging sustainable practices in both production and consumption. It integrated by creating an online marketplace for eco-friendly products such as bags and basket, allowing reducing waste and prograss the consumption with sustainability. It provides products using environmentally-friendly materials such as biodegradable plastics and recycled materials, along with a buying guide that informs users on responsible purchasing behavior in order to minimize environmental harm.

The project encourages sustainable products that are usable, recyclable, thus reducing the disposal of items and adhering to a circular economy principle whereby materials are reused  and waste is minimized. Also, the marketplace provides shelf inventory management to avoid overproduction by making sure that products are sold at an optimum pace. The project in general persuades consumers to consume more sustainably and it will contribute to SDG 12 by decreasing waste generation through prevention, recycling and reuse.

IV. PROGRAM/SYSTEM INSTRUCTIONS
Using the Application
The EcoStyle Marketplace is designed for sellers to input, view, and manage their product listings. Below are the instructions on how to interact with the application:
Login Screen:
Upon launching the application, you will be prompted to either Log In or Sign Up.
If you already have an account, select Log In and enter your Username and Password.
If you don’t have an account, click Sign Up and follow the prompts to create a new account.
Sign Up Process:
Enter a new Username, Password, and Confirm Password.
After successfully signing up, you will be logged into the system and can proceed to the Seller Information screen.
Seller Information Input:
On this screen, you will be asked to provide the following details about your product:
Seller Name
Location
Phone Number
Product Name
Product Description
Product Price
Availability (Stock Level)
After entering the required details, click the Submit Product button to add the product to the marketplace.
View Products:
Once you have added products, you can view them by selecting the View Products option.
The products will be displayed in a well-organized format, showing the seller’s name, location, phone number, product name, description, price, and availability.
Additional Options:
After submitting a product, you will be given the option to Add Another Product, View Products, or Exit the application.
You can continue to add products or exit the application when finished.
Error Handling and Validation
The application has built-in validation to ensure the data entered by the seller is accurate and complete. If any required fields are left empty, the system will display an error message asking the user to fill in the missing information.
Login Errors: If the username or password is incorrect, an error message will prompt the user to try again.
Sign Up Errors: If the username already exists or the passwords don’t match, an error message will notify the user.
Product Input Errors: If any fields are left blank when adding a product, the application will ask the user to fill all required fields before submitting the product.
Exiting the Application
To exit the application at any time, click the Exit button on any screen. This will close the application and terminate the program.
