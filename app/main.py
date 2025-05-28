import streamlit as st
from analyzer import analyze_image
from roi_calculator import calculate_roi
from PIL import Image

st.title("🌞 Solar Rooftop AI Assistant")
uploaded_file = st.file_uploader("Upload a rooftop image")

if uploaded_file:
    # Save uploaded file temporarily
    temp_file_path = "temp_uploaded_image.jpg"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Open and display image
    image = Image.open(temp_file_path)
    st.image(image, caption="Uploaded Rooftop", use_column_width=True)

    with st.spinner("Analyzing image..."):
        try:
            result = analyze_image(temp_file_path)
            st.success("Analysis Complete!")

            # Result is a list of dicts, get the first prediction
            if isinstance(result, list) and len(result) > 0:
                top_result = result[0]
                # Extract label or area if your model provides it
                area = top_result.get("area_sqft", 500) if "area_sqft" in top_result else 500
                sunlight = top_result.get("sunlight_hours", 5) if "sunlight_hours" in top_result else 5
            else:
                area = 500
                sunlight = 5

            roi = calculate_roi(area, sunlight)

            st.write("### Recommended Setup:")
            st.json(result)

            st.write("### ROI Estimate:")
            st.write(roi)

        except Exception as e:
            st.error(f"Error analyzing image: {e}")
