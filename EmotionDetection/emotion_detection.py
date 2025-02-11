"""
This module provides functionality to detect emotions in text using
the Watson Emotion API.
"""

import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using the Watson Emotion API.

    Parameters:
    text_to_analyze (str): The text for which emotions need to be analyzed.

    Returns:
    dict: The response from the API containing the emotion analysis results.
    """
    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json={"raw_document": {"text": text_to_analyze}}
        )
        response.raise_for_status()  # Raise an error for bad responses

        data_json = response.json()
        data = data_json['emotionPredictions'][0]['emotion']
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        if e.response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None
            }
        return {}
    except KeyError as e:
        print(f"Different response: {e}")
        return {}
