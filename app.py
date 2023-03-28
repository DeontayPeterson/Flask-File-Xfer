from flask import Flask, render_template, request, send_file
import os



app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/static"


@app.route('/')    
def index():
    files = os.listdir('static')
    return render_template('index.html',files=files )

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"static/{file.filename}")
    return "File uploaded!"

@app.route('/download')
def download():
    #all_files = os.listdir('static')
    filename = request.args.get('filename')
    return send_file(f"static/{filename}", as_attachment=True)

HOST = 'ip'
PORT = "PORT"

app.debug = True
app.run(host=HOST, port=PORT)