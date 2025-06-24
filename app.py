import streamlit as st
import numpy as np
import pickle

# Load model and normalizer
try:
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("normalizer.pkl", "rb") as norm_file:
        normalizer = pickle.load(norm_file)
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.title("Liver Cirrhosis Prediction App")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
total_bilirubin = st.number_input("Total Bilirubin (mg/dL)", min_value=0.0, step=0.1)
direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", min_value=0.0, step=0.1)
alkaline_phosphotase = st.number_input("Alkaline Phosphotase (IU/L)", min_value=0.0, step=1.0)
alamine_aminotransferase = st.number_input("Alamine Aminotransferase (IU/L)", min_value=0.0, step=1.0)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase (IU/L)", min_value=0.0, step=1.0)
total_proteins = st.number_input("Total Proteins (g/dL)", min_value=0.0, step=0.1)
albumin = st.number_input("Albumin (g/dL)", min_value=0.0, step=0.1)
albumin_globulin_ratio = st.number_input("Albumin/Globulin Ratio", min_value=0.0, step=0.1)

# Convert gender to number
gender_value = 1 if gender == "Male" else 0

# Prediction
if st.button("Predict"):
    try:
        input_data = np.array([[age, gender_value, total_bilirubin, direct_bilirubin,
                                alkaline_phosphotase, alamine_aminotransferase,
                                aspartate_aminotransferase, total_proteins,
                                albumin, albumin_globulin_ratio]])
        
        # Normalize
        input_scaled = normalizer.transform(input_data)
        prediction = model.predict(input_scaled)

        # Output
        if prediction[0] == 1:
            st.error("⚠️ High Risk of Liver Cirrhosis. Please consult a doctor.")
        else:
            st.success("✅ Low Risk of Liver Cirrhosis. Keep up healthy habits!")
    except Exception as e:
        st.warning(f"Prediction error: {e}")
        
