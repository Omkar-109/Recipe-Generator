from boltiotai import openai
import os
from flask import Flask, render_template, request

GET_API_KEY=os.environ['GET_API_KEY']
openai.api_key = GET_API_KEY
default_items="Water, Oil, Salt"
def generate_recipe(components):

 response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
   "role": "system",
   "content": "You are a helpful assistant"
  }, {
   "role":
   "user",
   "content":
   f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, {default_items}"
  }])
 return response['choices'][0]['message']['content']


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():
 output = ""
 if request.method == 'POST':
  components = request.form['components']
  output = generate_recipe(components)
 return render_template('index.html',output=output,default_items=default_items)

@app.route('/generate', methods=['POST'])

def generate():
 components = request.form['components']
 return generate_recipe(components)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)