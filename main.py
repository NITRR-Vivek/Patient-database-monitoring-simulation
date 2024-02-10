import streamlit as st
import mysql.connector
import pandas as pd
import os
import datetime
import mysql_help as sh
import generate_data as gd
import interface_input as inif
import dashboard as ds
from welcome import welcome,dash_image

from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("user")
PASS = os.getenv("password")
HOST = os.getenv("host")

st.set_page_config(
    page_title="PDBMSS",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state='expanded'
)

def connect_to_mysql(userid,userpass):
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=userid,
            password=userpass,
            database="healthcaresystem"
        )
        return connection
    except mysql.connector.Error as error:
        st.error(f"Failed to connect to MySQL: {error}")
        return None

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor
    except mysql.connector.Error as error:
        st.error(f"Failed to execute query: {error}")
        return None
    
def sql_commands(userid,userpass):
    st.header("MySQL Playground")
    connection = connect_to_mysql(userid=userid,userpass=userpass)
    # Perform CRUD operations
    command = st.text_area("Enter MySQL command:", height=100)
    if st.button("Execute"):
        st.markdown("---")
        if command:
            try:
                cursor = execute_query(connection, command)
                if cursor:
                    if command.lower().startswith(("select", "show")):
                        results = cursor.fetchall()
                        if results:
                            # Fetch column names from cursor's metadata
                            column_names = [col[0] for col in cursor.description]
                            # Create DataFrame
                            df = pd.DataFrame(results, columns=column_names)
                            st.dataframe(df)
                        else:
                            st.write("No results found.")
                    elif command.lower().startswith("describe"):
                        rows = cursor.fetchall()
                        if rows:
                            # Fetch column names from cursor's metadata
                            column_names = [col[0] for col in cursor.description]
                            # Create DataFrame
                            df = pd.DataFrame(rows, columns=column_names)
                            st.write(df)
                        else:
                            st.write("No results found.")
                    else:
                        if "insert" in command.lower() or "update" in command.lower() or "delete" in command.lower():
                            connection.commit()  # Commit changes
                        st.success("Command executed successfully")
            except mysql.connector.Error as error:
                st.error(f"Failed to execute query: {error}")
        else:
            st.warning("Please enter a MySQL command.")


# Function to check login credentials
def authenticate(user_id, user_pass):
    # Hardcoded credentials (replace with your authentication logic)
    if user_id == USER and user_pass == PASS:
        return True
    else:
        return False

# Define login function
def login():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    st.sidebar.title("Login")
    user_id = st.sidebar.text_input("User ID")
    user_pass = st.sidebar.text_input("Password", type="password")
    submit_button = st.sidebar.button("Submit")

    if submit_button:
        USER = user_id
        PASS = user_pass
        if authenticate(user_id, user_pass):
            st.session_state.logged_in = True
            st.sidebar.success("Login successful!")
            st.snow()
        else:
            st.sidebar.error("Invalid credentials")

def generate_data():
    st.title("Generate Synthetic Data and Insert into Database")
    gd.take_input(HOST,USER,PASS)
    

# Main function
def main():
    login()

    if not st.session_state.logged_in:
        welcome()
        dash_image()
        st.sidebar.error("❗Not Connected !")

    else:
        st.sidebar.success("✅Connected")
        st.sidebar.markdown("---")
        st.sidebar.title("Menu")

        if 'selected_option' not in st.session_state:
            st.session_state.selected_option = "Welcome Message"

        selected_option = st.sidebar.radio("Go to", ["Dashboard", "Generate Data","SQL Playground","Entry","SQL Help"])

        if selected_option == "Dashboard":
            ds.dash_main(HOST,USER,PASS)
        elif selected_option == "Generate Data":
            generate_data()
        elif selected_option== "SQL Playground":
            sql_commands(USER,PASS)    
        elif selected_option== "Entry":
            inif.main(HOST,USER,PASS) 
        elif selected_option== "SQL Help":
            sh.sql_help()  

if __name__ == "__main__":
    main()




 
 