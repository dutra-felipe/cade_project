# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FAQ
from .utils import ChatbotProcessor
import json

def chatbot_page(request):
    """
    Render the chatbot interface with predefined questions
    """
    language = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'pt'
    
    predefined_faqs = FAQ.objects.filter(
        is_predefined=True,
        language=language
    ).order_by('order', 'question')

    return render(request, 'chatbot.html', {
        'predefined_faqs': predefined_faqs
    })

@csrf_exempt
def chatbot_api(request):
    """API endpoint for chatbot interactions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            language = data.get('language', 'pt')
            
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)
            
            # Usar o ChatbotProcessor para processar a mensagem
            processor = ChatbotProcessor()
            result = processor.process_message(user_message, language)
            
            return JsonResponse(result)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'language': language,
                'response': processor.get_default_response(language)
            }, status=500)
            
    return JsonResponse({'error': 'Method not allowed'}, status=405)