from flask import Flask , request , jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
        data = request.json
        text = data.get("text", "")
        if not text:
                return jsonify({'error': 'No text provided'}), 400
        
        analysis = TextBlob(text).sentiment
        response = {
		"polarity": analysis.polarity,
		"subjectivity": analysis.subjectivity,
	}
        return jsonify(response)

@app.route('/', methods=['GET'])
def hello():
        return 'Hello World!'

if __name__ == '__main__':
        app.run(debug=True)