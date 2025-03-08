# MOE Learning Centre Website

This project is a website for MOE Learning Centre, an educational center offering tutoring classes, consultation, and academic curriculum development. It is built using Python and the Streamlit library.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project develops a dynamic and visually appealing website for MOE Learning Centre using Streamlit. The website showcases the center's educational services, including tutoring classes, consultation, and academic curriculum. It features interactive elements like animations, image displays, and a contact form to enhance user engagement. The website aims to provide a comprehensive overview of the center's offerings and facilitate inquiries from prospective students and parents.

## Features

- **Interactive Web Interface:** Built with Streamlit, providing a user-friendly and responsive experience.
- **Service Showcase:** Detailed descriptions of tutoring classes, consultation, and curriculum development services.
- **Course Information:** Comprehensive information about English, Science, and Math courses, including grade levels and curriculum details.
- **Visual Appeal:** Uses animations (Lottie) and images to enhance the website's visual appeal.
- **Contact Form:** Integrated contact form for easy communication.
- **Custom Styling:** Custom CSS for a tailored website appearance.
- **Facebook Page Link:** Easy access to the learning center's Facebook page.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:

    -   **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    -   **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

    (If you don't have a requirements.txt file, create one with the following content and then run the command above)
    ```
    streamlit
    requests
    Pillow
    streamlit-lottie
    ```

### Running the Application

1.  Navigate to the project directory.
2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

    (Replace `app.py` with the name of your main Python file if it's different.)

3.  The application will open in your default web browser.

## Usage

-   Navigate through the sections to explore the services and courses offered by MOE Learning Centre.
-   Use the contact form to send inquiries.
-   Click the Facebook link to visit the center's Facebook page.


## Dependencies

-   streamlit
-   requests
-   Pillow (PIL)
-   streamlit-lottie

## Author
- Nay Linn Htin/ Willie Nay
