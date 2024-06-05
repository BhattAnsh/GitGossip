import google.generativeai as genai
import os
from dotenv import load_dotenv

#getting the key from the env file
load_dotenv()
key = os.getenv("API_KEY")
genai.configure(api_key=key)

class Gossip:
    def gettingRes(self, querry):
            try:
                model = genai.GenerativeModel(model_name= 'gemini-pro')
                response = model.start_chat(history=[])
                res = response.send_message(querry)
                return res.text
            except:
                 res = response.send_message(querry)
                 return res.text