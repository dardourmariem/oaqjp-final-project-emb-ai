from EmotionDetection.emotion_detection import emotion_detector
import unittest, json

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):        
        self.assertEqual(get_top_emotion('I am glad this happened'), 'joy')

        self.assertEqual(get_top_emotion('I am really mad about this'), 'anger')
        
        self.assertEqual(get_top_emotion('I feel disgusted just hearing about this'), 'disgust')
        
        self.assertEqual(get_top_emotion('I am so sad about this'), 'sadness')

        self.assertEqual(get_top_emotion('I am really afraid that this will happen'), 'fear')

def get_top_emotion(text):
    result = json.loads(emotion_detector(text))
    print(result) 
    return max(result['emotionPredictions'][0]['emotion'], key=result['emotionPredictions'][0]['emotion'].get)

unittest.main()
