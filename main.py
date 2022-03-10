from flask import Flask,render_template,Blueprint,send_from_directory
from flask_cors import CORS



app = Flask(__name__, static_folder="dist/Demo-App/")
angular = Blueprint('angular',__name__,template_folder='dist/Demo-App/')
app.register_blueprint(angular)
CORS(app)





@app.route('/assets/<path:filename>')
def custom_static_for_assets(filename):
    return send_from_directory('dist/Demo-App/assets',filename)

@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('dist/Demo-App/',filename)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)