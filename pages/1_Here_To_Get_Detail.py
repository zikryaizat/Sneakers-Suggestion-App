import os
import streamlit as st
import openai 
from dotenv import load_dotenv
import requests
import pandas as pd
from PIL import Image
import rapidfuzz


#Load .env file
load_dotenv()

#Initialize OpenAi
openai.api_key = os.getenv('OPENAI_API_KEY')

st.set_page_config(
    page_title='SneakersSeeker : Insights to Sneakers',
    page_icon='👟'
)

image = Image.open('logo.jpg')

st.image(image, width = 780)
st.title("Welcome to SneakersSeeker : Find the perfect pair for you")
st.markdown(
    """
    In this page, you can find details about any sneakers that you want by entering the name of sneakers in the textbox.

    * **Model:** Gpt-3.5-Turbo, Dall-E-2
    * **Source of Sneakers Price:** [StockX](https://stockx.com/) as of 5/3/2024.
    """
)

def suggested_shoe_ai(msg):
    system_input = f"You are a shoes or sneakerhead that knows a lot of things about shoes and sneakers.Give details about the sneaker which contains released year, colours, material, current price and collaboration with artists/influencer if there are any based on user's input and write it in a tabular form"

    example_input = f"Please give details about Adidas Yeezy 350 v2"

    example_output = f"""
    Details:
    The Yeezy Boost 350 V2 is a popular sneaker model created in collaboration between Adidas and Kanye West, the American rapper, singer, and fashion designer.\n
    * Brand: Adidas (collaboration with Kanye West)\n
    * Release Year: The Yeezy Boost 350 V2 was first released in September 2016.\n
    * Material: The Yeezy Boost 350 V2 is primarily made from re-engineered Primeknit with additional elements like a monofilament side stripe, reflective threads, and a Boost midsole.\n
    * Available Colors: There have been numerous colorways released since its initial launch. Some of the most popular ones include "Zebra," "Beluga," "Bred," "Cream White," "Sesame," "Static," "Butter," "Black Static," "Yeezreel," "Clay," "Lundmark," "Yecheil," and many more. New colorways are periodically released, so the available options may vary over time.\n
    * Size Range: The Yeezy Boost 350 V2 is typically available in a wide range of sizes, catering to both men and women. Sizes typically range from US 4 to US 16 for men and US 5 to US 12 for women.\n
    * Collaborations: While the Yeezy Boost 350 V2 is primarily a collaboration between Adidas and Kanye West, there have been some limited edition releases that involved collaborations with other brands or artists. For example, there have been collaborations with brands like BAPE and collaborations with artists like Pharrell Williams. However, these collaborations are less common compared to the general releases.\n
    * Average Price: The retail price for a pair of Yeezy Boost 350 V2 sneakers varies depending on the specific colorway and any special editions or collaborations. Retail prices typically range from around $220 to $250 USD. However, due to their popularity and limited availability, resale prices for certain colorways can be significantly higher, sometimes reaching hundreds or even thousands of dollars above retail.\n
    """

    user_input = f"Please generate details of the sneakers based on the input: {msg}"

    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system','content': f'{system_input}'},
            {'role': 'user','content': f'{example_input}'}, # sample question
            {'role': 'assistant','content': f'{example_output}' },# sample answer
            {'role': 'user','content': f'{user_input}'}, # user question
        ],
        max_tokens=500
    )
    suggestion = response.choices[0].message.content
    return suggestion

def coverPhoto_ai(msg):
    response = openai.images.generate(
        model = "dall-e-2",
        prompt=f"Show a realistic picture of {msg} sneaker",
        n=1,
        size = "512x512",
        quality="standard"
    )
    image_url = response.data[0].url
    return image_url

# Load the shoe data
CSV_PATH = os.path.join(os.getcwd(),'cleaned_data1.csv')
data = pd.read_csv(CSV_PATH)

def find_closest_match(shoe_name, data):
    # Assuming you have a list of shoe names called 'shoe_names'
    closest_match, *_ = rapidfuzz.process.extractOne(shoe_name, data["Shoes"])
    return closest_match



def main():
    desc_text = ""
    shoe_img = ""
    closest_match = None
    #User input @ Sidebar
    with st.sidebar:
        st.header("Input Options")
        desc_input = st.text_area("Enter the name of shoes: ", height=100)
        submit_button = st.button("Find the details of your pair!")

    #Process user input
    if desc_input and submit_button:
        with st.spinner("Generating......"):
            desc_text = suggested_shoe_ai(desc_input)
            shoe_img = coverPhoto_ai(msg=desc_input)
            closest_match = find_closest_match(desc_input, data)

    # Display the story and cover photo
    st.header("Details of your shoes :")
    st.info(desc_text)

    st.header("AI image of the sneaker")
    if shoe_img:
        img = Image.open(requests.get(shoe_img, stream=True).raw)
        st.image(image=img)
    else:
        st.write("Image not available")

    # Display the price of the closest match
    if closest_match:
        price = data.loc[data["Shoes"] == closest_match]["Price(Usd)"].values[0]
        price = float(price.replace('$', ''))
        st.write(f"The price of the shoe, **{closest_match}**, obtained from StockX is **${price:.2f}**")
        st.markdown(
        """

        Suggested Sneakers shopping website(subjected to availability) :

        * [StockX](https://stockx.com/)
        * [Atmos KL](https://atmos-kl.com/)
        * [Footlocker](https://www.footlocker.my/)
        * [JD Sports](https://www.jdsports.my/)
        """
    )
    else:
        st.write("No matching shoe found in the dataset.")
    


if __name__ == '__main__' :
    main()



