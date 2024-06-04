import google.generativeai as genai
import os
from dotenv import load_dotenv

#getting the key from the env file
load_dotenv()
key = os.getenv("API_KEY")
genai.configure(api_key=key)

class gossip:
    def gettingRes(self, querry):
            try:
                model = genai.GenerativeModel(model_name= 'gemini-1.5-flash')
                response = model.generate_content(querry)
                res = response.text
                return res
            except:
                 res = self.gettingRes(querry)
                 return res