import streamlit as st
import pickle
import numpy as np

# Load trained pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢")

# Story Introduction
st.title("🚢 Titanic Survival Prediction App")
st.markdown("""
Imagine a twist in history: the Titanic has mysteriously reappeared in the Atlantic Ocean, intact.  
The world is watching, and you have a ticket to board this legendary ship.  

Would you survive if disaster struck again?  
Use this app to check your survival chances based on historical data from the 1912 voyage.
""")
st.markdown("---")

st.image(r"D:\Jupyter Notebook\Training\Titanic Project\proceed-continue.gif")

# User Inputs
st.subheader("📝 Enter Passenger Details")
pclass = st.selectbox("Passenger Class", [1, 2, 3], help="1 = First Class, 2 = Second Class, 3 = Third Class / Steerage")
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.slider("Fare", 0, 500, 50)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"], help="C = Cherbourg, Q = Queenstown, S = Southampton")

# Prediction Button
if st.button("🔮 Predict Survival"):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = pipe.predict(input_data)[0]

    st.subheader("📜 Prediction Result:")
    if prediction == 1:
        st.success("🎉 Fate smiles upon you! If the Titanic sailed today, you would **Survive** this legendary voyage!")
        # Success GIF (local file)
        st.image(r"D:\Jupyter Notebook\Training\Titanic Project\happy-catto-cats.gif", width=400)
    else:
        st.error("💀 Alas! The odds are against you. If history repeated itself, you would **Not Survive** the Titanic disaster.")
        # Failure GIF (local file)
        st.image(r"D:\Jupyter Notebook\Training\Titanic Project\catsad-sad.gif", width=400)

    # Optional reasoning for engagement
    st.markdown("---")
    st.subheader("🧐 Why this prediction?")
    reasons = []
    if pclass == 1:
        reasons.append("Being in First Class greatly increased survival chances.")
    elif pclass == 3:
        reasons.append("Third Class passengers faced the toughest odds during evacuation.")
    if age < 15:
        reasons.append("Children were prioritized during evacuation.")
    if not reasons:
        reasons.append("Historical data shows outcomes were uncertain in this scenario.")
    st.write(" • ".join(reasons))

    st.markdown("""
---

🌊 **Disclaimer:** This is a fun, historical prediction based on Titanic data from 1912.  
It is not real-life advice — just a glimpse into history's most famous maritime tragedy.  
""")
