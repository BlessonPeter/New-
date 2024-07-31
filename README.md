 # nlp task on flipkart reviews

 Project Title: Sentiment Analysis on Flipkart Reviews using XGBOOST algorithm 

Dataset: The dataset consists of over 3000 reviews scraped from more than 300 pages of the Flipkart e-commerce website for the Firebolt Smartwatch product, using custom Python code. The dataset contains 3 features:

- Review Rating (numerical)
- Review Title (string)
- Review Body (string)

Additionally, the dataset includes reviews with 5 levels of rarity, providing a diverse range of opinions and sentiments.

Goal: The objective of this project is to develop a prediction model that analyzes the sentiment in a given review and classifies it as either positive or negative.

Methodology:

- Data Preprocessing:
    - Removed emojis, unnecessary characters, and symbols using Python libraries like Regex.
    - Performed lemmatization, tokenization, and bag-of-words transformation using NLTK and Spacy.
    - Converted text data into numerical features using CountVectorizer and TfidfVectorizer.
- Feature Extraction:
    - Utilized Word2Vec to capture semantic relationships between words.
- Modeling:
    - Explored various machine learning algorithms, including KNN, Bagging, Boosting, and XGBoost.
    - Hyperparameter tuning was performed to optimize model performance.
- Evaluation Metrics: Accuracy, Precision, and Recall were used to evaluate the model's performance.

Deployment:

- The trained model was deployed using Python Flask framework to create a RESTful API.
- The API allows for easy integration with web applications and cloud platforms like AWS, Azure, etc.
- The API endpoint accepts review text as input and returns the predicted sentiment (positive or negative).

Results:

- Training Accuracy: 96%
- Testing Accuracy: 97.5%

Conclusion: This project demonstrates the effectiveness of sentiment analysis on e-commerce reviews using machine learning techniques. The XGBoost model achieved high accuracy in classifying reviews as positive or negative, showcasing its potential applications in customer feedback analysis and product recommendation systems. The large and diverse dataset, combined with the deployment of the model using Flask and its potential for cloud deployment, make this a robust and scalable solution.

Extracting customer reviews on a product ( around 1000 reviews),
doing sentiment analysis, and then building a classification model to predict the
sentiment.
 
 
   ## Data Set Details: 
   
Data contains 3211 reviews with mostly 5 and 1 stared reviews

data scraped for the product firebolt smartwatch from Flipkart




## requirements
Flask==3.0.3
requests==2.26.0
numpy== 1.24.0
scikit-learn==1.3.2



## how to set up and execute-----

create virtual environment for installing only nessessary packages we needed and also for smooth running,

1. open anaconda promnt:-

    conda create -n nlp python==3.8 -y     

2. go to the particular directory of the code and activate the environment by,

 conda activate nlp
     

3. installing requried libraries by requirements.txt file,

    pip install -r requirements.txt

4. finally run the app.py in anaconda prompt by
    
    python app.py 

    (copy the localhost address and paste link on your google chrome and run)


try using different inputs inorder to predict the Energy Production 


Author:
License This project is licensed under the MIT License. Feel free to use and modify the code as needed.

Contributor #bn

### THANK YOU FELLOW DEVELOPERS