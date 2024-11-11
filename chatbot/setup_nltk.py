# chatbot/setup_nltk.py
import nltk
import os


def setup_nltk():
    """Download required NLTK data"""
    try:
        # Define um diretório personalizado para os dados do NLTK
        nltk_data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'nltk_data')
        if not os.path.exists(nltk_data_dir):
            os.makedirs(nltk_data_dir)

        nltk.data.path.append(nltk_data_dir)

        # Download apenas os dados necessários
        nltk.download('stopwords', download_dir=nltk_data_dir, quiet=True)

        print("NLTK data downloaded successfully!")
        return True
    except Exception as e:
        print(f"Error downloading NLTK data: {str(e)}")
        return False


if __name__ == "__main__":
    setup_nltk()
