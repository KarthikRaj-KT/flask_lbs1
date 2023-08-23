from flask import Flask , render_template, request
import weight_predict 
app=Flask(__name__)
@app.route('/', method = ['GET','POST'])
def hello():
    if request.method == 'POST':
        height = request.form['height']
        print(height)
        weight = weight_predict.prediction([[float(height)]])
        return render_template('index.html',hei = height,wei = weight)
    return render_template('index.html')
if __name__=="main__":
    app.run(port=3008)