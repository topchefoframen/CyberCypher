import streamlit as st
import google.generativeai as genai

# Google AI API Configuration
GOOGLE_API_KEY = "AIzaSyDHYYjl6EQ0PEoA4wc1oPOai1eIzcUJSYg"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to get AI response
def ask_ai(prompt):
    model = genai.GenerativeModel("gemini-pro")  # Using Gemini-Pro model
    response = model.generate_content(prompt)
    return response.text if response else "Error: No response from AI."

# Streamlit UI
st.title("🚀 AI Startup Advisor")
st.write("Ask any question about building a startup, and AI will help!")

user_input = st.text_area("What do you need help with?", "")

if st.button("Ask AI"):
    if user_input:
        st.write("⏳ Fetching AI Response...")
        response = ask_ai(user_input)
        st.write("### AI Response:")
        st.write(response)
    else:
        st.write("⚠️ Please enter a question.")
