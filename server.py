from flask import Flask, request
import os
import predict
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        static_file = request.files['the_file']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system

        file_p = 'files/temp.wav'
        static_file.save(file_p)

        pred = predict.predict(file_p)
        os.remove(file_p)
        return pred


if __name__ == "__main__":
    app.run(host='10.0.55.170',ssl_context='adhoc')