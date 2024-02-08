import os
from flask import Flask, render_template, request, url_for
# from predictor import check,check2
from malariapredict import malar,checkmal
from chestpneumonia import pneumo,checklung
from eyepredict import check,checkeye
from predictor import checkbrain,check2
from heartdisease import *
author = 'TEAM DELTA'

app = Flask(__name__, static_folder="static")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/upload', methods=['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)
        ans3=checkeye(filename)
        if ans3==False:
            return render_template('random.html',image_name=filename)
        else:
            status1=check(filename)
            return render_template('completeeye.html', image_name=filename, predvalue=status1)
     
        
   
       
@app.route('/upload2', methods=['GET', 'POST'])
def upload2():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)
        ans2=checkmal(filename)
        if ans2==False:
            return render_template('random.html',image_name=filename)
        else:
            status1=malar(filename)
            return render_template('completemalaria.html', image_name=filename, predvalue=status1)
            
          
@app.route('/upload3', methods=['GET', 'POST'])
def upload3():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)
        ans2=checklung(filename)
        if ans2==False:
            return render_template('random.html',image_name=filename)
        else:
            status1=pneumo(filename)
            return render_template('completepneumo.html', image_name=filename, predvalue=status1)
       
    
@app.route('/uploadb', methods=['GET', 'POST'])
def uploadb():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        print(filename)
        dest = '/'.join([target, filename])
        print(dest)
        file.save(dest)
    
        status1=checkbrain(filename)
        return render_template('completebrain.html', image_name=filename, predvalue=status1)  
@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  return render_template('upload.html')

@app.route('/my-link2/')
def my_link2():
  print ('I got clicked!')
  return render_template('uploadmalaria.html')

@app.route('/my-link3/')
def my_link3():
  print ('I got clicked!')
  return render_template('uploadpneumo.html')

@app.route('/my-link4/')
def my_link4():
  print ('I got clicked!')
  return render_template('uploadbrain.html')

@app.route('/my-link69/')
def my_link69():
  print ('I got clicked!')
  return render_template('uploadbrain.html')

@app.route('/login')
def serve_login():
    return render_template('login.html')

@app.route('/admin')
def admin():
    print("BYR")
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/my-linkheart/')
def my_link_heart():
  print ('I got clicked!')
  return render_template('completeheart.html')


@app.route("/predict", methods = ["POST"])
def predict():
    if(request.method == "POST"):
        data = pd.read_csv("heart/heart.csv")
        X, y = data.values[:, 0:13], data.values[:, -1]
        clf = DecisionTree()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        clf.fit(X_train, y_train)
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = clf.predict(features)
        result = "Negative" if prediction == 0 else "Positive"
        return render_template("completeheart.html", prediction_text = result)


if __name__ == "main":
    app.run(port=4555, debug=True)
