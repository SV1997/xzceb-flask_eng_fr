'''this module provide translation service'''
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
APIKEY="o-Ifr0LmPr39QA-6r1LSHB4-S_E1T48B1srZBYJJ5EYt"
URL='''https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/a70261ee-0e59-4e9e-b460-3b7b0380c985'''
authenticator=IAMAuthenticator(APIKEY)
translator=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
translator.set_service_url(URL)
def en2fr(mess):
    '''
    This function translate english to french
    '''
    # mess=input("enter text: ")
    mess=[mess]
    translation=translator.translate(text=mess,model_id='en-fr').get_result()
    return translation['translations'][0]['translation']
def fr2en(mess):
    '''
       This function translate french to english
    '''
    # mess = input("enter text: ")
    mess=[mess]
    translation = translator.translate(text=mess, model_id='fr-en').get_result()
    return translation['translations'][0]['translation']

# text=input("enter text: ")
# C=en2fr('Hello')
# print(type(C))
# C=str(C)
# fr2en(C)
