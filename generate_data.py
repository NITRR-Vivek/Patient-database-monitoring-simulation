import streamlit as st
import pandas as pd
import os
import time
from faker import Faker
import random
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("user")
PASS = os.getenv("password")

def initialize_database(host, user, password):
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        # Create database if not exists
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS healthCareSystem;")
        cursor.execute("USE healthCareSystem;")

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patient (
                PatientID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                DateOfBirth DATE,
                Gender VARCHAR(10),
                City VARCHAR(255),
                ContactNumber VARCHAR(15)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctor (
                DoctorID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Specialization VARCHAR(255),
                ContactNumber VARCHAR(15),
                Salary INT
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Nurse (
                NurseID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Department VARCHAR(255),
                ContactNumber VARCHAR(15)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Appointment (
                AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
                Date DATE,
                Time TIME,
                Location VARCHAR(255),
                PatientID INT,
                DoctorID INT,
                NurseID INT,
                FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
                FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
                FOREIGN KEY (NurseID) REFERENCES Nurse(NurseID)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MedicalRecord (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                Date DATE,
                Diagnosis VARCHAR(255),
                Prescription VARCHAR(255),
                PatientID INT,
                FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()

        print("Database tables initialized successfully.")

    except mysql.connector.Error as e:
        print("Error initializing database tables:", e)

# Function to generate synthetic data for the Patient table
def generate_patient_data(num_rows):
    fake = Faker('en_IN')
    data = {
        'PatientID': list(range(1, num_rows + 1)),
        'Name': [fake.name() for _ in range(num_rows)],
        'DateOfBirth': [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(num_rows)],
        'Gender': [random.choice(['Male', 'Female']) for _ in range(num_rows)],
        'City': [fake.city() for _ in range(num_rows)],
        'ContactNumber': [fake.phone_number() for _ in range(num_rows)],
    }
    return pd.DataFrame(data)

# Function to insert data into Patient table
def insert_patient_data(conn, cursor, data):
    for index, row in data.iterrows():
        cursor.execute("INSERT INTO Patient (PatientID, Name, DateOfBirth, Gender, City, ContactNumber) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (row['PatientID'], row['Name'], row['DateOfBirth'], row['Gender'], row['City'], row['ContactNumber']))
    conn.commit()

# Function to generate synthetic data for the Doctor table
def generate_doctor_data(num_rows):
    fake = Faker('en_IN')
    data = {
        'DoctorID': list(range(1, num_rows + 1)),
        'Name': [fake.name() for _ in range(num_rows)],
        'Specialization': [fake.job().replace(',', ';') for _ in range(num_rows)],
        'ContactNumber': [fake.phone_number() for _ in range(num_rows)],
        'Salary': [fake.random_int(min=50000, max=150000) for _ in range(num_rows)],
    }
    return pd.DataFrame(data)

# Function to insert data into Doctor table
def insert_doctor_data(conn, cursor, data):
    for index, row in data.iterrows():
        cursor.execute("INSERT INTO Doctor (DoctorID, Name, Specialization, ContactNumber, Salary) VALUES (%s, %s, %s, %s, %s)", 
                        (row['DoctorID'], row['Name'], row['Specialization'], row['ContactNumber'], row['Salary']))
    conn.commit()

# Function to generate synthetic data for the Nurse table
def generate_nurse_data(num_rows):
    fake = Faker('en_IN')
    data = {
        'NurseID': list(range(1, num_rows + 1)),
        'Name': [fake.name() for _ in range(num_rows)],
        'Department': [fake.job().replace(',', ';') for _ in range(num_rows)],
        'ContactNumber': [fake.phone_number() for _ in range(num_rows)],
    }
    return pd.DataFrame(data)

# Function to insert data into Nurse table
def insert_nurse_data(conn, cursor, data):
    for index, row in data.iterrows():
        cursor.execute("INSERT INTO Nurse (NurseID, Name, Department, ContactNumber) VALUES (%s, %s, %s, %s)", 
                        (row['NurseID'], row['Name'], row['Department'], row['ContactNumber']))
    conn.commit()

# Function to generate synthetic data for the Appointment table
def generate_appointment_data(num_rows, num_patients, num_doctors, num_nurses):
    fake = Faker('en_IN')
    data = {
        'AppointmentID': list(range(1, num_rows + 1)),
        'Date': [fake.date_this_month() for _ in range(num_rows)],
        'Time': [fake.time() for _ in range(num_rows)],
        'Location': [fake.address().replace('\n', ' ').replace(',','') for _ in range(num_rows)],
        'PatientID': [random.randint(1, num_patients) for _ in range(num_rows)],
        'DoctorID': [random.randint(1, num_doctors) for _ in range(num_rows)],
        'NurseID': [random.randint(1, num_nurses) for _ in range(num_rows)],
    }
    return pd.DataFrame(data)

# Function to insert data into Appointment table
def insert_appointment_data(conn, cursor, data):
    for index, row in data.iterrows():
        cursor.execute("INSERT INTO Appointment (AppointmentID, Date, Time, Location, PatientID, DoctorID, NurseID) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                        (row['AppointmentID'], row['Date'], row['Time'], row['Location'], row['PatientID'], row['DoctorID'], row['NurseID']))
    conn.commit()

# Function to generate synthetic data for the Medical Record table
def generate_medical_record_data(num_rows, num_patients):
    fake = Faker('en_IN')
    data = {
        'RecordID': list(range(1, num_rows + 1)),
        'Date': [fake.date_this_month() for _ in range(num_rows)],
        'Diagnosis': [fake.sentence() for _ in range(num_rows)],
        'Prescription': [fake.sentence() for _ in range(num_rows)],
        'PatientID': [random.randint(1, num_patients) for _ in range(num_rows)],
    }
    return pd.DataFrame(data)

# Function to insert data into Medical Record table
def insert_medical_record_data(conn, cursor, data):
    for index, row in data.iterrows():
        cursor.execute("INSERT INTO MedicalRecord (RecordID, Date, Diagnosis, Prescription, PatientID) VALUES (%s, %s, %s, %s, %s)", 
                        (row['RecordID'], row['Date'], row['Diagnosis'], row['Prescription'], row['PatientID']))
    conn.commit()

# def get_last_id(cursor, table_name):
#     cursor.execute(f"SELECT MAX({table_name}ID) FROM {table_name}")
#     last_id = cursor.fetchone()[0]
#     return last_id if last_id else 0


# Main function to create Streamlit interface
def take_input(userhost,userid,userpass):
    initialize_database('localhost', 'yourusername', 'yourpassword')
    num_patients = st.number_input("Enter number of patients", min_value=1, step=1, value=25)
    num_doctors = st.number_input("Enter number of doctors", min_value=1, step=1, value=3)
    num_nurses = st.number_input("Enter number of nurses", min_value=1, step=1, value=5)
    num_appointments = st.number_input("Enter number of appointments", min_value=1, step=1, value=10)
    num_medical_records = st.number_input("Enter number of medical records", min_value=1, step=1, value=15)
    if st.button("Initialize",type='primary'):
        try:
            with st.spinner("Initializing...."):
                initialize_database(userhost,userid,userpass)
        except Exception as e:
            st.error(f"Error: {e}")    
    if st.button("Generate and Insert Data",type='secondary'):
        try:
            with st.spinner("Generating and inserting data..."):
                time.sleep(1)    
                conn = mysql.connector.connect(
                    host="localhost",
                    user=userid,
                    password=userpass,
                    database="healthcaresystem"
                )
                cursor = conn.cursor()
                patient_data = generate_patient_data(num_patients)
                time.sleep(1)

                insert_patient_data(conn, cursor, patient_data)
                doctor_data = generate_doctor_data(num_doctors)
                insert_doctor_data(conn, cursor, doctor_data)
                time.sleep(1)
                
                nurse_data = generate_nurse_data(num_nurses)
                insert_nurse_data(conn, cursor, nurse_data)
                time.sleep(1)
                
                appointment_data = generate_appointment_data(num_appointments, num_patients, num_doctors, num_nurses)
                insert_appointment_data(conn, cursor, appointment_data)
                time.sleep(1)
                
                medical_record_data = generate_medical_record_data(num_medical_records, num_patients)
                insert_medical_record_data(conn, cursor, medical_record_data)
                st.success("Data insertion successful!")
                time.sleep(2)
                conn.close()
        except Exception as e:
            st.error(f"Error: {e}")
         
    





