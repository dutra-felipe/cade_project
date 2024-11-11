# chatbot/apps.py
from django.apps import AppConfig
import os


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def ready(self):
        try:
            import nltk
            # Defina um diretório personalizado para os dados do NLTK
            nltk_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'nltk_data')
            if not os.path.exists(nltk_data_dir):
                os.makedirs(nltk_data_dir)

            nltk.data.path.append(nltk_data_dir)

            try:
                nltk.data.find('tokenizers/punkt')
            except LookupError:
                nltk.download('punkt', download_dir=nltk_data_dir)

            try:
                nltk.data.find('corpora/stopwords')
            except LookupError:
                nltk.download('stopwords', download_dir=nltk_data_dir)
        except Exception as e:
            print(f"Error configuring NLTK: {str(e)}")
