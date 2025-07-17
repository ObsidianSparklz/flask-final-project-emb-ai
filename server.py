from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response_dict = emotion_detector(text_to_analyze)
    dominant_emotion = response_dict.pop('dominant_emotion')
    score_strings = []
    for emotion, score in response_dict.items():
        score_strings.append(f"'{emotion}': {score}")
    
    formatted_scores = ", ".join(score_strings)

    return (
        f"For the given statement, the system response is {formatted_scores}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
