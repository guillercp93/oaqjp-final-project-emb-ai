"""
This module provides a Flask web application for emotion detection
using a specified emotion detection model.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the provided text for emotional content.

    Returns:
        str: A response containing the emotional analysis of the input text.
        int: HTTP status code indicating the result of the request.
    """
    body = request.args.get('textToAnalyze')
    try:
        result = emotion_detector(body.strip())
        # Validate information
        if all(v is None for v in result.values()):
            return "Invalid text! Please try again!."

        # Convert to string and remove braces
        result_str = str(result).replace('{', '').replace('}', '')
        return f"For the given statement, the system response is {result_str}."
    except KeyError:
        return ('An error has ocurred!', 500)


@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
