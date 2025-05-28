# Solar Industry AI Assistant

🌞 **Solar Rooftop AI Assistant** is an AI-powered tool that analyzes rooftop images (from satellite or user uploads) to assess solar installation potential, provide installation recommendations, and estimate ROI for solar setups.

---

## Project Overview

This project leverages Vision AI models to analyze rooftop images, identifies rooftop types, estimates suitable solar panel setup, and calculates ROI based on area and sunlight availability.

### Key Features
- Upload rooftop images via a web interface
- AI-driven rooftop analysis with labels and confidence scores
- Calculation of solar installation ROI (cost, annual savings, payback period)
- User-friendly interactive UI built with Streamlit

---

## Tech Stack

- **Python 3.9+**
- **Streamlit** — Web UI framework
- **Requests** — API calls to Vision AI model
- **Pillow (PIL)** — Image processing
- **Hugging Face API** — Vision AI model inference

---

## Prerequisites

- Python 3.9 or later installed on your machine
- An API key for Hugging Face API (you can get one by signing up at [Hugging Face](https://huggingface.co/))
- Internet connection for API calls

---

✅ Set Up a Virtual Environment (Optional but Recommended)
cd solar_ai_assistant
python -m venv venv
venv\Scripts\activate

✅ Install Required Dependencies
pip install -r requirements.txt

✅ Change the directory
cd app

✅ Run the app
streamlit run main.py


Now select the image given in the folder assets

Then!!! Booooom💥💥💥💥 It's done...
