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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add custom CSS for text colors and improved user experience
st.markdown("""
<style>
    .title-text {
        font-size: 3.2rem !important;
        font-weight: 700 !important;
        color: #FFD700 !important;
        margin-bottom: 1.5rem;
    }
    .subtitle-text {
        font-size: 1.8rem !important;
        color: #3CB371 !important;
        font-weight: 600 !important;
    }
    .header-text {
        font-size: 2.5rem !important;
        color: #1E90FF !important;
        font-weight: 600 !important;
        margin-top: 1rem !important;
    }
    .normal-text {
        font-size: 1.1rem !important;
        color: #E0E0E0 !important;
        line-height: 1.6 !important;
    }
    .contact-text {
        font-size: 1.1rem !important;
        color: #F08080 !important;
    }
    .highlight-text {
        color: #FFD700 !important;
        font-weight: 600 !important;
    }
    .divider {
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
    }
    ul {
        margin-left: 1.5rem !important;
    }
    li {
        color: #E0E0E0 !important;
        margin-bottom: 0.5rem !important;
    }
    /* Form styling */
    input, textarea {
        border-radius: 8px !important;
        padding: 12px !important;
        margin-bottom: 12px !important;
        border: 1px solid #555 !important;
        width: 100% !important;
        background-color: #333 !important;
        color: white !important;
    }
    button[type="submit"] {
        background-color: #4CAF50 !important;
        color: white !important;
        padding: 12px 20px !important;
        border: none !important;
        border-radius: 8px !important;
        cursor: pointer !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    button[type="submit"]:hover {
        background-color: #3e8e41 !important;
        transform: translateY(-2px) !important;
    }
</style>
""", unsafe_allow_html=True)

local_css("style.css")

animation_lottie = "https://lottie.host/6e1f213d-a396-46d3-9428-4b7923a53488/XwpEHXq62v.json"
img_studying_pic = Image.open("45 Hilarious Memes For When You Need A Laugh.jpeg")
img_harry_potter_pic = Image.open("7 secretos de belleza que Emma Watson aplica todos los días - Cultura Colectiva.jpeg")

# Enhanced header with wave animation
st.markdown('<p class="subtitle-text">Hello, Welcome to MOE Learning Centre 👋</p>', unsafe_allow_html=True)
st.markdown('<h1 class="title-text">The Best Learning Environment for your children</h1>', unsafe_allow_html=True)
st.markdown('<p class="normal-text">We provide various education services such as tutoring classes, consultation and academic curriculum</p>', unsafe_allow_html=True)
st.markdown('<p class="contact-text">For further inquiries → <span class="highlight-text">lilymoe74@gmail.com</span>, <span class="highlight-text">+95 9798743047</span></p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown('<h2 class="header-text">Our Services</h2>', unsafe_allow_html=True)
        st.write('##')
        st.markdown(
            """
            <p class="normal-text">
            Currently, we provide basic English, Math Science classes for various grades:
            <ul>
                <li>We follow a variety of curriculums provided by Cambridge, Pearson, and many more</li>
                <li>Other courses such as summer school, English language speaking, IT and British Council level exam focus classes.</li>
            </ul>
            </p>
            <p class="normal-text">
            If you are interested, contact us for further detailed inquiries.
            </p>
            """, unsafe_allow_html=True
        )
        
        st.markdown('<a href="https://www.facebook.com/profile.php?id=100086756350545&mibextid=LQQJ4d" target="_blank" style="color: #4267B2; font-weight: bold; text-decoration: none;">Facebook Page →</a>', unsafe_allow_html=True)
    with right_column:
        st_lottie(animation_lottie, height=300, key="Education")

# Services section with enhanced styling
with st.container():
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<h2 class="header-text">Our Classes</h2>', unsafe_allow_html=True)
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_harry_potter_pic)
    with text_column:
        st.markdown('<h3 class="subtitle-text">English Language Courses</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="normal-text">
            <ul>
                <li>We offer English courses using textbooks from Pearson and Cambridge.</li>
                <li>The courses are available from children starting from Grade 2 up till Grade 10.</li>
                <li>Preparation courses for Cambridge Level Tests are also available (Starters, Movers, Flyers KET, PET, FCE)</li>
            </ul>
            </p>
            """, unsafe_allow_html=True
        )
        st.markdown('<h3 class="subtitle-text">Science Courses</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="normal-text">
            <ul>
                <li>We also offer Science courses using textbooks from Macmillan/McGraw Hill.</li>
                <li>The courses are available from children starting from Grade 2 up till Grade 10.</li>
                <li>Courses are available both online and in person with experiments and practical lab time weekly.</li>
            </ul>
            </p>
            """, unsafe_allow_html=True
        )
        st.markdown('<h3 class="subtitle-text">Math Courses</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="normal-text">
            <ul>
                <li>We also offer Math courses using textbooks from Cambridge and My Pals Are Here.</li>
                <li>The courses are available from children starting from Grade 2 up till Grade 10.</li>
                <li>Courses are available both online and in person.</li>
            </ul>
            </p>
            """, unsafe_allow_html=True
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_studying_pic)
    with text_column:
        st.markdown('<h3 class="subtitle-text">Consulting</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            <p class="normal-text">
            <ul>
                <li>We also offer educational consulting services with students graduating from highschool.</li>
                <li>The services include guiding students what to pursue.</li>
                <li>For example, tests and prerequisites they should take for university, which major should they choose, and introducing them with options to study abroad.</li>
            </ul>
            </p>
            """, unsafe_allow_html=True
        )

# Enhanced contact form with better styling
with st.container():
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<h2 class="header-text">Reach out to us!</h2>', unsafe_allow_html=True)
    st.write("##")

    contact_info = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" style="height: 150px;" required></textarea>
        <button type="submit">Send Message</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
         st.markdown(contact_info, unsafe_allow_html=True)
    with right_column:
        st.empty()
