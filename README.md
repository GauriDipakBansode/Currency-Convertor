# Currency Converter Application (Python Tkinter)

## Overview

This project is a **GUI-based Currency Converter application** developed using **Python and Tkinter**. The application allows users to convert an amount from one currency to another using predefined exchange rates.

The interface is simple, user-friendly, and suitable for academic projects, internships, and beginner-level GUI demonstrations.

---

## Features

* Graphical User Interface using Tkinter
* Convert between multiple currencies
* Drop-down menus for currency selection
* Clear and Convert functionality
* Real-time conversion display

---

## Supported Currencies

* Rupees (INR)
* Dollar (USD)
* Euro (EUR)
* Yuan (CNY)
* Rand (ZAR)

---

## Technologies Used

* Python 3
* Tkinter (GUI framework)
* Variables (`StringVar`, `DoubleVar`)
* Conditional logic

---

## Project Structure

```
Currency-Converter/
│
├── currency_converter.py   # Main application file
├── README.md               # Project documentation
```

---

## How to Run the Application

### Prerequisites

* Python 3 installed on the system

### Run Command

```bash
python currency_converter.py
```

---

## Application Workflow

1. Enter the amount to be converted.
2. Select the source currency from the first drop-down.
3. Select the target currency from the second drop-down.
4. Click on the **Convert** button to get the result.
5. Click **Clear** to reset the fields.

---

## Code Logic Explanation

* Tkinter widgets are used to build the GUI (Label, Entry, Button, OptionMenu).
* Currency selections are handled using `StringVar`.
* Converted value is stored using `DoubleVar`.
* Conversion logic is implemented using nested conditional statements.
* Fixed exchange rates are used for simplicity.

---

## Learning Outcomes

* Understanding Tkinter GUI development
* Handling user input in GUI applications
* Using drop-down menus and variables
* Implementing real-world applications using Python

---

## Limitations

* Exchange rates are static and not real-time
* No error handling for invalid input
* Internet-based currency updates are not included

---

## Future Enhancements

* Real-time exchange rates using an API
* Input validation and error handling
* Improved UI layout and styling
* Support for more currencies

---

## Author

Gauri

---
