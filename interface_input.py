# input.py

import streamlit as st
import mysql.connector

# Database connection details
host = 'localhost'
user = ''
password = ''
database = 'healthCareSystem'


# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Function to create Patient tab
def patient_tab():
    st.title("Patient Data")
    st.write("Enter patient details below:")

    # Patient form fields
    name = st.text_input("Name",placeholder="Patient's Name")
    dob = st.date_input("Date of Birth")
    gender = st.selectbox("Gender", ["Male", "Female"])
    city = st.text_input("City")
    contact_number = st.text_input("Contact Number",placeholder="+91 8888888888")

    # Submit button
    if st.button("Submit Patient Data"):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Patient (Name, DateOfBirth, Gender, City, ContactNumber) VALUES (%s, %s, %s, %s, %s)", (name, dob, gender, city, contact_number))
            conn.commit()
            conn.close()
            st.success("Patient data submitted successfully.")

# Function to create Doctor tab
def doctor_tab():
    st.title("Doctor Data")
    st.write("Enter doctor details below:")

    # Doctor form fields
    name = st.text_input("Name",placeholder="Doctor's Name")
    specialization = st.text_input("Specialization")
    contact_number = st.text_input("Contact Number",placeholder="+91 8888888888")
    salary = st.number_input("Salary", min_value=0, step=1000)

    # Submit button
    if st.button("Submit Doctor Data"):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Doctor (Name, Specialization, ContactNumber, Salary) VALUES (%s, %s, %s, %s)", (name, specialization, contact_number, salary))
            conn.commit()
            conn.close()
            st.success("Doctor data submitted successfully.")

# Function to create Nurse tab
def nurse_tab():
    st.title("Nurse Data")
    st.write("Enter nurse details below:")

    # Nurse form fields
    name = st.text_input("Name", placeholder="Nurse's name")
    department = st.text_input("Department")
    contact_number = st.text_input("Contact Number", placeholder="+91 8888888888")

    # Submit button
    if st.button("Submit Nurse Data"):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Nurse (Name, Department, ContactNumber) VALUES (%s, %s, %s)", (name, department, contact_number))
            conn.commit()
            conn.close()
            st.success("Nurse data submitted successfully.")

# Function to create Appointment tab
def appointment_tab():
    st.title("Appointment Data")
    st.write("Enter appointment details below:")

    # Appointment form fields
    date = st.date_input("Date")
    time = st.time_input("Time")
    location = st.text_input("Location")
    patient_id = st.number_input("Patient ID", min_value=1)
    doctor_id = st.number_input("Doctor ID", min_value=1)
    nurse_id = st.number_input("Nurse ID", min_value=1)

    # Submit button
    if st.button("Submit Appointment Data"):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Appointment (Date, Time, Location, PatientID, DoctorID, NurseID) VALUES (%s, %s, %s, %s, %s, %s)", (date, time, location, patient_id, doctor_id, nurse_id))
            conn.commit()
            conn.close()
            st.success("Appointment data submitted successfully.")

# Function to create Medical Record tab
def medical_record_tab():
    st.title("Medical Record Data")
    st.write("Enter medical record details below:")

    # Medical Record form fields
    date = st.date_input("Date")
    diagnosis = st.text_area("Diagnosis")
    prescription = st.text_area("Prescription")
    patient_id = st.number_input("Patient ID", min_value=1)

    # Submit button
    if st.button("Submit Medical Record Data"):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO MedicalRecord (Date, Diagnosis, Prescription, PatientID) VALUES (%s, %s, %s, %s)", (date, diagnosis, prescription, patient_id))
            conn.commit()
            conn.close()
            st.success("Medical record data submitted successfully.")

# Main function to create tabs
def main(userhost,user_id,user_pass):
    global host,user,password
    host = userhost
    user = user_id
    password = user_pass
    st.sidebar.title("Data Entry Tabs")
    tab_selection = st.sidebar.radio("Select Data Entry Tab", ("Patient", "Doctor", "Nurse", "Appointment", "Medical Record"))

    if tab_selection == "Patient":
        patient_tab()
    elif tab_selection == "Doctor":
        doctor_tab()
    elif tab_selection == "Nurse":
        nurse_tab()
    elif tab_selection == "Appointment":
        appointment_tab()
    elif tab_selection == "Medical Record":
        medical_record_tab()
