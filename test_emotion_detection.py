from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(seft):
        
        # Caso de prueba para la emocion alegria
        result_1 = emotion_detector('I am glad this happened')
        seft.assertEqual(result_1['dominant_emotion'], 'joy')
        # Caso de prueba para la emocion enojo
        result_2 = emotion_detector('I am really angry about this.')
        seft.assertEqual(result_2['dominant_emotion'], 'anger')
        # Caso de prueba para la emocion disgustado
        result_3 = emotion_detector('I feel disgusted just hearing about this.')
        seft.assertEqual(result_3['dominant_emotion'], 'disgust')
        # Caso de prueba para la emocion tristeza
        result_4 = emotion_detector('I am so sad about this')
        seft.assertEqual(result_4['dominant_emotion'], 'sadness')
        # Caso de prueba para la emocion miedo
        result_5 = emotion_detector('I am terrified that this will happen')
        seft.assertEqual(result_5['dominant_emotion'], 'fear')



unittest.main()