from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="MOE Learning Centre",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Custom CSS to make the app more vibrant and modern
def apply_custom_styles():
    st.markdown("""
    <style>
        /* Main color scheme */
        :root {
            --primary-color: #4361ee;
            --secondary-color: #3a0ca3;
            --accent-color: #7209b7;
            --background-color: #f8f9fa;
            --text-color: #2b2d42;
            --light-accent: #4cc9f0;
        }
        
        /* Global text styling */
        body {
            color: var(--text-color);
            background-color: var(--background-color);
            font-family: 'Poppins', sans-serif;
        }
        
        /* Header styling */
        h1, h2, h3, h4 {
            color: var(--primary-color);
            font-weight: 700;
        }
        
        /* Subheader with wave animation */
        .wave-text {
            background: linear-gradient(45deg, #4361ee, #3a0ca3, #7209b7, #f72585);
            background-size: 300% 300%;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 10px;
            animation: gradient 6s ease infinite;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Container styling */
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Card styling for services */
        .service-card {
            background-color: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
        }
        
        /* Contact form styling */
        .contact-form {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            font-size: 16px;
        }
        
        .contact-form button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: background-color 0.3s ease;
        }
        
        .contact-form button:hover {
            background-color: var(--secondary-color);
        }
        
        /* Custom divider */
        .custom-divider {
            height: 4px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            border-radius: 2px;
            margin: 2rem 0;
        }
        
        /* Image styling */
        .rounded-image img {
            border-radius: 10px;
            width: 100%;
            object-fit: cover;
            height: 300px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        }
        
        /* Footer styling */
        .footer {
            background-color: var(--primary-color);
            color: white;
            padding: 1rem;
            text-align: center;
            border-radius: 10px;
            margin-top: 2rem;
        }
        
        /* Social media icons */
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
        }
        
        .social-icon {
            font-size: 24px;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Apply custom styles
apply_custom_styles()

# Load assets
animation_lottie = load_lottie_url("https://lottie.host/6e1f213d-a396-46d3-9428-4b7923a53488/XwpEHXq62v.json")
img_studying_pic = Image.open("45 Hilarious Memes For When You Need A Laugh.jpeg")
img_harry_potter_pic = Image.open("7 secretos de belleza que Emma Watson aplica todos los días - Cultura Colectiva.jpeg")

# Header section with gradient effect
st.markdown('<div class="wave-text"><h2>👋 Welcome to MOE Learning Centre</h2></div>', unsafe_allow_html=True)
st.title("The Best Learning Environment for Your Children")
st.write("We provide comprehensive education services including tutoring classes, academic consultations, and customized curriculum planning.")

# Contact info with icons
col1, col2 = st.columns([3, 1])
with col1:
    st.write("📧 Email: lilymoe74@gmail.com  |  📱 Phone: +95 9798743047")
with col2:
    st.markdown("""
    <div class="social-icons">
        <a href="https://www.facebook.com/profile.php?id=100086756350545" target="_blank"><span class="social-icon">📘</span></a>
        <a href="#" target="_blank"><span class="social-icon">📸</span></a>
    </div>
    """, unsafe_allow_html=True)

# Custom divider
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# Our Services Section
with st.container():
    left_column, right_column = st.columns([1.5, 1])
    
    with left_column:
        st.header("🌟 Our Services")
        st.markdown("""
        <div class="service-card">
            <p>At MOE Learning Centre, we provide comprehensive education services tailored to your child's needs:</p>
            <ul>
                <li>We follow a variety of curriculums from Cambridge, Pearson, and other leading educational institutions</li>
                <li>Specialized courses including summer school, English language speaking, IT skills, and British Council exam preparation</li>
                <li>Small class sizes to ensure personalized attention for each student</li>
                <li>Both online and in-person learning options to suit your schedule</li>
            </ul>
            <a href="https://www.facebook.com/profile.php?id=100086756350545&mibextid=LQQJ4d" target="_blank">
                <div style="background-color: #4361ee; color: white; padding: 8px 16px; border-radius: 5px; display: inline-block; font-weight: 600;">
                    Visit our Facebook Page →
                </div>
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with right_column:
        st_lottie(animation_lottie, height=300, key="Education")

# Custom divider
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# Classes section with card-based layout
st.header("📚 Our Classes")

tab1, tab2, tab3, tab4 = st.tabs(["English", "Science", "Math", "Consulting"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="rounded-image">', unsafe_allow_html=True)
        st.image(img_harry_potter_pic)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="service-card">
            <h3 style="color: #4361ee;">English Language Courses</h3>
            <p>Our comprehensive English language program uses the finest materials from Pearson and Cambridge:</p>
            <ul>
                <li>Available for students from Grade 2 through Grade 10</li>
                <li>Focus on reading, writing, speaking, and listening skills</li>
                <li>Preparation courses for Cambridge Level Tests (Starters, Movers, Flyers, KET, PET, FCE)</li>
                <li>Native-speaking teachers for advanced conversation practice</li>
                <li>Regular progress assessments and parent feedback</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="service-card">
        <h3 style="color: #3a0ca3;">Science Courses</h3>
        <p>Our science program brings learning to life with interactive experiments and hands-on activities:</p>
        <ul>
            <li>Curriculum based on Macmillan/McGraw Hill textbooks</li>
            <li>Available for students from Grade 2 through Grade 10</li>
            <li>Weekly laboratory sessions with practical experiments</li>
            <li>Both online and in-person learning options</li>
            <li>Project-based learning to develop critical thinking skills</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="service-card">
        <h3 style="color: #7209b7;">Math Courses</h3>
        <p>Our mathematics program develops strong numerical skills and problem-solving abilities:</p>
        <ul>
            <li>Curriculum based on Cambridge and My Pals Are Here textbooks</li>
            <li>Available for students from Grade 2 through Grade 10</li>
            <li>Focus on both fundamental skills and advanced problem-solving</li>
            <li>Regular practice with international competition-style questions</li>
            <li>Available in both online and in-person formats</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="rounded-image">', unsafe_allow_html=True)
        st.image(img_studying_pic)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="service-card">
            <h3 style="color: #f72585;">Educational Consulting</h3>
            <p>We guide high school graduates toward their academic and career goals:</p>
            <ul>
                <li>Personalized guidance for university applications</li>
                <li>Assessment of student strengths and interests</li>
                <li>Information about required tests and prerequisites</li>
                <li>Major selection advice based on career aspirations</li>
                <li>Guidance on study abroad opportunities</li>
                <li>Scholarship application assistance</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Custom divider
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# Contact section with improved form
st.header("📬 Reach Out to Us!")

contact_form = """
<div class="contact-form">
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" rows="5" required></textarea>
        <button type="submit">Send Message</button>
    </form>
</div>
"""

location_info = """
<div class="service-card">
    <h3>Visit Us</h3>
    <p>We're located in a convenient, central location:</p>
    <p>123 Education Street<br>Yangon, Myanmar</p>
    <h4>Opening Hours</h4>
    <p>Monday - Saturday<br>
    Sunday: Closed</p>
</div>
"""

col1, col2 = st.columns(2)
with col1:
    st.markdown(contact_form, unsafe_allow_html=True)
with col2:
    st.markdown(location_info, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 MOE Learning Centre. All rights reserved.</p>
    <p>Providing quality education since 2018</p>
</div>
""", unsafe_allow_html=True)
