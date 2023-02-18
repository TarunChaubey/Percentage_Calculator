from flask import Flask, render_template, url_for, request
import numpy as np

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
@app.route('/home',methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/result',methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        physics = request.form['physics']
        chemistry = request.form['chemistry']
        maths = request.form['maths']
        english = request.form['english']
        optional = request.form['optional']

        TotalMarks = int(physics) + int(chemistry) +int(maths) +int(english) +int(optional)
        Percentage = np.round((TotalMarks/500)*100,2)
        FinalResult = ('Pass' if Percentage>=65 else 'Fail')
        jdata = request.form.to_dict()
        return render_template('result.html',data=jdata, Percentage=Percentage, FinalResult=FinalResult)
    
    else:
        return render_template('result.html',data="Please Enter Valid Data")

if __name__ == "__main__":
    app.run(debug=True)