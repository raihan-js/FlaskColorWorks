from flask import Flask, request, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from color import detect_and_color_objects, get_model

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Loading the model (consider doing this outside request handling)
model = get_model()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Process the image here
            target_label = int(request.form['target_label'])
            rgb_color = tuple(map(int, request.form['rgb_color'].split(',')))
            output_filename = "processed_" + filename
            output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            
            detect_and_color_objects(filepath, target_label, rgb_color, model, output_filepath)

            return render_template('index.html', filename=filename, output_filename=output_filename)

@app.route('/display/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
