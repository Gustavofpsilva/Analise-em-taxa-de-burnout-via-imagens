import datetime
import cv2
import gradio as gr
from fer import FER
import tempfile
import os

def analyze_emotions_and_print(img):
    # Detector emotions
    detector = FER(mtcnn=True)
    detected_emotions = detector.detect_emotions(img)

    # Highest score emotions
    emotion, score = detector.top_emotion(img)

    # Print detected emotions
    print("Detected Emotions:")
    for face in detected_emotions:
        print(face)

    # Print highest emotion
    print("Highest Emotion:", emotion, "Score:", score)

    # Create a new text file
    with open('Emotion.txt', 'w') as txt_file:
        # Write date and time to text file
        txt_file.write("Date and hours: {}\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        # Write emotions and scores to text file
        txt_file.write("Emotions: {}\n".format(emotion))
        txt_file.write("Highest score: {}\n".format(score))

    return ", ".join([f"{e}: {s}" for e, s in detected_emotions[0].items()])

iface = gr.Interface(
    fn=analyze_emotions_and_print,
    inputs=gr.Image(),
    outputs=gr.Textbox(),
    live=True
)

iface.launch(share=True)
