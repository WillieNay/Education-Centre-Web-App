from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="MOE Learning Centre", page_icon="📚", layout="wide")

def load_lottiteurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.markdown("""
<style>
    /* Improve background colors */
    .stApp {
        background-color: #f0f4f8;
    }
    
    h1 {
        color: #1e3a8a;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    h2, h3, .subheader {
        color: #1e3a8a;
        font-weight: 600;
    }
    
    p, li {
        color: #1f2937;
        font-size: 1.05rem;
        line-height: 1.6;
    }
  
    .content-section {
        background-color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    
    hr {
        height: 3px;
        background-color: #3b82f6;
        border: none;
        margin: 2rem 0;
    }
    
    form input, form textarea {
        background-color: #f9fafb;
        color: #1f2937;
        border: 1px solid #d1d5db;
        border-radius: 0.375rem;
        padding: 0.75rem;
        margin-bottom: 1rem;
        font-size: 1rem;
    }
    
    form button {
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 0.375rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    form button:hover {
        background-color: #2563eb;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
    }
    
    th {
        background-color: #e0e7ff;
        color: #1e3a8a;
        padding: 0.75rem;
        text-align: left;
        font-weight: 600;
    }
    
    td {
        padding: 0.75rem;
        border-bottom: 1px solid #e5e7eb;
        color: #1f2937;
    }
    
    /* Link styling for better visibility */
    a {
        color: #2563eb;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Image styling for better blending */
    img {
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        max-width: 100%;
        height: auto;
    }
    
    /* Remove image backgrounds */
    .img-no-bg {
        background-color: transparent !important;
        mix-blend-mode: multiply;
    }
</style>
""", unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    local_css("style.css")
except:
    pass

try:
    animation_lottie = load_lottiteurl("https://lottie.host/6e1f213d-a396-46d3-9428-4b7923a53488/XwpEHXq62v.json")
    img_studying_pic = Image.open("studying_image.png")  # Assuming transparent PNG version
    img_harry_potter_pic = Image.open("student_image.png")  # Assuming transparent PNG version
except Exception as e:
    st.warning(f"Some images could not be loaded. The app will continue without them.")
    animation_lottie = None
    img_studying_pic = None
    img_harry_potter_pic = None

# Main content wrapped in styled containers
st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Hello, Welcome to MOE Learning Centre 👋")
st.title("The Best Learning Environment for your children")
st.write("We provide various education services such as tutoring classes, consultation and academic curriculum")
st.write(" For further inquiries > lilymoe74@gmail.com, +95 9798743047 ")
st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Services")
        st.write('##')
        st.write(
            """
            Currently, we provide basic English, Math Science classes for various grades:
            - We follow a variety of curriculums provided by Cambridge, Pearson, and many more
            - Other courses such as summer school, English language speaking, IT and British Council level exam focus classes.

            If you are interested, contact us for further detailed inquiries.
           """
        )
        
        st.write("[Facebook Page >](https://www.facebook.com/profile.php?id=100086756350545&mibextid=LQQJ4d)")
    
    with right_column:
        if animation_lottie:
            st_lottie(animation_lottie, height=300, key="Education")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Services section
with st.container():
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    st.header("Our classes")
    st.write("##")
    
    # First row of services
    image_column, text_column = st.columns((1,2))
    with image_column:
        if img_harry_potter_pic:
            st.markdown('<div class="img-no-bg">', unsafe_allow_html=True)
            st.image(img_harry_potter_pic)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Fallback if image is not available
            st.image("https://via.placeholder.com/400x300?text=Student+Image", use_column_width=True)
    
    with text_column:
        st.subheader("English Language Courses")
        st.write(
            """
            - We offer English courses using textbooks from Pearson and Cambridge. 
            
            - The courses are available from children starting from Grade 2 up till Grade 10.

            - Preparation courses for Cambridge Level Tests are also available (Starters, Movers, Flyers KET, PET, FCE)
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
    
    st.markdown('</div>', unsafe_allow_html=True)

# Second row of services
with st.container():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    image_column, text_column = st.columns((1,2))
    with image_column:
        if img_studying_pic:
            st.markdown('<div class="img-no-bg">', unsafe_allow_html=True)
            st.image(img_studying_pic)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Fallback if image is not available
            st.image("https://via.placeholder.com/400x300?text=Studying+Image", use_column_width=True)
    
    with text_column:
        st.subheader("Consulting")
        st.write(
            """
            - We also offer educational consulting services with students graduating from highschool. 
            
            - The services include guiding students what to pursue.

            - For example, tests and prerequisites they should take for university, which major should they choose, and introducing them with options to study abroad.
            """
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Info
with st.container():
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    
    st.header("Reach out to us!")
    st.write("##")

    contact_info = """
    <form action="https://formsubmit.co/lilymoe74@gmail.com" method="POST">
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
    
    st.markdown('</div>', unsafe_allow_html=True)
