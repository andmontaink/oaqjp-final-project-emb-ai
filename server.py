from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

# Uso de lista de emociones
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]

@app.route("/emotionDetector")

def sent_detector():

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Emocion dominante
    emotion_name = response['dominant_emotion']

    # String con todas las emociones
    all_scores = ", ".join([f"'{emo}': {response[emo]}" for emo in EMOTIONS])
    
    # Resultado final
    result_text = (f"Para la declaración dada, la respuesta del sistema es {all_scores}. "
        f"La emoción dominante es {emotion_name}. ")
    
    if response ['dominant_emotion'] is None:
        return " ¡Texto inválido! ¡Por favor, inténtalo de nuevo!."
    else:
        return result_text
        
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)