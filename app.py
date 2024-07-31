from flask import Flask, request, jsonify, render_template
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('wordnet')


app = Flask(__name__)

# Lemmatization class
class LemmaTokenizer(object):
    def __init__(self):
        self.wordnetlemma = WordNetLemmatizer()
    def __call__(self, reviews):
        return [self.wordnetlemma.lemmatize(word) for word in word_tokenize(reviews)]

# Load the model and vectorizer
with open('nlp_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review_text = data.get('review_text')
    if not review_text:
        return jsonify({'error': 'No review text provided'}), 400
    
    try:
        # Transform the review text using the loaded vectorizer
        review_vector = vectorizer.transform([review_text])
        
        # Make a prediction using the loaded model
        prediction = model.predict(review_vector)#[]  # Assuming model.predict() returns a list-like object
        
        # Return the prediction as a JSON response
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
