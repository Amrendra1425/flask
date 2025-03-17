from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/welcome')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the score is " +str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        
        

        #return redirect(url_for(result,score=average_marks))


        return render_template('results.html',results=average_marks)


if __name__=='__main__':
    app.run(debug=True)
