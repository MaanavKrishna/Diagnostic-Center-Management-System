# 🏥 Diagnostic Center Management System
Welcome to the Diagnostic Center Management System! This Python-powered application is your go-to solution for managing the day-to-day operations of a diagnostic center with ease and efficiency. From handling doctor and patient records to generating insightful reports, this system is designed to bring structure and simplicity to your healthcare operations. 💡

✨ Key Features

👩‍⚕️ Doctor Management
	•	🩺 Add new doctors with details like name, title, gender, qualifications, contact information, and medical license number.
	•	✍️ Modify existing doctor records to ensure up-to-date information.
	•	🔎 Search for doctors by license number, center ID, name, or contact details.
	•	🗑️ Delete doctor records when no longer needed.

🧑‍🔬 Patient Management
	•	🩻 Add patient records, including details like name, test type (e.g., X-ray, MRI), referred doctor, and test date.
	•	📝 Modify patient records to reflect changes in test details or personal information.
	•	🔍 Search for patients by registration number, name, or contact details.
	•	🚮 Delete outdated patient records.

📊 Reports and Insights
	•	📋 Generate comprehensive reports for doctors by center or as a full directory.
	•	🏥 Create patient reports filtered by test type, test date, or as a complete directory.

📌 How to Use
	Step 1:Clone the Repository

    git clone https://github.com/your-username/diagnostic-center-management.git
  Navigate into the project directory
       
    cd diagnostic-center-management

  Step 2: Set Up the Database
	•	Install MySQL and create a database named Scancentre.
	•	Update the database credentials in the script (host, user, passwd).
	•	Run the script to automatically create necessary tables if they don’t exist.
	3.	Run the Program
      
    python diagnostic_center.py
    
  Step 4:Explore the Features
	  •	Admin Menu: Access complete management features.
	  •	Doctor Menu: Focus on patient operations and generate reports.

🛠️ Technologies Used
	•	Python: Core programming language for logic and functionality.
	•	MySQL: Robust database for managing data.
	•	Tabulate: For displaying data in easy-to-read table formats.

🌟 Example Reports

Doctor Directory 📑

+------------+-------+--------+------------+---------------+--------+-----------+---------+----------------+--------------------+
| Name       | Title | Gender | DOB        | Qualification | MLNO   | Center_ID | Address | Contact_Number | Email_ID          |
+------------+-------+--------+------------+---------------+--------+-----------+---------+----------------+--------------------+
| Dr. Smith  | MD    | Male   | 1980-05-12 | Cardiology    | 123456 | 1         | ...     | 9876543210     | smith@domain.com  |
+------------+-------+--------+------------+---------------+--------+-----------+---------+----------------+--------------------+

Patient Directory 🩺

+---------------------+-------------------+------+-------+------------+---------+----------------+----------------+------------+--------------+-------------+
| Registration_Number | Registration_Date | Name | Gender | DOB        | Address | Contact_Number | Referred_By    | Test_Date  | Test_Type   | Doctor_Name | Fee         |
+---------------------+-------------------+------+-------+------------+---------+----------------+----------------+------------+--------------+-------------+
| 101                 | 2023-12-01       | John | Male   | 1990-04-15 | ...     | 9876543210     | Dr. Smith      | 2023-12-05 | MRI Scan    | Dr. Smith   | 5000        |
+---------------------+-------------------+------+-------+------------+---------+----------------+----------------+------------+--------------+-------------+

🧑‍💻 Contributing

Feel free to contribute by raising issues or submitting pull requests. Let’s improve this system together! 🚀

📬 Contact

Have questions? Reach out at your-email@example.com.

Let the Diagnostic Center Management System make your healthcare operations stress-free and efficient! 🎉
