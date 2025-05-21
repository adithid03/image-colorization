from flask import Flask, request, render_template, send_file, redirect, url_for
import os
import subprocess
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'images_input'
OUTPUT_FOLDER = 'images_output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    output_path = os.path.join(app.config['OUTPUT_FOLDER'], 'colored_out.png')

    try:
        subprocess.run(['./colorize_app', filepath], check=True)
        if not os.path.exists(output_path):
            return "Colorization failed: output file not found."

        return render_template('result.html', image_url=url_for('output_file'), download_url=url_for('download_file'))

    except subprocess.CalledProcessError:
        return "Error running colorize_app"

@app.route('/output')
def output_file():
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], 'colored_out.png'), mimetype='image/png')

@app.route('/download')
def download_file():
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], 'colored_out.png'),
                     mimetype='image/png',
                     as_attachment=True,
                     download_name='colorized_image.png')
@app.route('/developer')
def developer():
    return render_template('developer.html')


if __name__ == '__main__':
    app.run(debug=True)
