import streamlit as st
import pandas as pd
import numpy as np
import os
import mysql.connector as mc
import matplotlib.pyplot as plt 
import time
import datetime
from PIL import Image
from io import StringIO
import cv2
import torch

st.set_page_config(
    page_title="PDBMSS",
    page_icon="🧊",
    layout="wide",
)

from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("user")
PASS = os.getenv("password")

st.title("**Streamlt App**")
st.header("Hello Bacho! ")
# df = pd.read_csv("doctor_data.csv")
# st.dataframe(df)
# st.metric("TCS Stock", value="3220.40", delta="19.10")

# df = pd.DataFrame(np.random.rand(10,2), columns=["prices","diff"])
# # st.table(df)
# st.dataframe(df)
# data = df.to_csv().encode("utf-8")
# st.download_button(
#     label="Download file",
#     data = data,
#     file_name="new_file.csv",
#     mime="text/csv"
# )

# file = open("robo.png","rb")
# btn = st.download_button(
#     label="Download image",
#     data= file,
#     file_name="robo.png",
#     mime="image/png"
# )

# Line Chart

# st.line_chart(df,y=["prices","diff"])
# st.area_chart(df)
# st.bar_chart(df)

# fig, ax = plt.subplots()
# # ax.scatter(np.arange(10),np.arange(10)**2)
# ax.hist(np.random.randn(100),bins=10)
# st.pyplot(fig)

# places = pd.DataFrame({
#     "lat": [19.07,28.64],
#     "lon" : [72.87, 77.21]
# })
# st.map(places)

# def fn():
#     st.write(time.time())

# pr = st.button("Click me", on_click=fn)
# st.write(pr)

# ck = st.checkbox("I agree to the terms and conditions",value=True)
# if ck == True:
#     st.button("Lets go")
# else:
#     st.warning("Please agree to the terms and conditions !")


# option = st.radio(
#     label="Order your food",
#     options=("pizza", "Burger", "Chips"),
#     index=1
# )
# if option == "pizza":
#     st.write("Pizza ordered !")
# elif option == "Burger":
#     st.write("Burger ordered !")  
# elif option == "Chips":
#     st.write("Chips Ordered !")  

# option = st.selectbox(
#     label= "Where do you live",
#     options= ("Moscow", "New York")
# )
# if option == "Moscow":
#     st.write("Moscow selected")
# elif option == "New York":
#     st.write("New York Selected! ")  

# option = st.multiselect(
#     placeholder="Select the places",
#     label="Which places have you been?",
#     options=("Sydney", "Tokyo","Paris","New Delhi"),
#     default=("Sydney", "Paris")
# )  
# st.write(option)

# num = st.slider(
#     label = "Your Age",
#     min_value= 18,
#     max_value= 120,
#     value=20,
#     step=1
# )
# st.write(num)

# num = st.slider(
#     label = "Your Salary Range",
#     min_value= 18000,
#     max_value= 120000,
#     value=(20000,60000),
#     step=1
# )
# st.write(num)

# num = st.slider(
#     label = "Appointment timing",
#     min_value= time(9,30),
#     max_value= time(14,30),
#     value=(time(11,30),time(12,45))
# )
# st.write(num)

# option = st.select_slider(
#     label = "Select the colour",
#     options=("Violet", "Indigo", "Blue","Green","Yellow","Orange","Red")
# )
# st.write(option)

# start_color, end_color = st.select_slider(
#     label="Select the color range",
#     options=("Violet", "Indigo", "Blue","Green","Yellow","Orange","Red"),
#     value=("Blue","Green")
# )
# st.write("From",start_color,"to",end_color)

# email = st.text_input(
#     label="Please Enter your Email",
#     max_chars= 25,
#     placeholder="Email Here",
#     type='default'
# )
# st.write(email)

# weight = st.number_input(
#     label="Enter your weight",
#     min_value=40,
#     max_value=120,
#     value=60,
#     step=1
# )
# st.write(weight)

# password = st.text_input(
#     label="Enter your Password",
#     max_chars= 25,
#     placeholder="Password",
#     type='password'
# )
# st.write(password)

# comment = st.text_area(
#     label="Enter any Comment",
#     height=100,
#     max_chars=100,
#     placeholder="Write here"
# )
# st.write(comment)

# date = st.date_input(
#     label="Enter your appointment date",
#     value=datetime.date(2024,4,11)
# )
# st.write(date)

# time = st.time_input(
#     "Enter your meet time",
#     value= datetime.time(14,00)
# )
# st.write(time)

# fl = st.file_uploader(
#     label="Upload here"
# )
# if fl:
#     st.write(fl.type)
#     if "image" in fl.type:
#        img = Image.open(fl) 
#        st.write(np.array(img).shape)
#     elif fl.type == "text/plain":
#         stringio = StringIO(fl.getvalue().decode("utf-8"))
#         string_data = stringio.read()
#         st.write(string_data)
                            
# picture = st.camera_input("Take a Pic")
# if picture:
#     img = Image.open(picture)
#     st.write(np.array(img).shape)
        
