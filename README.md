### README for Plant Disease Diagnosis App

This README provides a step-by-step guide to setting up and running a Streamlit app for diagnosing plant diseases using GPT-4's vision capabilities. The app allows users to upload an image of a plant leaf and receive a diagnosis, including treatment suggestions if a disease is detected.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
   - [1. Clone the Repository](#1-clone-the-repository)
   - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
   - [3. Activate the Virtual Environment](#3-activate-the-virtual-environment)
   - [4. Install the Required Packages](#4-install-the-required-packages)
3. [Running the App](#running-the-app)
4. [Usage](#usage)
5. [Notes](#notes)
6. [License](#license)

---

## Prerequisites

- **Python 3.7+**: Make sure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **OpenAI API Key**: Obtain an API key from OpenAI. This key is required to access GPT-4's vision capabilities. You can get the API key from the [OpenAI API Dashboard](https://platform.openai.com/account/api-keys).

---

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine. If you haven't created a repository yet, you can skip this step and simply create a directory for the project.

```bash
git clone https://github.com/yourusername/plant-disease-diagnosis.git
cd plant-disease-diagnosis
```

If you're not using Git, create a new directory and navigate to it:

```bash
mkdir plant-disease-diagnosis
cd plant-disease-diagnosis
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to keep the project dependencies isolated.

```bash
python -m venv venv
```

This command creates a new virtual environment named `venv` inside your project directory.

### 3. Activate the Virtual Environment

Activate the virtual environment using the following command:

- **For Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- **For macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

Once activated, your terminal prompt should change to indicate that the virtual environment is active.

### 4. Install the Required Packages

With the virtual environment activated, install the necessary Python packages using `pip`:

```bash
pip install streamlit openai pillow requests
```

This command installs the following libraries:
- **Streamlit**: For creating the web app.
- **OpenAI**: To interact with GPT-4's API.
- **Pillow**: For image processing.
- **Requests**: For making HTTP requests to the OpenAI API.

### 5. Put the GPT API KEY HERE
![image](https://github.com/user-attachments/assets/d2965274-6413-4523-955d-9f81f7a03908)

---


## Running the App

To start the Streamlit app, ensure your virtual environment is activated and run the following command:

```bash
streamlit run app.py
```

After running this command, Streamlit will launch a local server, and a web browser should automatically open with the app. If the browser doesn’t open automatically, navigate to the URL provided in the terminal, typically `http://localhost:8501`.

---

## Usage

1. **Upload an Image**: Click on the "Choose an image..." button and select an image of a plant leaf from your local system. The app supports `.jpg`, `.jpeg`, and `.png` formats.

2. **View the Diagnosis**: After uploading, the image will be displayed on the screen. The app will then analyze the image using GPT-4's vision capabilities and provide a diagnosis of any plant disease detected.

3. **Treatment Suggestions**: If a disease is detected, the app will also provide treatment suggestions, including recommended medicines and dosages.


