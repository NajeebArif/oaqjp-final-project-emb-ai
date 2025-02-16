import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    inputJson = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    emotion = {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion":None
            }
    response = requests.post(url, json = inputJson, headers=header)
    if response.status_code == 200:
        emotion = json.loads(response.text)['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion, key=emotion.get)
        emotion['dominant_emotion'] = dominant_emotion
    return emotion