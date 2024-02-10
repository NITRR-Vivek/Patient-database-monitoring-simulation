import streamlit as st

def sql_help():
    st.write("MySQL Commands Reference")

    with st.expander("Basic Commands",expanded=True):
        st.write("**Selecting all rows from a table:**")
        st.code("SELECT * FROM table_name;", language="sql")

        st.write("**Selecting specific columns from a table:**")
        st.code("SELECT column1, column2 FROM table_name;", language="sql")
        
        # Add more basic commands here...

    with st.expander("Data Manipulation"):
        st.write("**Inserting data into a table:**")
        st.code('''INSERT INTO doctor(Name, Specialization, ContactNumber)
values ('Rahul','Kidney Specialist', '+919638527410');''', language="sql")

        st.write("**Updating data in a table:**")
        st.code("UPDATE table_name SET column1 = value1 WHERE condition;", language="sql")

        # Add more data manipulation commands here...

    with st.expander("Data Filtering"):
        st.write("**Filtering rows based on a condition:**")
        st.code("SELECT * FROM table_name WHERE condition;", language="sql")
        
        st.write("**Filtering rows based on a condition:**")
        st.code('''Select Count(Name) from patient;
SELECT COUNT(DISTINCT City) AS DistinctCityCount FROM patient;''', language="sql")

        st.write("**Sorting rows in ascending order:**")
        st.code("SELECT * FROM table_name ORDER BY column_name ASC;", language="sql")

    with st.expander("Joins"):
        st.write("**Inner Join:**")
        st.code("SELECT * FROM table1 INNER JOIN table2 ON table1.key = table2.key;", language="sql")

        st.write("**Left Join:**")
        st.code("SELECT * FROM table1 LEFT JOIN table2 ON table1.key = table2.key;", language="sql")

        # Add more join commands here...

    with st.expander("Aggregation Functions"):
        st.write("**Count the number of rows:**")
        st.code("SELECT COUNT(*) FROM table_name;", language="sql")

        st.write("**Calculate the average value:**")
        st.code("SELECT AVG(column_name) FROM table_name;", language="sql")
    with st.expander("Database Commands"):
        st.write("**Delete the whole database:**")
        st.code("DROP database healthcaresystem;", language="sql")

    

