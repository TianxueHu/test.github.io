from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # get the uploaded file
        f = request.files['inputfile']
        basePath = os.path.dirname(__file__)
        uploadPath = os.path.join(basePath, 'static\\uploads', f.filename)
        # save the file to server
        f.save(uploadPath)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
