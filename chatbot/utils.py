# chatbot/utils.py
from .models import FAQ, SearchKeyword


class ChatbotProcessor:
    def find_best_match(self, message, language):
        """
        Encontra a melhor correspondência para a mensagem do usuário
        considerando FAQs e palavras-chave no idioma correto
        """
        message = message.lower().strip()

        # Primeiro tenta encontrar uma correspondência exata
        exact_match = FAQ.objects.filter(
            language=language,
            question__iexact=message
        ).first()

        if exact_match:
            return exact_match.answer

        # Tenta encontrar uma correspondência parcial
        partial_match = FAQ.objects.filter(
            language=language,
            question__icontains=message
        ).first()

        if partial_match:
            return partial_match.answer

        # Se não encontrar, procura por palavras-chave
        keywords = SearchKeyword.objects.filter(
            language=language
        ).values_list('keyword', flat=True)

        # Procura por palavras-chave na mensagem
        for keyword in keywords:
            if keyword.lower() in message:
                faq = FAQ.objects.filter(
                    language=language,
                    question__icontains=keyword
                ).first()

                if faq:
                    return faq.answer

        return None

    def get_default_response(self, language):
        """Retorna a resposta padrão no idioma especificado"""
        responses = {
            'pt': 'Desculpe, não consegui encontrar uma resposta específica. Por favor, acesse nossa página de contato para obter ajuda.',
            'en': 'Sorry, I couldn\'t find a specific answer. Please visit our contact page for assistance.',
            'es': 'Lo siento, no pude encontrar una respuesta específica. Por favor, visite nuestra página de contacto para obtener ayuda.'
        }
        return responses.get(language, responses['en'])

    def process_message(self, message, language='pt'):
        """
        Processa a mensagem do usuário e retorna uma resposta apropriada
        """
        # Procura a melhor correspondência
        response = self.find_best_match(message, language)

        # Se não encontrar correspondência, usa resposta padrão
        if not response:
            response = self.get_default_response(language)

        return {
            'response': response,
            'language': language,
            'found': bool(response != self.get_default_response(language))
        }
