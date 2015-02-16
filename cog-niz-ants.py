# Turn this to false when it's "finished"
DEBUG_SETTING = True

# This is the web server
from flask import Flask
app = Flask(__name__)
app.debug = DEBUG_SETTING
# Import the ability to render templates
from flask import render_template, json, make_response

# Import a random function
from random import random as rand
# Import datetime for non-cached response
from datetime import datetime

def updateLoc(botLoc):
  botLoc["cx"] += ((0.5-rand())/10.0)
  botLoc["cy"] += ((0.5-rand())/10.0)
  return botLoc

# Create an initial array of automatons
locArray = [{"cx":rand(), "cy":rand(), "r":10*rand()} for i in xrange(100)]

@app.route("/")
def hello():
  return render_template('output.html', name="PANTS")

@app.route("/botLocJson")
def dataLink():
  global locArray
  currentLoc = locArray
  locArray = [updateLoc(bot) for bot in locArray]
  response =  make_response(json.dumps(currentLoc))
  response.headers['Last-Modified'] = datetime.now()
  response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
  response.headers['Pragma'] = 'no-cache'
  response.headers['Expires'] = '-1'
  return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("6020"))
