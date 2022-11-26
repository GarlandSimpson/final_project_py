"""Basic French to English and English to French Translator using Watson"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['APIKEY']
url = os.environ['URL']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-20',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    """Converts English text to French"""
    if english_text == "":
        return ""

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation["translations"]
    french_text = french_text[0]
    return french_text["translation"]


def french_to_english(french_text):
    """Converts French to English"""
    if french_text == "":
        return ""

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation["translations"]
    english_text = english_text[0]
    return english_text["translation"]
