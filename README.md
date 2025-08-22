This project is designed to simulate the Cairo Metro system.
It contains several classes:
1. Metro class
This is the base class.
It stores data such as:
The metro line the passenger will take
The starting station
The destination station
The amount of money the passenger has
2. Prices class (inherits from Metro)
This class is responsible for calculating the ticket price.
It contains lists of stations for each metro line (El-Monib, Shubra El-Kheima, Helwan, El-Marg, Rod El-Farag Corridor, and Adly Mansour).
The code calculates the number of stations between the starting and destination stations, then determines the ticket price based on the distance:
Up to 8 stations → 8 EGP (Yellow ticket)
Up to 16 stations → 10 EGP (Green ticket)
Up to 23 stations → 15 EGP (Pink ticket)
Up to 39 stations → 20 EGP (Light blue ticket)
3. Buy_ticket class (inherits from Prices)
This class handles the actual ticket purchase.
It checks whether the passenger paid enough money or not.
If the passenger paid more than the required fare, it returns the change.
It also returns the type of ticket (based on its color).
Program Output
At the end, the code prints:
A welcome message: "Welcome to Cairo Metro System"
The calculated ticket price for the chosen trip
A message showing the ticket type and any change returned
Key Concepts
The project is built using Object-Oriented Programming (OOP).
It demonstrates inheritance and simulates a real-world metro system in a simple way.
