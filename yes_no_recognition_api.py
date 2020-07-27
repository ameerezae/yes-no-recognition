import os
from flask import Flask, request
from flask_restplus import Resource, Api
from flask_cors import CORS
from werkzeug.utils import secure_filename
from common import yes_no_recognition

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)


@api.route('/yes_no_recognition')
class YesNoRecognition(Resource):
    def post(self):
        threshold = 20
        wav_file = request.files.get("audio-file")
        dst_path = os.path.join(uploads_dir, secure_filename(wav_file.filename))
        wav_file.save(dst=dst_path)
        result, feature_value = yes_no_recognition(dst_path, threshold)
        return {"result": result, "feature_value": feature_value}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)