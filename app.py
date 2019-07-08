from flask import Flask  
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__, static_url_path='/static')

# a route to display our html page gotten from [react-chat-widget](https://github.com/mrbot-ai/rasa-webchat)
@app.route("/")
def index():  
    return render_template('index.html')

# run the application
if __name__ == "__main__":  
    app.run(debug=True)