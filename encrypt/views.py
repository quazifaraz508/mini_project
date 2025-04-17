from django.db import models
from django.http import HttpResponse , HttpResponseRedirect 
from django.shortcuts import redirect , render

import random
import string
import os

def generate_codes():
    """Generate random alphanumeric codes for each alphabet and digit"""
    code = {}
    for char in "QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnopqrstuvwxyz1234567890.+*-/?[];:',.}{|<>!@#$%^&()=":
        code[char] = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
    
    code[' '] = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
    
    return code

def save_codes(username, code):
    """Save the codes to a file specific to the user"""
    filename = f"codes_{username}.txt"
    with open(filename, "w") as f:
        for char, code_char in code.items():
            if char == ' ':  # special case for the space character
                f.write(f"space:{code_char}\n")  # store space as 'space'
            else:
                f.write(f"{char}:{code_char}\n")

def load_codes(username):
    """Load the codes from a file specific to the user"""
    filename = f"codes_{username}.txt"
    if not os.path.exists(filename):
        return None
    code = {}
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) == 2:
                char_code, code_char = parts
                if char_code == 'space':  # handle space correctly by checking for 'space'
                    code[' '] = code_char  # map space key to the actual space character
                else:
                    code[char_code] = code_char
            else:
                print(f"Skipping invalid line: {line}")
    return code

def encode(code, user_input):
    """Encode a string using the codes"""
    encoded_string = ""
    for char in user_input:
        encoded_string += code.get(char, "")  # handles space automatically if ' ' is in code
    return encoded_string

def decode(code, encoded_string):
    """Decode a string using the codes"""
    decoded_string = ""
    for i in range(0, len(encoded_string), 6):
        encoded_char = encoded_string[i:i+6]
        decoded_char = next((char for char, code_char in code.items() if code_char == encoded_char), '?')
        decoded_string += decoded_char
    return decoded_string

from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import os

def encoder_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        choice = request.POST.get('choice')
        user_input = request.POST.get('user_input')

        # Handle file upload
        uploaded_file = request.FILES.get('file_upload')

        # Load the codes for the user
        code = load_codes(username)
        if not code:
            code = generate_codes()
            save_codes(username, code)

        # If a file is uploaded
        if uploaded_file:
            # Save the uploaded file
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)  # Get the actual file path for reading

            # Read the content of the uploaded .txt file
            with open(file_path, 'r') as file:
                file_content = file.read()

            # If user chose to encode the file
            if choice == '1':  # Encode
                encoded_content = encode(code, file_content)
                # Generate file for download
                response = HttpResponse(encoded_content, content_type='text/plain')
                response['Content-Disposition'] = f'attachment; filename="encoded_file.txt"'
                return response

            # If user chose to decode the file
            elif choice == '2':  # Decode
                decoded_content = decode(code, file_content)
                # Generate file for download
                response = HttpResponse(decoded_content, content_type='text/plain')
                response['Content-Disposition'] = f'attachment; filename="decoded_file.txt"'
                return response
            else:
                return render(request, 'index.html', {'error': "Invalid choice. Please try again."})

        # If no file is uploaded, use the user input for encoding/decoding
        elif user_input:
            if choice == '1':  # Encode
                encoded_string = encode(code, user_input)
                # Generate file for download
                response = HttpResponse(encoded_string, content_type='text/plain')
                response['Content-Disposition'] = f'attachment; filename="encoded_string.txt"'
                return response
            elif choice == '2':  # Decode
                decoded_string = decode(code, user_input)
                # Generate file for download
                response = HttpResponse(decoded_string, content_type='text/plain')
                response['Content-Disposition'] = f'attachment; filename="decoded_string.txt"'
                return response
            else:
                return render(request, 'index.html', {'error': "Invalid choice. Please try again."})

    return render(request, 'index.html')


def download_decode(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        choice = request.POST.get('choice')
        
        # Load the codes for the user
        code = load_codes(username)
        if not code:
            code = generate_codes()
            save_codes(username, code)

        # If user chose to encode the Ner_text
        if choice == '1' and 'Ner_text' in request.POST:
            ner_text = request.POST.get('Ner_text')  # Assume Ner_text is passed via POST
            encoded_ner_text = encode(code, ner_text)
            # Generate file for download
            response = HttpResponse(encoded_ner_text, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="encoded_ner_text.txt"'
            return response
        
    return render(request, 'encode_download.html', {'Ner_text': 'Some NER Text'})
        
