# 🏥 Diagnostic Center Management System
Welcome to the Diagnostic Center Management System (DCMS), a Python-powered solution designed to streamline the operations of a diagnostic center. This system offers seamless management of doctors, patients, and essential reports, ensuring efficient record-keeping and improved organizational workflows.

🚀 Features
	•	Doctor Management
	•	Add, modify, delete, and search for doctor records.
	•	Maintain detailed records including name, title, gender, qualifications, and contact information.
	•	Patient Management
	•	Effortlessly handle patient records with options to add, modify, delete, or search.
	•	Track test types, dates, referred doctors, and registration information.
	•	Reporting
	•	Generate insightful reports for doctors and patients.
	•	Focused reports such as doctors by center or patients by test type.
	•	User Roles
	•	Dedicated admin functionalities.
	•	Simplified doctor menu with patient operations and reports.

🛠️ Usage

1. Clone the Repository

       git clone https://github.com/your-repo/diagnostic-center-management-system.git

Navigate into the project directory

    cd diagnostic-center-management-system

2. Set Up MySQL Database
	•	Ensure MySQL is installed on your system.
	•	Create a database named Scancentre using the following command:

CREATE DATABASE Scancentre;



3. Install Required Libraries
	•	Install the necessary Python packages:

pip install mysql-connector-python tabulate



4. Run the Program
	•	Start the application by executing:

python dcms.py



5. Follow the Menus
	•	Navigate through the interactive menus to manage doctors, patients, and generate reports.

📋 Example Reports

Doctor Directory

| Name      | Title        | Gender | DOB        | Qualification | MLNO  | Center_ID | Address           | Contact_Number | Email_ID            |
|-----------|--------------|--------|------------|---------------|-------|-----------|-------------------|----------------|---------------------|
| Dr. John  | Cardiologist | Male   | 1975-05-12 | MD            | 12345 | 1         | 123 Heart Lane    | 1234567890     | john@health.com     |
| Dr. Sarah | Radiologist  | Female | 1980-02-18 | MBBS          | 67890 | 2         | 456 Care Street   | 9876543210     | sarah@care.com      |

Patients by Test Type

| Registration_Number | Name      | Test_Date   | Test_Type   | Doctor_Name | Fee  |
|---------------------|-----------|-------------|-------------|-------------|------|
| 101                 | Alice     | 2023-12-15  | X-ray       | Dr. John    | 500  |
| 102                 | Bob       | 2023-12-16  | MRI Scan    | Dr. Sarah   | 2000 |

💡 Why Choose DCMS?
	1.	Intuitive Interface: Simple, interactive menus for hassle-free management.
	2.	Scalable Design: Adaptable to centers of any size.
	3.	Powerful Reports: Get valuable insights with a few keystrokes.
	4.	Secure Database Integration: Robust MySQL backend for reliable data storage.

🛠️ Technologies Used
	•	Python: The core programming language.
	•	MySQL: For database operations.
	•	Tabulate: To display data in clean, tabular formats.

Elevate your diagnostic center’s efficiency with DCMS!
