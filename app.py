from flask import Flask, render_template, request
from utils import extract_text
from scorer import calculate_score
from ai import generate_ai_feedback
from database import create_database, save_analysis
import os

app = Flask(__name__)

# Create database
create_database()

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------------- HOME PAGE ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- UPLOAD RESUME ---------------- #

@app.route("/upload", methods=["POST"])
def upload():

    # Check if a file is uploaded
    if "resume" not in request.files:
        return "No file selected."

    file = request.files["resume"]

    # Check empty filename
    if file.filename == "":
        return "Please select a PDF file."

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from PDF
    resume_text = extract_text(filepath)

    # Calculate ATS score
    score, feedback, category_scores = calculate_score(resume_text)

    # Generate AI Review
    ai_feedback = generate_ai_feedback(resume_text)

    # Save into database
    save_analysis(
        file.filename,
        score,
        str(ai_feedback)
    )

    # Show result page
    return render_template(
        "result.html",
        filename=file.filename,
        score=score,
        feedback=feedback,
        category_scores=category_scores,
        ai_feedback=ai_feedback
    )

# ---------------- RUN APP --------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))