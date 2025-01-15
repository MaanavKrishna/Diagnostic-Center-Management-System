import mysql.connector,tabulate

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("USE DCMS")

def checktableexists(tablename):
    mycursor.execute("SHOW TABLES LIKE %s", (tablename,))
    rec1 = mycursor.fetchone()
    return rec1

def doctor():
    if checktableexists("doctor"):
        pass
    else:
        mycursor.execute("CREATE TABLE doctor(Name VARCHAR(20), Title VARCHAR(20), Gender VARCHAR(20), DOB DATE, Qualification VARCHAR(20), MLNO INT, Center_ID INT, Address VARCHAR(40), Contact_Number INT, Email_ID VARCHAR(40));")

def patient():
    if checktableexists("patient"):
        pass
    else:
        mycursor.execute("CREATE TABLE patient(Registration_Number INT, Registration_Date DATE, Name VARCHAR(20), Gender VARCHAR(20), DOB DATE, Address VARCHAR(40), Contact_Number INT, Referred_By VARCHAR(30), Test_Date DATE, Test_Type VARCHAR(20), Doctor_Name VARCHAR(20), Fee INT);")

def adddoctor():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        name = input("Enter Name:")
        title = input("Enter Title:")
        gender = input("Enter Gender:")
        dob = input("Enter Date Of Birth(YY/MM/DD):")
        qualification = input("Enter Qualification:")
        mlno = int(input("Enter Medical License No.:"))
        centerid = int(input("Enter Center_ID:"))
        address = input("Enter Address:")
        contact_no = int(input("Enter Contact_Number:"))
        emailid = input("Enter EmailID:")
        mycursor.execute("INSERT INTO doctor VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, title, gender, dob, qualification, mlno, centerid, address, contact_no, emailid))
        mydb.commit()

def addpatient():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        reno = int(input("Enter Registration Number:"))
        reda = input("Enter Registration Date(YY/MM/DD):")
        name = input("Enter Name:")
        gender = input("Enter Gender:")
        dob = input("Enter Date Of Birth(YY/MM/DD):")
        address = input("Enter Address:")
        contact_no = int(input("Enter Contact_Number:"))
        ref = input("Enter Referred By:")
        teda = input("Enter Test Date(YY/MM/DD):")
        while True:
            tety = input("Enter Test Type(X-ray/ECG/CT Scan/MRI Scan/Cardiac CT):")
            if tety in ["X-ray", "ECG", "MRI Scan", "Cardiac CT"]:
                break
            else:
                print("Not a valid Option:")
        docname = input("Enter Doctor Name:")
        fee = int(input("Enter Fee"))
        mycursor.execute("INSERT INTO patient VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (reno, reda, name, gender, dob, address, contact_no, ref, teda, tety, docname, fee))
        mydb.commit()

def modify(tablename):
    tarfie = input("Enter Field to be modified:")
    if tablename == "doctor":
        if tarfie in ["Name", "Title", "Gender", "DOB", "Qualification", "MLNO", "Center_ID", "Address", "Contact_Number", "Email_ID"]:
            tarval = int(input("Enter Medical License No.:"))
            chanval = eval(input("Enter New Value:"))
            mycursor.execute("UPDATE %s SET %s=%s WHERE %s=%s" % (tablename, tarfie, chanval, "MLNO", tarval))
            mydb.commit()
        else:
            print("Field Does not Exist")
    else:
        if tarfie in ["Registration_Number", "Registration_Date", "Name", "Gender", "DOB", "Address", "Contact_Number", "Referred_By", "Test_Date", "Test_Type", "Doctor_Name", "Fee"]:
            tarval = int(input("Enter Registration_Number:"))
            chanval = eval(input("Enter New Value:"))
            mycursor.execute("UPDATE %s SET %s=%s WHERE %s=%s" % (tablename, tarfie, chanval, "Registration_Number", tarval))
            mydb.commit()
        else:
            print("Field Does not Exist")

def delete(tablename):
    if tablename == "doctor":
        mlno = int(input("Enter Medical License No.:"))
        mycursor.execute("DELETE FROM %s WHERE MLNO=%s" % (tablename, mlno))
        mydb.commit()
    else:
        reno = int(input("Enter Registration_Number:"))
        mycursor.execute("DELETE FROM %s WHERE Registration_Number=%s" % (tablename, reno))
        mydb.commit()

def search(tablename):
    if tablename == "doctor":
        ch = int(input("Search Using\n1.Medical License No.\n2.Center Id\n3.Doctor Name\n4.Contact Number\nOption:"))
        if ch == 1:
            mlno = int(input("Enter Medical License No.:"))
            mycursor.execute("SELECT * FROM doctor WHERE MLNO=%s", (mlno,))
        elif ch == 2:
            ceid = int(input("Enter Center ID:"))
            mycursor.execute("SELECT * FROM doctor WHERE Center_ID=%s", (ceid,))
        elif ch == 3:
            docname = int(input("Enter Doctor Name:"))
            mycursor.execute("SELECT * FROM doctor WHERE Name=%s", (docname,))
        elif ch == 4:
            cono = input("Enter Contact Number:")
            mycursor.execute("SELECT * FROM doctor WHERE Contact_Number=%s", (cono,))
        header = ["Name", "Title", "Gender", "DOB", "Qualification", "MLNO", "Center_ID", "Address", "Contact_Number", "Email_ID"]
    else:
        ch = int(input("Search Using\n1.Registration Number\n2.Patient Name\n3.Contact Number\nOption:"))
        if ch == 1:
            reno = int(input("Enter Registration Number:"))
            mycursor.execute("SELECT * FROM patient WHERE Registration_Number=%s", (reno,))
        elif ch == 2:
            paname = input("Enter Patient Name:")
            mycursor.execute("SELECT * FROM patient WHERE Name=%s", (paname,))
        elif ch == 3:
            cono = input("Enter Patient Name:")
            mycursor.execute("SELECT * FROM patient WHERE Contact_Number=%s", (cono,))
        header = ["Registration_Number", "Registration_Date", "Name", "Gender", "DOB", "Address", "Contact_Number", "Referred_By", "Test_Date", "Test_Type", "Doctor_Name", "Fee"]
    rec = mycursor.fetchall()
    print(tabulate.tabulate(rec, header, tablefmt="grid"))

def docger():
    ch = int(input("Doctor Report\n1.Doctor Directory\n2.Doctors by Center\nOption:"))
    if ch == 1:
        mycursor.execute("SELECT * FROM doctor")
    elif ch == 2:
        ceid = int(input("Enter Center ID:"))
        mycursor.execute("SELECT * FROM doctor WHERE Center_ID=%s", (ceid,))
    rec = mycursor.fetchall()
    header = ["Name", "Title", "Gender", "DOB", "Qualification", "MLNO", "Center_ID", "Address", "Contact_Number", "Email_ID"]
    print(tabulate.tabulate(rec, header, tablefmt="grid"))

def patger():
    ch = int(input("Patient Report\n1.Patient Directory\n2.Patients by Test Date\n3.Patients by Test Type\nOption:"))
    if ch == 1:
        mycursor.execute("SELECT * FROM patient")
    elif ch == 2:
        teda = input("Enter Test Date(YY/MM/DD):")
        mycursor.execute("SELECT * FROM patient WHERE Test_Date=%s", (teda,))
    elif ch == 3:
        while True:
            tety = input("Enter Test Type(X-ray/ECG/CT Scan/MRI Scan/Cardiac CT):")
            if tety in ["X-ray", "ECG", "MRI Scan", "Cardiac CT"]:
                break
            else:
                print("Not a valid Option:")
        mycursor.execute("SELECT * FROM patient WHERE Test_Type=%s", (tety,))
    rec = mycursor.fetchall()
    header = ["Name", "Title", "Gender", "DOB", "Qualification", "MLNO", "Center_ID", "Address", "Contact_Number", "Email_ID"]
    print(tabulate.tabulate(rec, header, tablefmt="grid"))
          
def ger(user): 
    if user == "admin":
        ch = int(input("\nReport Menu\n\t1.Doctor\n\t2.Patient\nOption:"))
        if ch == 1:
            docger()
        elif ch == 2:
            patger()
        else:
            print("Option does not exist")
    else:
        patger()

def admin():
    while True:
        ch = int(input("\nAdmin Menu\n\t1.Doctor\n\t2.Patient\n\t3.Report\n\t4.Exit\nOption:"))
        if ch == 1:
            doctor()
            opt = int(input("\nDoctor Menu\n\t1.Add\n\t2.Modify\n\t3.Search\n\t4.Delete\nOption:"))
            if opt == 1:
                adddoctor()
            elif opt == 2:
                modify("doctor")
            elif opt == 3:
                search("doctor")
            elif opt == 4:
                delete("doctor")
            else:
                print("Option does not exist")
        elif ch == 2:
            patient()
            opt = int(input("\nPatient Menu\n\t1.Add\n\t2.Modify\n\t3.Search\n\t4.Delete\nOption:"))
            if opt == 1:
                addpatient()
            elif opt == 2:
                modify("patient")
            elif opt == 3:
                search("patient")
            elif opt == 4:
                delete("patient")
            else:
                print("Option does not exist")
        elif ch == 3:
            ger("admin")
        elif ch == 4:
            break
        else:
            print("Option does not exist")

def docmenu():
    while True:
        ch = int(input("\nDoctor Menu\n\t1.Patient Operations\n\t2.Report\n\t3.Exit\nOption:"))
        if ch == 1:
            opt = int(input("\nPatient Menu\n\t1.Add\n\t2.Modify\n\t3.Search\n\t4.Delete\nOption:")) 
            if opt == 1:
                addpatient()
            elif opt == 2:
                modify("patient")
            elif opt == 3:
                search("patient")
            elif opt == 4:
                delete("patient")
            else:
                print("Option does not exist")
        elif ch == 2:
            ger("user")
        elif ch == 3:
            break
        else:
            print("Option does not exist")

while True:
    op = int(input("--------" * 7 + "Diagnostic Center Management System" + "--------" * 7 + "\n\nWelcome To Diagnostic Center Management System\n\nMain Menu\n\t1.Admin\n\t2.Doctor\n\t3.Exit\nOption:"))
    if op == 1:
        admin()
    elif op == 2:
        docmenu()
    elif op == 3:
        break
    else:
        print("Option does not exist")