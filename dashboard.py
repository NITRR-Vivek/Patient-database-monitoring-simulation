from welcome import welcome
import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Database connection details
host = 'localhost'
user = ''
password = ''
database = 'healthCareSystem'

def hello():
    welcome(show_text="Dashboard")
# dashboard.py

# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database='healthCareSystem'
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Function to fetch data from the database for the specified table
def fetch_data(table_name):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        conn.close()
        return data, cursor  # Return both data and cursor
    return None, None  # Return None for both data and cursor if connection fails
# Function to display statistics based on user selection
 

def display_statistics(data, cursor, columns, graph_type):
    if data:
        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
        # st.write(df)
        fig, ax = plt.subplots()

        try:
            x_axis = st.selectbox("Select X-Axis", columns)
            y_axis = st.selectbox("Select Y-Axis", columns)
        except KeyError:
            st.write("Error: Unable to retrieve column names.")

        # Display statistics based on user selection
        if graph_type == "Line Plot":
            ax.plot(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Line Plot")

        elif graph_type == "Bar Plot":
            ax.bar(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Bar Plot")
        elif graph_type == "Scatter Plot":
            ax.scatter(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Bar Plot")

        st.pyplot(fig) 
                  

def dash_main(userhost, user_id, user_pass):
    hello()
    global host, user, password
    host = userhost
    user = user_id
    password = user_pass
    
    tab_p, tab_d, tab_n, tab_a, tab_m = st.tabs(["Patient", "Doctor", "Nurse", "Appointment", "Medical Record"])
    
    data_p, cursor_p = fetch_data("Patient")
    data_d, cursor_d = fetch_data("Doctor")
    data_n, cursor_n = fetch_data("Nurse")
    data_a, cursor_a = fetch_data("Appointment")
    data_m, cursor_m = fetch_data("MedicalRecord")
    
    if tab_p:
        if data_p:
            df_p = pd.DataFrame(data_p, columns=[i[0] for i in cursor_p.description])
            tab_p.dataframe(df_p,use_container_width=True)
        else:
            tab_p.write("No data available.")
    if tab_d:
        if data_d:
            df_d = pd.DataFrame(data_d, columns=[i[0] for i in cursor_d.description])
            tab_d.dataframe(df_d,use_container_width=True)
        else:
            tab_d.write("No data available.")
    if tab_n:
        if data_n:
            df_n = pd.DataFrame(data_n, columns=[i[0] for i in cursor_n.description])
            tab_n.dataframe(df_n,use_container_width=True)
        else:
            tab_n.write("No data available.")
    if tab_a:
        if data_a:
            df_a = pd.DataFrame(data_a, columns=[i[0] for i in cursor_a.description])
            tab_a.dataframe(df_a,use_container_width=True)
        else:
            tab_a.write("No data available.")
    if tab_m:
        if data_m:
            df_m = pd.DataFrame(data_m, columns=[i[0] for i in cursor_m.description])
            tab_m.dataframe(df_m,use_container_width=True)
        else:
            tab_m.write("No data available.")
    st.markdown('---')        
    st.subheader("Patient Statistics...") 
    if data_p:
     try:
        columns_p = [i[0] for i in cursor_p.description]
        selected_columns_p = st.multiselect("Select Columns", columns_p, default=columns_p[:2])
        graph_type_p = st.radio("Select Graph Type", ["Line Plot", "Bar Plot","Scatter Plot"])
        try:
            display_statistics(data_p, cursor_p, selected_columns_p, graph_type_p)
        except:
            st.write("KeyError: No data found")    
     except TypeError:
        st.error("Cursor description is None. Cannot fetch column names.")
    else:
     st.write("No data available.")

      
