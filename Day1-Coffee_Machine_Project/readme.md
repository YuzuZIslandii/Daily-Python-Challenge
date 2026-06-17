# ☕ Coffee Machine Simulator (Day 15)

## 📖 Project Overview
A Python-based command-line interface (CLI) application that simulates the logic of a real-world coffee machine. The program manages internal resources, processes financial transactions, and serves different types of coffee based on user input and available ingredients.
Project requirements were given by Angela Yu's 100 Days of Code challenge.

## ✨ Key Features
* **Resource Management:** Real-time tracking of water, milk, coffee beans, and money.
* **Transaction System:** Processes US coins (quarters, dimes, nickles, pennies), checks against item cost, and dispenses accurate change rounded to two decimal places.
* **State Maintenance:** Blocks transactions if machine ingredients are insufficient, returning refunds automatically.
* **Service Commands:** Includes hidden maintenance inputs (`report` to print current resource levels and `off` for safe system shutdown).

## 🧠 What I've Learned (Technical Takeaways)
* **Nested Data Structures:** Navigating and extracting data from multi-level dictionaries (handling the complex `MENU` catalog).
* **State Mutation:** Safely updating global state variables (machine resources) based on isolated function logic without breaking the system.
* **Code Optimization & Refactoring:** Eliminating redundant code by replacing unnecessary `for` loops with clean mathematical equations and ensuring functions have a single responsibility.
* **Business Logic Implementation:** Translating a strict set of business requirements (client specification) into a 100% compliant, functional script.