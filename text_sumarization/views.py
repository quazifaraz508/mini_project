from django.shortcuts import render

# Create your views here.
from transformers import pipeline


class TextSummarizer:
    def __init__(self, max_token_length=900, model="facebook/bart-large-cnn", device=-1):
    
        self.max_token_length = max_token_length
        self.summarizer = pipeline("summarization", model=model, device=device)
    
    def chunk_text(self, text):
       
        sentences = text.split('. ')
        chunks = []
        current_chunk = []
        current_length = 0

        for sentence in sentences:
            sentence_length = len(sentence.split())
            if current_length + sentence_length > self.max_token_length:
                chunks.append('. '.join(current_chunk) + '.')
                current_chunk = [sentence]
                current_length = sentence_length
            else:
                current_chunk.append(sentence)
                current_length += sentence_length

        if current_chunk:
            chunks.append('. '.join(current_chunk) + '.')

        return chunks
    
    def summarize_chunks(self, text_chunks):
       
        summaries = []
        for chunk in text_chunks:
            try:
                summary = self.summarizer(chunk, do_sample=False)[0]["summary_text"]
                summaries.append(summary)
            except Exception as e:
                print(f"Error summarizing chunk: {e}")
                summaries.append("Error in summarizing this chunk.")
        
        final_summary = "\n\n".join(summaries)
        return final_summary

    def summarize_text(self, input_text):
      
        text_chunks = self.chunk_text(input_text)
        final_summary = self.summarize_chunks(text_chunks)
        return final_summary
