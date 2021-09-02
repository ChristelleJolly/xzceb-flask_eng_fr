'''This module provides IBM Watson language Translator functionalities'''

import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Convert english_text to French'''
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]

def french_to_english(french_text):
    ''' Convert french_text to English'''
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]
