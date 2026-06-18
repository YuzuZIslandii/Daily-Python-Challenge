# ☕ OOP Coffee Machine Simulator (Day 02) - Part of Angela Yu's 100 Days of Code.

> **📝 Course Exercise Context:** The underlying class modules (`menu.py`, `coffee_maker.py`, `money_machine.py`) and their corresponding documentation were provided by Angela Yu as part of the course. My specific task and primary learning objective for this project was to practice **Object-Oriented Programming (OOP)** by reading the provided documentation, instantiating the objects, and writing the overarching control flow to connect them into a fully functional system.

## 📖 Project Overview
A Python-based command-line interface (CLI) application that simulates the logic of a real-world coffee machine. While functionally identical to the Day 01 project, this version has been entirely rebuilt from the ground up using **Object-Oriented Programming (OOP)** principles. Instead of relying on global dictionaries and procedural functions, this script acts as a central controller that instantiates and manages communication between pre-built, independent objects. 

## ✨ Key Features
* **Object-Oriented Architecture:** Utilizes independent classes (`Menu`, `CoffeeMaker`, `MoneyMachine`) to handle specific domains of the application, keeping the main script minimal and clean.
* **Encapsulated Logic:** Resource deduction and coin processing are handled internally by the respective objects; the main script simply triggers methods and passes return values.
* **Smart Control Flow:** Prioritizes hidden maintenance commands (`report`, `off`) and input validation before querying the menu system, preventing crashes or unavailable item errors.
* **Modular Design:** Demonstrates a plug-and-play approach, making the codebase highly scalable (e.g., adding a credit card reader would only require swapping the `MoneyMachine` module).

## 🧠 What I've Learned (Technical Takeaways)
* **OOP Paradigm:** Successfully shifting mindset from procedural logic to Object-Oriented Programming—understanding how to instantiate objects and interact with their attributes and methods.
* **Working with External Code:** Reading documentation and integrating pre-written class modules without modifying their internal code, simulating a real-world collaborative environment.
* **Control Flow Optimization:** Structuring `while` loops and cascading `if` statements correctly to prevent logical bugs (such as avoiding searching the menu for an "off" string).
* **DRY Principle (Don't Repeat Yourself):** Storing object method returns (like the selected drink object) into variables (`chosen_drink`) to eliminate redundant method calls and optimize performance.