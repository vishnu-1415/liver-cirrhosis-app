import streamlit as st
import pickle
import numpy as np

# Load model and normalizer
model = pickle.load(open("model.pkl", "rb"))
normalizer = pickle.load(open("normalizer.pkl", "rb"))

st.title("Liver Cirrhosis Prediction")

# Inputs
age = st.number_input("Age", 1, 120)
gender = st.selectbox("Gender", ["Male", "Female"])
total_bilirubin = st.number_input("Total Bilirubin")
direct_bilirubin = st.number_input("Direct Bilirubin")
alkaline_phosphotase = st.number_input("Alkaline Phosphotase")
alamine_aminotransferase = st.number_input("Alamine Aminotransferase")
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase")
total_proteins = st.number_input("Total Proteins")
albumin = st.number_input("Albumin")
albumin_globulin_ratio = st.number_input("Albumin-Globulin Ratio")

# Gender to number
gender_num = 1 if gender == "Male" else 0

if st.button("Predict"):
    try:
        input_data = np.array([[age, gender_num, total_bilirubin, direct_bilirubin,
                                alkaline_phosphotase, alamine_aminotransferase,
                                aspartate_aminotransferase, total_proteins,
                                albumin, albumin_globulin_ratio]])
        
        input_data_scaled = normalizer.transform(input_data)
        result = model.predict(input_data_scaled)

        if result[0] == 1:
            st.error("⚠️ High Risk of Liver Cirrhosis")
        else:
            st.success("✅ Low Risk of Liver Cirrhosis")

    except Exception as e:
        st.warning(f"Error occurred: {e}")
        
