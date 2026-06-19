# 🧠 OOP Quiz Project (Day 17) - Part of Angela Yu's 100 Days of Code.

> **📝 Course Exercise Context:** Because this project serves as my foundational introduction to creating custom classes from scratch, the architecture and logic flow are heavily guided by Angela Yu's instructions. The focus of this milestone was not on writing completely novel system designs, but on mastering the syntax and structural patterns of defining custom types and managing object state in Python.

## 📖 Project Overview
A modular, object-oriented Quiz application executed via the command-line interface (CLI). The program dynamically processes a catalog of trivia data, converts raw structures into dedicated data objects, and utilizes a centralized manager class to handle game state, track user progression, validate answers, and maintain live score metrics.

## ✨ Key Features
* **Custom Class Blueprinting:** Built entirely around custom-defined models (`Question` and `QuizBrain`) rather than utilizing primitive nested dictionaries or external libraries.
* **State Management:** The `QuizBrain` controller encapsulates dynamic state variables (`score`, `question_number`) that evolve safely over the execution lifecycle.
* **Dynamic Input Validation:** Methods accept raw terminal inputs, handle case-insensitivity formatting automatically, and validate values against encapsulated data object properties.
* **Sandboxed Prototyping:** Includes a separate `randomexercises.py` environment exploring relational object logic (modeling social media mechanics like dynamic user follow/follower state mutations).

## 🧠 What I've Learned (Technical Takeaways)
* **Constructor Mechanics:** Mastering the `__init__` constructor method and the `self` keyword to securely initialize attributes when instantiating new objects.
* **Object-to-Object Interaction:** Implementing custom methods where an object can directly receive, read, and mutate the internal state parameters of another independent object instance.
* **Separation of Concerns:** Structuring an application across multiple modular files (`main.py`, `quiz_brain.py`, `question_model.py`, `data.py`) each retaining a single, clear architectural responsibility.
* **Lifecycle Flow Control:** Designing loop evaluations based on dynamic boolean method returns (`still_has_questions`) to cleanly drive program execution until data streams are exhausted.