import os
import easyocr
import cv2
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)
reader = easyocr.Reader(["en"], gpu=True)

# Define the folder for saving uploaded images
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
            uploaded_file.save(image_path)
            results = reader.readtext(image_path)
            img = cv2.imread(image_path)
            for detect in results:
                t_left = tuple([int(val) for val in detect[0][0]])
                b_right = tuple([int(val) for val in detect[0][2]])
                text = detect[1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                img = cv2.rectangle(img, t_left, b_right, (0, 0, 255), 5)
                img = cv2.putText(img, text, t_left, font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

            # Save the annotated image
            annotated_image_path = os.path.join(app.config["UPLOAD_FOLDER"], "annotated_" + uploaded_file.filename)
            cv2.imwrite(annotated_image_path, img)

            return render_template("index.html", results=[result[1] for result in results], image_path=annotated_image_path)

    return render_template("index.html", results=[], image_path=None)

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
