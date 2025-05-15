import streamlit as st
from PIL import Image
from models.gemini_api import get_gemini_response, prepare_image
from agents.meal_planner import weekly_meal_plan
from agents.calorie_calculator import summarize_calories

def main():
    st.set_page_config(page_title="Smart AI Nutrition Assistant")
    st.title("🍎 Smart AI Nutrition Assistant")

    input_text = st.text_input("🔍 Describe your meal or goal:")
    uploaded_file = st.file_uploader("📷 Upload a food image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze and Plan"):
        if uploaded_file and input_text:
            image_data = prepare_image(uploaded_file)
            prompt = (
                "You are a nutritionist. Identify food items in the image, calculate total calories, and list nutrients. "
                "Give output in the format:\n"
                "1. Item - calories, nutrients\n"
                "2. Item - calories, nutrients\n"
                "...\n"
                "Also, provide a weekly healthy meal plan."
            )

            result = get_gemini_response(input_text, image_data, prompt)
            st.subheader("🧾 Nutrition Analysis")
            st.write(result)

            total_calories, breakdown = summarize_calories(result)
            st.markdown(f"**Total Estimated Calories:** {total_calories}")
            st.markdown("**Breakdown:**")
            for item in breakdown:
                st.write(item)

            st.subheader("📅 Weekly Meal Plan")
            plan = weekly_meal_plan()
            for day, meals in plan.items():
                st.markdown(f"**{day}:** {meals}")
        else:
            st.error("Please upload an image and enter your goal.")

