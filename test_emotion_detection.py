import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for the emotion_detector function from the EmotionDetection module.

    This class contains tests for various emotional responses based on input text.
    Each test checks if the detected emotion matches the expected emotion.
    """

    def check_emotion(self, input_text, expected_emotion):
        result = emotion_detector(input_text)
        self.assertEqual(
            max(result, key=result.get),
            expected_emotion
        )

    def test_joy_emotion(self):
        self.check_emotion(
            "I am glad this happened",
            'joy'
        )

    def test_anger_emotion(self):
        self.check_emotion(
            "I am really mad about this",
            'anger'
        )

    def test_disgust_emotion(self):
        self.check_emotion(
            "I feel disgusted just hearing about this",
            'disgust'
        )

    def test_sadness_emotion(self):
        self.check_emotion(
            "I am so sad about this",
            'sadness'
        )

    def test_fear_emotion(self):
        self.check_emotion(
            "I am really afraid that this will happen",
            'fear'
        )


unittest.main()
