# Python Mini Project - Cafe Management App
This is a **command-line interface(CLI)** app developed in Python to manage **products**,**Orders** and **Couriers**.It simulates real-world CRUD operations(Create,Read,Update,Delete) and introduces data persistence using files.

Each week, new functionality was added:
- **Week 1:** Product creation with basic menu navigation.
- **Week 2:** Order status management and refinement.
- **Week 3:** Courier management and file persistence for all menus.
- **Week 4:** Unit testing
- **Week 5:** Connect to loacl database
- **Week 6:** Refactored final code 

## 📌 Client Requirements

The client is a newly launched **pop-up café** operating in a busy business district. Their goal is to efficiently manage orders, products, and delivery couriers for their growing customer base. The application should be a **command-line interface (CLI)** program that evolves over time to meet increasing business needs. Below are the core requirements:

### 📦 Product & Courier Management
- Maintain a dynamic collection of **products** (e.g., homemade lunches, beverages).
- Maintain a list of **couriers** to handle deliveries.
- Enable users to **create**, **read**, **update**, and **delete** product and courier records.

### 📑 Order Management
- Accept **new customer orders** and assign couriers and products.
- Track and **update the order status** (e.g., _preparing_, _out-for-delivery_, _delivered_).
- Support a **status table** in the database to allow easy status changes and scalability.

### 💾 Data Persistence
- Ensure data is **not lost between sessions** by progressively storing it using:
  - `.txt` files (initial implementation)
  - `.csv` files (structured intermediate format)
  - **Relational database (SQL)** – final version supports all CRUD operations using database tables.

### 📋 Technical & UI Requirements
- The app must run in the **command-line interface (CLI)**.
- Display **main and nested menus** with clear options.
- Allow smooth **navigation and exit** between menus.
- Handle **invalid or blank inputs** gracefully without crashing the app.

### ✅ Testing & Quality Assurance
- Implement **unit testing** using Python's built-in test framework to verify functionality and reliability.
- Maintain **clean, refactored code** following Python best practices (PEP8).

### 📊 Bonus Features (Stretch Goals)
- Display orders **filtered by courier or status**.
- Manage a list of **customers** with CRUD operations.
- Track **product inventory** levels.
- Support **import/export of data** using CSV format.
- Provide **data visualizations** using Jupyter Notebook and Matplotlib to help the client analyze business trends.

### 🔄 Software Lifecycle
- The project is delivered iteratively over **6 weeks**, with weekly updates based on newly introduced concepts and features.
- Emphasizes an **agile methodology**—continuous improvement through weekly increments.
- Each week's work builds upon the foundation of previous weeks.


  ## ▶️ Steps to Run

1. **Clone or Download** the repository to your local machine.

2. Each week's version of the project is organized into separate folders:
   - [week1](https://github.com/PrajaktaBade/mini_project_gen/tree/main/mini-project/week1/sources/app_w1.py) – Product Management with basic menu navigation
   - [week2](https://github.com/PrajaktaBade/mini_project_gen/tree/main/mini-project/week2/sources/app_w2.py) – Added Order Management and order status tracking
   - [week3](https://github.com/PrajaktaBade/mini_project_gen/tree/main/mini-project/week3/sources/app_w3.py) – Introduced Courier Management and data persistence using CSV files
   - [week4](https://github.com/PrajaktaBade/mini_project_gen/tree/main/mini-project/week4/sources/app_w4.py) - Refactored code to use dictionaries and CSV files.Introduced unit testing to check correctness of functions.
   - [week5](https://github.com/PrajaktaBade/mini_project_gen/tree/main/mini-project/week5/sources/app_w5.py) - Refactored the code to connect with a local database and store data in the corresponding database tables.
   - [week6](https://github.com/PrajaktaBade/mini_project_gen/tree/main/mini-project/week6/sources/final_app.py) - Refactored code to use order_status table separately and added file handling
3. Navigate into the folder for the version you want to run. For example:
   ```bash
   cd week3
   ```
4. For **Week 3**, ensure the following CSV files exist in the same directory as `app.py`:
   - `products.csv`
   - `couriers.csv`
   - `orders.csv`

   *(If these files are missing, create them manually or let the app create them automatically when you add new records.)*

5. Run the application:
   ```bash
   python3 app_w*.py /python3 final_app.py(for last week 6)
   ```

6. Follow the **menu-driven interface** to manage:
   - Products
   - Couriers
   - Orders 

7. Upon exiting, all data is **automatically saved** to the CSV files listed above till week 4 and then to the local database tables.



## 🧪 How to Run Unit Tests (with pytest)

Unit tests for this project are located in the [**Week 4**](https://github.com/DE-X6-LM/Prajakta-portfolio/tree/main/mini-project/week4/sources) folder and use the `pytest` framework.

### 🔧 Prerequisites:
Make sure `pytest` is installed. You can install it using pip:

```bash
pip install pytest
```

### ▶️ Running Tests:

1. Open your terminal or command prompt.
2. Navigate to the Week 4 folder:

```bash
cd(path to project)/week4

3. Run all tests:

```bash
pytest
```

4. To run tests with detailed output (recommended during debugging):

```bash
pytest -v -s
```

5. To run a specific test file:

```bash
pytest test_filename.py
```

### ✅ Notes:
- Test files should be named like `test_*.py`.
- Function names inside tests should begin with `test_`.

---

These tests validate core functionalities such as adding, updating, and deleting products, couriers, and orders, ensuring the code remains reliable after each refactor.
