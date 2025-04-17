# data_pre_proccess/views.py
from django.shortcuts import render
from text_to_image.views import  image_to_txt # Import your extraction function
from NER.views import ner_logic # Ner data function
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
from text_sumarization.views import TextSummarizer
from topic_modeling.views import main_fun_topic_modeling

nltk.download('stopwords')
port_stem = PorterStemmer()
summarizer = TextSummarizer()



def data_pre_processing(request):
    extracted_text = ''
    stemmed_content = ''
    Ner_text = ''
    summarized_text = ''
    topic_model_result = []
    coherence_score = 0
    visualization = "" 
    
    if request.method == 'POST':
        # uploaded_image = request.FILES.get('image')  # Get the uploaded image from the request
        
        uploaded_image = request.FILES.get('textFile')
        
        if uploaded_image:
            # extracted_text = image_to_txt(uploaded_image)  # Extract text
            
            extracted_text = uploaded_image.read().decode('utf-8')
            
            Ner_op = ner_logic() # NER text
            Ner_text = Ner_op.build(extracted_text) 
            
            # Process the extracted text (e.g., stemming)
            stemmed_content = re.sub('[^a-zA-Z]', ' ', extracted_text)
            stemmed_content = stemmed_content.lower()
            stemmed_content = stemmed_content.split()
            stemmed_content = [port_stem.stem(word) for word in stemmed_content if word not in stopwords.words('english')]
            stemmed_content = ' '.join(stemmed_content)
            
            try:
                topicModeling_fun = main_fun_topic_modeling(extracted_text)

                topic_model_result, coherence_score, visualization = topicModeling_fun
            except ValueError as e:
                pass
            
            summarized_text = summarizer.summarize_text(extracted_text)
            
            
    
    return render(request, 'index_img_txt.html', {'text': extracted_text,
                                                  'stemmed_content': stemmed_content,
                                                  'Ner_text': Ner_text, 
                                                  'topic_model_result': topic_model_result ,
                                                  'coherence_score': coherence_score,
                                                  'summarized_text': summarized_text, 
                                                  'visualization': visualization })
