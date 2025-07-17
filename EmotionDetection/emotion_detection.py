import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or not isinstance(text_to_analyse, str) or text_to_analyse.strip() == "":
        return None
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    try:
        response = requests.post(url, json = myobj, headers=header)
        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotion_scores = formatted_response['emotionPredictions'] [0] ['emotion']
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion
            return emotion_scores
        elif response.status_code == 400:
            return None
    except (requests.exceptions.RequestException, KeyError, IndexError):
        return None