# color = st.color_picker("Pick a color")      
# if color:
#     st.write("You picked a color", color) 

# img = Image.open("robo.png")  # loading image with PIL uses RGB channels
# # img = cv2.imread('robo.png')  # loading image with cv2 uses BGR channels
# st.image(
#     img,
#     caption="Image of an astronaut robot",
#     width=400,
#     channels="RGB"
# )

# st.audio("audio.mp4", start_time= 10)

# st.video("video.mp4")

# Layout elements, Sidebars, Columns, Tabs, Expanders, and Container

# choice = st.sidebar.radio(
#     label="Choose the option",
#     options=("audio","video")
# )
# if choice == "audio":
#     st.write("This is audio")
# if choice == "video":
#     st.write("This is video")

# col1,col2 = st.columns(2, gap="small")
# col1.write("This is column1")
# col2.write("This is column2")


# exp = st.expander("See Pic")
# exp.write("Image of an astronaut robo")
# exp.image("robo.png", width=400)

# cont = st.container()
# cont.write("One")
# st.write("Two")
# cont.write("Three")

# txt = "% completed"
# my_bar = st.progress(0, text=txt)
# for pr in range(100):
#     time.sleep(0.1)
#     my_bar.progress(pr +1 , text=txt)

# with st.spinner("wait for it..."):
#     time.sleep(5)
# st.write("wait over")  

# st.balloons()  

# st.snow()

# st.error("This is an error message ! ")
# st.warning("Warning message !")
# st.info("Some Information.")
# st.success("Successful")

# e = RuntimeError("Exp")
# st.exception(e)

# Add HTML and JavaScript for a basic animation
# st.markdown("""
#     <style>
#         #animated-text {
#             font-size: 36px;
#             animation: color-change 2s infinite alternate;
#         }
#         @keyframes color-change {
#             from {color: blue;}
#             to {color: red;}
#         }
#     </style>
#     <div id="animated-text">Hello, Streamlit!</div>
#     <script>
#         // JavaScript for animation control (optional)
#         // You can use JavaScript to control more complex animations
#     </script>
# """, unsafe_allow_html=True)

# email = st.text_input("Enter email")
# if not email:
#     st.warning("Enter your Email Please...")
#     st.stop()
# st.success("Go ahead")    

# Form
# form = st.form("Basic Info")
# name = form.text_input("Name")
# age = form.slider("Age", min_value=18, max_value=120, step=1)
# date = form.date_input("Birthday", value=datetime.date(2024,1,1))
# submitted = form.form_submit_button("Submit")
# if submitted:
#     if name.strip() == '':
#         st.error('Name cannot be empty!')
#     elif date is None:
#         st.error('Date cannot be empty!')
#     else:
#         st.success('Form submitted successfully!')
#         st.write(f'Name: {name}')
#         st.write(f'Date: {date}')
#         st.write(f'Age: {age}')

# def sum(a, b):
#     return a+b
# with st.echo():
#     def mult(a, b):
#         return a * b
#     a = 10
#     b = 20
#     su = sum(a,b)
#     mu = mult(a,b)
#     st.write(su,mu)
# st.write("This is outside")  

# st.help(mc)  

# df1 = pd.DataFrame(
#     np.random.randn(10,2),
#     columns = ["col1","col2"]
# )
# my_table = st.table(df1)

# df2 = pd.DataFrame(
#     np.random.randn(1,2),
#     columns = ["col1","col2"]
# )
# my_table.add_rows(df2)
# my_chart = st.line_chart(df1)
# # my_chart.add_rows(df2)
# for i in range(5):
#     time.sleep(1)
#     df2 = pd.DataFrame(
#         np.random.randn(1,2),
#         columns=["col1","col2"]
#     )
#     my_chart.add_rows(df2)

# st.session_state
# if "key" not in st.session_state:
#     st.session_state["key"] = 1
# st.session_state  
# if "key" in st.session_state:
#     st.session_state["key"]=32
#     del st.session_state["key"]  
# st.session_state

# for k in st.session_state.keys():
#     del st.session_state[k]
# st.session_state 

# st.session_state
# st.text_input("Name", key="name")
# st.session_state   

# Callbacks
# def form_callback():
#     st.write(st.session_state["my_slider"])
#     st.write(st.session_state["my_checkbox"])

# with st.form(key = "my_form"):
#     slider_input = st.slider("My slider",0,15,5,key="my_slider")
#     checkbox_input = st.checkbox("Yes or No", key = "my_checkbox")
#     submit_button = st.form_submit_button("Submit", on_click=form_callback)

# Cache
# @st.cache_resource
# def load_model(args):   # args should remains same all throughout
#     st.write(st.write(time.time()))
#     model = Net()
#     checkpoints = torch.load(r"D:\\Path_to_model")
#     model.load_state_dict(checkpoints["model_state"])
#     return model

# model = load_model(data)

# @st.cache_data
# def inference(data):
#     st.write(time.time())
#     return model(torch.Tensor(data))
# model = load_model(input)








