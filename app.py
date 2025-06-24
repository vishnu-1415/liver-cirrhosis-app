import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load the model and normalizer
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("normalizer.pkl", "rb") as norm_file:
    normalizer = pickle.load(norm_file)

# Streamlit app UI
st.title("Liver Cirrhosis Prediction App 🧠")

# Input fields
age = st.number_input("Enter your Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Select Gender", ("Male", "Female"))
total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, step=0.1)
direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, step=0.1)
alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0.0, step=1.0)
alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0.0, step=1.0)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0.0, step=1.0)
total_proteins = st.number_input("Total Proteins", min_value=0.0, step=0.1)
albumin = st.number_input("Albumin", min_value=0.0, step=0.1)
albumin_globulin_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.0, step=0.1)

# Convert gender to numerical
gender_val = 1 if gender == "Male" else 0

# Predict button
if st.button("Predict"):
    try:
        input_data = np.array([[age, gender_val, total_bilirubin, direct_bilirubin,
                                alkaline_phosphotase, alamine_aminotransferase,
                                aspartate_aminotransferase, total_proteins,
                                albumin, albumin_globulin_ratio]])

        input_data_scaled = normalizer.transform(input_data)
        prediction = model.predict(input_data_scaled)

        if prediction[0] == 1:
            st.error("⚠️ High risk of Liver Cirrhosis. Please consult a doctor.")
        else:
            st.success("✅ Low risk of Liver Cirrhosis. Keep taking care!")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
     
                                                                                 st.error("⚠️ High Risk: Liver Cirrhosis Likely")
                                                                                                                              else:
                                                                                                                                      st.success("✅ Low Risk: No Liver Cirrhosis Detected")
                                                                                                                                      
