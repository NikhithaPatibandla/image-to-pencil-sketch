from flask import Flask, render_template, request, url_for
import os
from werkzeug.utils import secure_filename

from sketch import pencil_sketch_image
import config

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = config.RESULT_FOLDER

def allowed_file(filename):
    return (
        "." in filename 
        and filename.rsplit(".",1)[1].lower() in config.ALLOWED_EXTENSIONS
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", error="No file uploaded")
        
        file = request.files["image"]
        
        if file.filename == "":
            return render_template("index.html", error="No selected file")
        
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_path = os.path.join(app.config['RESULT_FOLDER'], filename)
            
            file.save(input_path)
            
            pencil_sketch_image(input_path, output_path)
            return render_template(
                "index.html",
                original_image= url_for("static", filename=f"uploads/{filename}"),
                sketch_image=url_for("static", filename=f"results/{filename}"),
                sketch_filename = filename
            )
        else:
            return render_template("index.html", error="File type not allowed")
        
    return render_template("index.html")


if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

    app.run(debug=True)