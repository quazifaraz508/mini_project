from django.shortcuts import render
from .models import image_to_txt_convert
import pytesseract
from PIL import Image
# Create your views here.


# def image_to_txt(request):
#     text = ''
#     if request.method == 'POST':
        
#         try:
#             # image_instance = image_to_txt_convert.objects.first()
#             image_instance = request.FILES.get('image')
#             if image_instance:
#                 image = Image.open(image_instance)
                
#                 text = pytesseract.image_to_string(image)
#             else:
#                 text = 'No image found'
#         except Exception as e:
#             text = f"Error occurred: ' + {str(e)}"
#     return render(request, 'index_img_txt.html', {'texts': text})


def image_to_txt(image_file):
    # Open the image using Pillow
    image = Image.open(image_file)
    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text