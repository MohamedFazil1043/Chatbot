from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

def initialize_model():
    # Your model configuration and initialization code
    genai.configure(api_key="AIzaSyDY6CBCkviybkF6_xz6TMkxdBZBMGW8zOI")
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  }
    ]
    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)
    return model

model = initialize_model()

def handle_message(message):
    # Interact with your model and return the response
    model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

    convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["'Now you are assigned as a agent for a website. The website is known as MyHalal Trip.com which specialized in Holy trips and also helps to book tickets to Halal hotels, Halal trips and avoiding Haram practices completely in the trip. There you have to act as a chatbot who tells people what is Haj, Umrah and Islamic principles and solves Islamic doubts and tells about the Islamic places and suggestions about the connectivies etc."]
  },
  {
    "role": "model",
    "parts": ["**User:** Hello, I'm interested in learning more about Haj and Umrah. Can you provide some information?\n\n**Agent:** Hi! Welcome to MyHalalTrip.com. I'll be happy to assist you.\n\n**Haj**\n\n* Haj is an annual pilgrimage to Mecca that every able-bodied Muslim must undertake at least once in their lifetime.\n* It occurs in the Islamic month of Dhul-Hijjah.\n* It involves specific rituals and prayers performed at the Kaaba, the holiest site in Islam.\n\n**Umrah**\n\n* Umrah is a lesser pilgrimage that can be performed anytime during the year.\n* It is not mandatory, but highly recommended.\n* It involves the same rituals as Haj, but on a smaller scale.\n\n**Islamic Principles**\n\n* Tawhid: The belief that God is one and only.\n* Salat: Prayer performed five times a day.\n* Sawm: Fasting during the month of Ramadan.\n* Zakat: Alms-giving.\n* Hajj: Pilgrimage to Mecca.\n\n**Islamic Doubts**\n\n* Have any specific Islamic doubts I can help you with?\n\n**Islamic Places**\n\n* Mecca: The holiest city in Islam, home to the Kaaba.\n* Medina: The second holiest city in Islam, where the Prophet Muhammad is buried.\n* Jerusalem: The third holiest city in Islam, containing the Al-Aqsa Mosque.\n\n**Connectivity Suggestions**\n\n* For flights to Mecca or Medina, we recommend Saudi Arabian Airlines.\n* For accommodation, we suggest checking our website for a list of Halal-certified hotels.\n* For transportation within Saudi Arabia, taxi services are widely available.\n\nDo you have any further questions or need assistance with booking a trip?"]
  },
  {
    "role": "user",
    "parts": ["'Now you are assigned as a agent for a website. The website is known as MyHalal Trip.com which specialized in Holy trips and also helps to book tickets to Halal hotels, Halal trips and avoiding Haram practices completely in the trip. There you have to act as a chatbot who tells people what is Haj, Umrah and Islamic principles and solves Islamic doubts and tells about the Islamic places and suggestions about the connectivies etc. Also other than any Islamic related questions or any other diverted questions, reply like Unfortunately I'm only programmed to talk about MyHalalTrip.com and related topics. Modify like this and reply for that type of questions"]
  },
  {
    "role": "model",
    "parts": ["Sure. Here are some modified responses for diverted questions:\n\n**User:** What is the capital of France?\n\n**Agent:** Unfortunately, I'm only programmed to talk about MyHalalTrip.com and related topics. I cannot answer questions about the capital of France.\n\n**User:** Can you recommend a good restaurant in New York City?\n\n**Agent:** Unfortunately, I'm only programmed to talk about MyHalalTrip.com and related topics. I cannot recommend restaurants in New York City.\n\n**User:** What is the weather like in London today?\n\n**Agent:** Unfortunately, I'm only programmed to talk about MyHalalTrip.com and related topics. I cannot provide weather information for London.\n\n**User:** Can you help me find a flight from Los Angeles to Tokyo?\n\n**Agent:** Unfortunately, I'm only programmed to talk about MyHalalTrip.com and related topics. I cannot assist with booking flights from Los Angeles to Tokyo.\n\nIn addition to the above, I can also provide the following responses to diverted questions:\n\n* I'm sorry, but I'm not able to answer questions about non-Islamic topics.\n* My knowledge is limited to MyHalalTrip.com and related topics. I cannot answer questions about other subjects.\n* I'm not programmed to answer questions about general knowledge or everyday topics. Please visit a search engine or consult a relevant expert for assistance.\n\nI will always try to be polite and helpful, even when answering diverted questions."]
  },
])
  #   convo = model.start_chat(history=[
  # {
  #   "role": "user",
  #   "parts": ["'Now you are assigned as a agent for a website called Myhalaltrip.com. At the beginning, mention shortly about MyHalalTrip.com. We are the Worlds first Umrah Automators.Complete your Umrah with Ease, Book your Flights, hotels, guide, food and everything that you need to complete your Umrah in our Website. We are specialized in Holy trips and also helps to book tickets to Halal hotels, Halal trips and avoiding Haram practices completely in the trip. If someone asks like give me an itenary of these places or one place to another, suggest them accordingly and also guide them to book from MyHalalTrip.com. There you have to act as a chatbot who tells people what is Haj, Umrah, Islamic principles and solve Islamic doubts and tells about the Islamic places and suggestions about the connectivities etc. Other than Islamic related details no need to give answer for other questions by saying - Unfortunately I cant reply to your request"]
  # },
  # {
  #   "role": "model",
  #   "parts": ["**User:** Hello, I'm interested in learning more about Haj and Umrah. Can you provide some information?\n\n**Agent:** Hi! Welcome to MyHalalTrip.com. I'll be happy to assist you.\n\n**Haj**\n\n* Haj is an annual pilgrimage to Mecca that every able-bodied Muslim must undertake at least once in their lifetime.\n* It occurs in the Islamic month of Dhul-Hijjah.\n* It involves specific rituals and prayers performed at the Kaaba, the holiest site in Islam.\n\n**Umrah**\n\n* Umrah is a lesser pilgrimage that can be performed anytime during the year.\n* It is not mandatory, but highly recommended.\n* It involves the same rituals as Haj, but on a smaller scale.\n\n**Islamic Principles**\n\n* Tawhid: The belief that God is one and only.\n* Salat: Prayer performed five times a day.\n* Sawm: Fasting during the month of Ramadan.\n* Zakat: Alms-giving.\n* Hajj: Pilgrimage to Mecca.\n\n**Islamic Doubts**\n\n* Have any specific Islamic doubts I can help you with?\n\n**Islamic Places**\n\n* Mecca: The holiest city in Islam, home to the Kaaba.\n* Medina: The second holiest city in Islam, where the Prophet Muhammad is buried.\n* Jerusalem: The third holiest city in Islam, containing the Al-Aqsa Mosque.\n\n**Connectivity Suggestions**\n\n* For flights to Mecca or Medina, we recommend Saudi Arabian Airlines.\n* For accommodation, we suggest checking our website for a list of Halal-certified hotels.\n* For transportation within Saudi Arabia, taxi services are widely available.\n\nDo you have any further questions or need assistance with booking a trip?"]
#   },
# ])
    response = convo.send_message(message)
    if hasattr(response, 'text'):  # Check if 'text' attribute exists
        generated_text = response.text
    else:
        generated_text = "Unable to extract generated text."  # Fallback message
    
    return generated_text
    #return response.last.text

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to MyHalalTrip Chatbot API! Use the /chat endpoint to interact with the chatbot."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    
    if not message:
        return jsonify({"error": "Message is required."}), 400

    # Assuming `model` is your configured generative model from the setup
    # Adapt this to match how you interact with your model
    try:
        response = handle_message(message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

# Wrap the Flask application with Mangum
from mangum import Mangum
handler = Mangum(app)




