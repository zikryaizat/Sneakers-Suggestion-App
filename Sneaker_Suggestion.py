import streamlit as st
import os
import textwrap
from dotenv import load_dotenv
import requests
from PIL import Image
import google.generativeai as genai

#Load .env file
load_dotenv()
genai.configure(api_key = os.environ.get('GOOGLE_API_KEY'))


st.set_page_config(
    page_title='SneakersSeeker : Insights to Sneakers',
    page_icon='👟',
    layout="wide"
)

st.image('logo.jpg')
st.title("Welcome to SneakersSeeker : Find the perfect pair for you")
st.markdown(
    """
    What is Sneakers? :

    **Sneakers** (US) or **trainers** (UK), also known by a wide variety of other names, are shoes primarily designed for sports or other forms of physical exercise but which are also widely used for daily wear in multiple occasions.
    """
)
st.markdown(
    """
    This app will give sneakers suggestions for you. Write your own occasion in the text box or select descriptions by selecting your personal criteria on the sidebar.

    * **Model:** Gemini 1.5 Pro
    """
)


def user_input_features(desc_input):
    desc = st.sidebar.selectbox('Occasion', ('Sports', 'Casual', 'Fashion'))
    desc2 = st.sidebar.selectbox('Gender', ('Men', 'Women'))
    desc3 = st.sidebar.selectbox('Age', ('Teens', 'Adults'))
    desc4 = st.sidebar.selectbox('User Personality', ('Stand-out', 'Chill', 'Classic', 'Eco-Conscious'))
    suggested_desc = ""

    if desc == "Sports" and desc2 == "Men" and desc3 == "Teens" and desc4 == 'Stand-out':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Teens" and desc4 == 'Chill':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Teens" and desc4 == 'Classic':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Teens" and desc4 == 'Eco-Conscious':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Teens" and desc4 == 'Stand-out':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Teens" and desc4 == 'Chill':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Teens" and desc4 == 'Classic':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Teens" and desc4 == 'Eco-Conscious':
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Sports" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Sports', ('Running', 'Basketball', 'Badminton', 'Gym', 'Volleyball', 'Skateboarding', 'Tennis'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Men)', 'Dinner(Men)', 'Party(Men)', 'Casual Outing(Men)', 'Office Work(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Casual" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Casual', ('Wedding(Women)', 'Dinner(Women)', 'Party(Women)', 'Casual Outing(Women)', 'Office Work(Women)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Teens" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Teens" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Men" and desc3 == "Adults" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Men)', 'Vintage(Men)', 'Minimalist(Men)', 'Streetwear(Men)', 'Athleisure(Men)', 'Smart Casual(Men)'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Stand-out":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Chill":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Classic":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"
    elif desc == "Fashion" and desc2 == "Women" and desc3 == "Adults" and desc4 == "Eco-Conscious":
        suggested_desc = st.sidebar.selectbox('Fashion', ('Business Formal(Women)', 'Vintage(Women)', 'Minimalist(Women)', 'Streetwear(Women)', 'Athleisure(Women)', 'Blouse', 'Dress', 'Ball Gown', 'Chic'))
        desc_concatenated = f"Occasion is {desc}, Gender is {desc2}, Age is {desc3}, User Personality is {desc4}, type of {desc} is {suggested_desc}"

    return desc_concatenated

