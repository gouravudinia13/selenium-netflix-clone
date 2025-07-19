# Selenium Netflix Clone Automation Testing

This project automates UI testing for a Netflix clone platform using **Selenium WebDriver** with **Pytest**.

## 🔍 Overview

The test suite validates core features of a Netflix-like OTT web platform. It ensures the functionality, UI consistency, and cross-browser compatibility of essential user flows such as login and subscription.

## 🧪 Features Tested

- ✅ **Login Functionality** — Verifies user login with valid and invalid credentials  
- ✅ **Subscription Process** — Automates the flow for selecting and confirming subscriptions  
- ✅ **Cross-Browser Testing** — Validated test runs on multiple browsers  
- ✅ **UI Consistency** — Checks element presence and visual behavior across pages  

## 🛠 Tech Stack

- **Selenium WebDriver**  
- **Pytest**  
- **Python 3.12**  
- **ChromeDriver**  

## 📁 Folder Structure

selenium_netflix_clone/
│
├── pages/ # Page Object Model classes
│ ├── login_page.py
│ └── subscription_page.py
│
├── tests/ # Test cases
│ ├── test_login.py
│ └── test_subscription.py
│
├── conftest.py # Pytest fixtures and setup
├── requirements.txt # Python dependencies

bash
Copy
Edit

## 🚀 Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/gouravudinia13/selenium-netflix-clone.git
   cd selenium-netflix-clone
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Run Tests

bash
Copy
Edit
pytest


✅ Test Output Sample
bash
Copy
Edit
============================= test session starts =============================
platform win32 -- Python 3.12.0, pytest-8.4.1
collected 4 items

tests/test_login.py ...                                               [75%]
tests/test_subscription.py .                                          [100%]

============================= 4 passed in 20.47s =============================