import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = jsonobj, headers=header)
    print(response.text)
    formatted_response = json.loads(response.text)
    try:
        if response.status_code == 400:
            formatted_response = apply_none_condition(formatted_response['emotionPredictions'][0]['emotion'])
        return formatted_response
    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred while making the request: {e}"}

def apply_none_condition(d):
    for key, value in d.items():
            d[key] = None
    return d