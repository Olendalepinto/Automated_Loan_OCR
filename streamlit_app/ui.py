import sys
import os
# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from app.preprocessing import preprocess_image
from app.ocr import extract_text
from app.extractor import extract_fields
from app.validator import validate_fields
from app.integrator import integrate_with_loan_system
import cv2
import tempfile

st.title("Automated Personal Loan Document Processing")

uploaded_file = st.file_uploader("Upload Loan Document", type=["png", "jpg", "jpeg"])

if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    preprocessed = preprocess_image(tfile.name)
    text = extract_text(preprocessed)
    fields = extract_fields(text)
    errors = validate_fields(fields)

    st.subheader("Extracted Fields")
    for key, value in fields.items():
        corrected = st.text_input(f"{key}:", value)
        fields[key] = corrected

    if errors:
        st.error(f"Validation Errors: {errors}")
    else:
        if st.button("Submit to Loan System"):
            if integrate_with_loan_system(fields):
                st.success("Data submitted successfully!")
