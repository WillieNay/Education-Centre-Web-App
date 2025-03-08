from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="MOE Learning Centre", page_icon=":::man_student:", layout="wide")

def load_lottiteurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
      



animation_lottie = "https://lottie.host/6e1f213d-a396-46d3-9428-4b7923a53488/XwpEHXq62v.json"
img_studying_pic = Image.open("images/45 Hilarious Memes For When You Need A Laugh.jpeg")
img_harry_potter_pic = Image.open("images/7 secretos de belleza que Emma Watson aplica todos los días - Cultura Colectiva.jpeg")


st.subheader("Hello, Welcome to MOE Learning Centre :wave:")
st.title("The Best Learning Environment for your children")
st.write("We provide various education service such as tutoring classes, consultation and academic ciriculum")
st.write(" For further inquiries > lilymoe74@gmail.com, +95 9798743047 ")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Services")
        st.write('##')
        st.write (
            """
            Currently, we provide basic English, Math Science clasess for various grades:
            - We follow a variety of ciriculums provided by Cambridge, Pearson, and many more
            - Other courses such as summer school, English language speaking, IT and British Council level exam focus classes.


            If you are interested, contact us for further detailed inquiries.
           """

         )
        
        st.write("[Facebook Page >](https://www.facebook.com/profile.php?id=100086756350545&mibextid=LQQJ4d)")
    with right_column:
        st_lottie(animation_lottie, height=300, key="Education")

# - - - - Services - - - - 
with st .container():
    st.write("- - -")
    st.header("Our classes")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_harry_potter_pic)
    with text_column:
        st.subheader("English Language Courses")
        st.write(
            """
            - We offer English courses using textbooks from Pearson and Cambridge. 
            
            - The courses are available from children starting from Grade 2 up till Grade 10.

            - Preparation courses for Cambridge Level Tests are also available (Starters, Movers, Flyers KET ,PET , FCE)
            """
        )
        st.subheader("Science Courses")
        st.write(
            """
            - We also offer Science courses using textbooks from Macmillan/McGraw Hill. 
            
            - The courses are available from children starting from Grade 2 up till Grade 10.

            - Courses are available both online and in person with experiments and practical lab time weekly.
            """
        )
        st.subheader("Math Courses")
        st.write(
            """
            - We also offer Math courses using textbooks from Cambridge and My Pals Are Here. 
            
            - The courses are available from children starting from Grade 2 up till Grade 10.

            - Courses are available both online and in person.
            """
        )
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_studying_pic)
    with text_column:
        st.subheader("Consulting")
        st.write(
            """
            - We also offer educational consulting services with students graduating from highschool. 
            
            - The services include guiding students what to pursue.

            - For example, tests and prerequisites they should take for university, which major should they choose, and introducing them with options to study abroad.
            """
        )

# - - - Contact Info - - -
with st.container():
    st.write("- - -")
    st.header("Reach out to us!")
    st.write("##")

    contact_info = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
         st.markdown(contact_info, unsafe_allow_html=True)
    with right_column:
        st.empty()
