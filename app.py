from flask import Flask, render_template, request, send_from_directory, url_for
from detect import *
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import os
import glob

app=Flask(__name__)
app.config['SECRET_KEY']='asldfkjlj'
app.config['UPLOADED_PHOTOS_DEST']='test'
app.config['RESULT_PHOTOS_DEST']='res_img'

photos = UploadSet('photos' , IMAGES)
configure_uploads(app, photos)

upload_btn=True

def run_dec():
    start_det()
    
    temp=isCavityPresent()
    if temp==True:
        print("Cavity Detected")
    else:
        print("No cavity!!!")
        
    return(temp)

class ShowRes(FlaskForm):
    submit = SubmitField('Show Result')

class UploadForm(FlaskForm):
        photo = FileField( 
            validators=[
                FileAllowed(photos, 'Only images are allowed'),
                FileRequired('File Field should not be empty')
            ]
        )
        submit = SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/res_img/<filename>')
def get_file2(filename):
    return send_from_directory(app.config['RESULT_PHOTOS_DEST'], filename)


@app.route('/', methods=['GET','POST'])
def upload_image():
    global upload_btn 
    form = UploadForm()
    ShowForm = ShowRes()
    if form.validate_on_submit():
        clr_folder("./test/*")
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file' , filename=filename)
        print(file_url)
        upload_btn=False
    else:
        file_url = None
    
    return render_template('index.html', form=form, file_url = file_url , upload_btn = upload_btn) 
    #return('Hello World')
    
@app.route('/res', methods=['GET','POST'])
def res():
    cavity=None
    cavity=run_dec()
    file_url = url_for('get_file2' , filename='result.png')
    return render_template('result.html', file_url = file_url , cavity = cavity )
    

#Define function to clear the specified dir(folder)
def clr_folder(folder_path):
  files = glob.glob(folder_path)
  for f in files:
    os.remove(f)

@app.route('/Admin')
def fun():
    return("Welcome Tanmay Bhosale and team")

if __name__ == '__main__':
    app.run(debug=True, port=8080)
