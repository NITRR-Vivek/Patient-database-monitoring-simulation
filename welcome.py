import streamlit as st
from PIL import Image

def welcome(show_text="Welcome!"):
    # st.subheader("**Welcome,**")
    st.markdown(f"""
        <style>
            #animated-text {{
                font-size: 40px;
                font-weight: bold;
                font-family: Arial, sans-serif;
                animation: color-change 2s infinite alternate;
            }}
            @keyframes color-change {{
                from {{color: blue;}}
                to {{color: red;}}
            }}
        </style>
        <div id="animated-text">{show_text}</div>
        <script>
            // JavaScript for animation control (optional)
            // You can use JavaScript to control more complex animations
        </script>
    """, unsafe_allow_html=True)
    st.subheader("_Patient Database Management System Simulation (PDBMSS)_")
    st.caption("Here, You can Simulate the Real Patient Database System and Play with the Realtime Patient Monitoring and Analysis.")

def dash_image():
    img = Image.open("dash.png")  # loading image with PIL uses RGB channels
    st.image(
    img,
    caption="Image of the Patient Database Management System Simulation",
    channels="RGB"
    )

# def dash_image():
#     # Load the first image
#     img1 = Image.open("icon1.jpeg")
#     # Load the second image
#     img2 = Image.open("icon2.jpeg")

#     # Display images side by side using columns
#     col1, col2 = st.columns(2)

#     with col1:
#         st.image(
#             img1,
#             caption="Image 1",
#             use_column_width=True  # Adjusts image width to the column width
#         )

#     with col2:
#         st.image(
#             img2,
#             caption="Image 2",
#             use_column_width=True  # Adjusts image width to the column width
#         )

