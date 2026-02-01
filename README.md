# Weekday-Determination-System-using-Python-MySQL
This project is a console-based Weekday Determination System developed using Python and MySQL. The program takes a date as input (day, month, year) and calculates the exact weekday using mathematical logic.

# Weekday Determination System using Python & MySQL

A console-based Python project that determines the **day of the week** for a given date using date calculation logic.  
The program also **generates a report file** and **stores the result in a MySQL database** with a timestamp.

---

## 🚀 Features
- Takes date, month, and year as user input  
- Calculates the correct weekday (Sunday–Saturday)  
- Handles leap year logic accurately  
- Generates a detailed `.txt` report file  
- Stores date, weekday, and timestamp in MySQL database  
- Uses modular functions for better readability  

---

## 🛠 Technologies Used
- Python  
- MySQL  
- mysql-connector-python  
- File Handling  
- datetime module  

---

## 🔄 Workflow
1. User enters date, month, and year  
2. Program calculates:
   - Month code  
   - Century code  
   - Last two digits of year  
3. Weekday is determined using mathematical logic  
4. A report file is generated in `.txt` format  
5. Date details are inserted into MySQL database  

---

## 📄 Output Example (Text File)

WEEKDAY DETERMINATION REPORT

Given Date : 15.8.2024
Day : Thursday
Generated on : 2024-08-15 10:30:22


---

## 🗄 Database Structure

Create the following table in MySQL:

```sql
CREATE TABLE date_day (
    date VARCHAR(20),
    weekday VARCHAR(20),
    generated_time DATETIME
);
```
▶️ How to Run the Project
1️⃣ Install Dependency
pip install mysql-connector-python

2️⃣ Update Database Credentials

Edit the following section in the code:

host="localhost"
user="root"
password="YOUR_PASSWORD"
database="YOUR_DATABASE"
3️⃣ Run the Program
python weekday_finder.py
