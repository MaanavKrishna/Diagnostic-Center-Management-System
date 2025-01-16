## 🏥 Diagnostic Center Management System
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

📦 Installation Guide

Step 1: Clone the Repository

    git clone https://github.com/MaanavKrishna/Diagnostic-Center-Management-System

Navigate into the project directory

    cd Diagnostic-Center-Management-System

Step 2: Install Dependencies

Install the required Python libraries:

    pip install mysql-connector-python tabulate

Step 3: Set Up the Database

	1.	Open your MySQL client and create a new database:

CREATE DATABASE GMS;

	2.	Tables (Doctor and Patient) are automatically created when the program is run for the first time.

Step 4: Run the Application

Run the script to start the system:

    python dcms.py


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

Here’s a markdown section detailing use cases for the Diagnostic Center Management System (DCMS):

🔍 Use Cases for DCMS

1️⃣ Efficient Doctor Management
	•	Add New Doctors: Easily add details of doctors, including their qualifications, medical license number, and assigned center.
	•	Update Records: Modify existing doctor information to keep your database accurate.
	•	Search Functionality: Find doctors based on their license number, name, or assigned center.
	•	Directory Management: Generate a directory of all doctors or filter by specific centers for quick reference.

2️⃣ Streamlined Patient Management
	•	Patient Registration: Quickly register new patients with complete details like test type, referred doctor, and contact information.
	•	Modify Records: Edit patient details as needed to reflect changes.
	•	Search for Patients: Retrieve patient data by registration number, name, or test date.
	•	Patient Directory: Generate reports for all patients or filter by test date/type for easy record-keeping.

3️⃣ Comprehensive Reporting
	•	Doctor Reports:
	•	View a full directory of doctors.
	•	Filter doctors based on the center they are assigned to.
	•	Patient Reports:
	•	Generate a complete list of patients.
	•	Filter patient data based on test type or test date.
	•	View fees collected for specific test types or patient groups.

4️⃣ Seamless User Roles
	•	Admin Role:
	•	Manage both doctors and patients with full control over adding, modifying, deleting, and generating reports.
	•	Doctor Role:
	•	Access to patient-related functionalities to ensure streamlined patient management.

5️⃣ Data Organization and Insights
	•	Centralized storage for all doctor and patient information.
	•	Clear and formatted tables for easy readability and data tracking.
	•	Insight into test trends, doctor assignments, and fees collected.

6️⃣ Customization and Scalability
	•	Add more features or modify existing ones to adapt to your diagnostic center’s unique needs.
	•	Scalable to accommodate an increasing number of patients and doctors.

This system ensures smooth operations, better data management, and a professional user experience for any diagnostic center! 😊

🛠️ Technologies Used
	•	Python: The core programming language.
	•	MySQL: For database operations.
	•	Tabulate: To display data in clean, tabular formats.

Elevate your diagnostic center’s efficiency with DCMS!
