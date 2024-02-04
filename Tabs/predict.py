import streamlit as st
from web_functions import predict

# Function to display the prediction page
def app(df, x, y):
    # Title page
    st.title("Prediction Page")

    # Split the column into three parts
    col1, col2, col3 = st.columns(3)

    # Input for features to be used in prediction
    with col1:
        bp = st.text_input("Blood Pressure")
        sg = st.text_input("Specific Gravity")
        al = st.text_input("Albumin")
        su = st.text_input("Sugar")
        rbc = st.text_input("Red Blood Cells")
        pc = st.text_input("Pus Cell")
        pcc = st.text_input("Pus Cell Clumps")
        ba = st.text_input("Bacteria")
    
    with col2:
        bgr = st.text_input("Blood Glucose Random")
        bu = st.text_input("Blood Urea")
        sc = st.text_input("Serum Creatinine")
        sod = st.text_input("Sodium")
        pot = st.text_input("Potassium")
        hemo = st.text_input("Hemoglobin")
        pcv = st.text_input("Packed Cell Volume")
        wc = st.text_input("White Blood Cell Count")
    
    with col3:
        rc = st.text_input("Red Blood Cell Count")
        htn = st.text_input("Hypertension")
        dm = st.text_input("Diabetes Mellitus")
        cad = st.text_input("Coronary Artery Disease")
        appet = st.text_input("Appetite")
        pe = st.text_input("Pedal Edema")
        ane = st.text_input("Anemia")

    # List the features
    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]

    # Button to make predictions
    if st.button("Prediction"):
        prediction, score = predict(x, y, features)
        st.info("Prediction is successful...")

        # Display the prediction result
        if prediction == 1:
            st.warning("The person is prone to kidney disease")
        else:
            st.success("The person is relatively safe from kidney disease")
        
        # Display model accuracy
        st.write("The model used has an accuracy rate of ", (score * 100), "%")
