from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from encypter import encryp, key_gen
from decrypter import decryp
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = ' '               #Senders mail server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ' '             #Senders mail id
app.config['MAIL_PASSWORD'] = ' '             #Senders mail id password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def back_home():
    return render_template('index.html')


@app.route('/upload')
def call_page_upload():
    return render_template('upload.html')


@app.route('/download/')
def downloads():
    return render_template('download.html')


@app.route('/encrypt_data', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        if f.filename == '':
            flash('No selected file')
            return 'NO FILE SELECTED'
        if f:
            filename = secure_filename(f.filename)
            email = request.form['mail']
            content = f.read()
            k = key_gen()
            e_data = encryp(content, k)
            with open(os.path.join(r"C:\Users\...",filename), 'w') as w:     #Path of location to store encrypted data
                w.write(e_data)

            msg = Message('Decryption key', sender=' ', recipients=[email])  #Senders mail id
            msg.html = "<b>Your decryption key:  <b>" + k.decode()
            mail.send(msg)

            return render_template('success.html')
        else:
            return 'Invalid File Format,ok !'


@app.route('/decrypt_data', methods=['GET', 'POST'])
def upload_key():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        if f.filename == '':
            flash('No selected file')
            return 'NO FILE SELECTED'
        if f:
            filename = secure_filename(f.filename)
            dec_content = f.read()
            k = request.form['key']
            data = decryp(dec_content, k)
            with open(os.path.join(r"C:\Users\....",filename), 'w') as w:    #Path of location to store decrypted data
                w.write(data)
            return render_template('restored.html')
        else:
            return 'Invalid File Format !'

if __name__ == '__main__':
    app.run(debug=True)