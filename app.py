from flask import Flask, render_template, request

app = Flask(__name__, static_folder="./static")





@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        return render_template('submissionForm.html', templates='templates')
    else:
        return render_template('hello.html', templates='templates')
#fsisfd
#sdkjfklsdjlfsd
#oeiuwoepq
#djssdjf
#ksjflfg

@app.route('/home')
def home():
    return render_template('submissionForm.html', templates='templates')



@app.route('/api')
def api():
    #pandas code
    pass

# main driver function
if __name__ == '__main__':
    
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()