def suggested_shoe_ai(desc_input):
    system_input = f"You are a shoe or sneaker enthusiast with knowledge about shoes and sneakers. Please provide 5 suggestions of shoes or sneakers from different brands based on the user's preferences."

    example_input = f"Please suggest good shoes for running."

    example_output = f"""
    Your suggested shoes:
    * Nike Air Zoom Pegasus 38: The Pegasus line from Nike is renowned for its versatility and comfort, suitable for both long-distance running and everyday training.
    * Adidas Ultraboost 21: Adidas Ultraboost series offers excellent cushioning and responsiveness, making it ideal for runners seeking both comfort and performance.
    * Brooks Ghost 14: Brooks Ghost series is known for its plush cushioning and smooth ride, making it a popular choice among neutral runners for both short and long distances.
    * New Balance Fresh Foam 1080v11: New Balance Fresh Foam 1080v11 offers a supportive and cushioned ride, making it suitable for runners looking for comfort and stability on their runs.
    * Asics Gel-Kayano 28: Asics Gel-Kayano series is known for its stability and support, making it an excellent choice for runners with overpronation or seeking extra support on their runs.
    """

    user_input = f"You are a shoe or sneaker enthusiast with knowledge about shoes and sneakers. Based on price range of 20 to 100 Usd (Low), 101 to 200 Usd (Mid) and above 201Usd (High) , please provide 5 suggestions of sneakers for each price range, from different brands based on the user's preferences. From each sneakers listed, give details about the released year, colours, material, latest price, and state from which website you took the price and collaboration with artists/influencer if there are any, and the link to google search of the sneakers. Show the output in tabular form , the length and width of tables are consistent and in a proper manner and make the price range as the table caption meaning that the output will have 3 tables. Please generate suggestions based on the description: {desc_input}"
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(user_input)
    suggestion = response.text
    return suggestion

def suggested_shoe_ai2(input2):
    system_input = f"You are a shoe or sneaker enthusiast with knowledge about shoes and sneakers. Please provide 5 suggestions of shoes or sneakers from different brands based on the user's preferences."

    example_input = f"Please suggest good shoes for running."

    example_output = f"""
    Your suggested shoes:
    * Nike Air Zoom Pegasus 38: The Pegasus line from Nike is renowned for its versatility and comfort, suitable for both long-distance running and everyday training.
    * Adidas Ultraboost 21: Adidas Ultraboost series offers excellent cushioning and responsiveness, making it ideal for runners seeking both comfort and performance.
    * Brooks Ghost 14: Brooks Ghost series is known for its plush cushioning and smooth ride, making it a popular choice among neutral runners for both short and long distances.
    * New Balance Fresh Foam 1080v11: New Balance Fresh Foam 1080v11 offers a supportive and cushioned ride, making it suitable for runners looking for comfort and stability on their runs.
    * Asics Gel-Kayano 28: Asics Gel-Kayano series is known for its stability and support, making it an excellent choice for runners with overpronation or seeking extra support on their runs.
    """

    user_input = f"You are a shoe or sneaker enthusiast with knowledge about shoes and sneakers. Based on price range of 20 to 100 Usd (Low), 101 to 200 Usd (Mid) and above 201Usd (High) , please provide 5 suggestions of sneakers for each price range, from different brands based on the user's preferences. From each sneakers listed, give details about the released year, colours, material, latest price and state from which website you took the price and collaboration with artists/influencer if there are any and link to google search of the sneakers. Show the output in tabular form , the length and width of tables are consistent and in a proper manner and make the price range as the table caption meaning that the output will have 3 tables. Please generate suggestions based on the description: {input2}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    suggestion = response.text
    return suggestion

def main():
    desc_text = ""
    desc_input = ""
    desc_input2 = ""

    # User input @ Sidebar
    with st.sidebar:
        st.header("Enter the occasion for your sneakers here")
        text_input_prompt = st.text_input("Enter the prompt: ")
        submit_button = st.button("Find your pair!")
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>(or)</h1>", unsafe_allow_html=True)
        st.header("Select your personal criteria here")
        

    # Modify desc_input based on user selection
    desc_input = user_input_features(desc_input)
    

    with st.sidebar:
        submit_button2 = st.button("Generate your pair!")
    
    if desc_input and submit_button2:
        st.write(f"Your selection of criteria: **{desc_input}**")
        with st.spinner("Generating suggestion for you"):
            desc_text = suggested_shoe_ai(desc_input)
            # Display the suggestion
            st.header("Your Suggested Pair :")
            st.info(desc_text)
    elif text_input_prompt and submit_button:
        st.write(f"You entered: **{text_input_prompt}**")
        with st.spinner("Generating suggestion for you"):
            desc_text = suggested_shoe_ai2(desc_input2)
            # Display the suggestion
            st.header("Your Suggested Pair :")
            st.info(desc_text)

if __name__ == '__main__':
    main()
