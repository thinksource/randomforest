from flask import Flask, current_app
from flask import request
from flask import render_template
from myforest import *
import numpy as np

import os
basedir = os.path.join(os.path.dirname(os.path.abspath(".")),"randomforest")

app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'))
with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name+" running.")

# my_loader = jinja2.ChoiceLoader([
#         app.jinja_loader,
#         jinja2.FileSystemLoader(['/flaskapp/userdata',
#                                  '/flaskapp/templates']),
#     ])

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        var1 = request.form['VAR1']
        var2 = request.form['VAR2']
        var3 = request.form['VAR3']
        var4 = datatype(request.form['VAR4'])
        var5 = datatype(request.form['VAR5'])
        var6 = datatype(request.form['VAR6'])
        var7 = datatype(request.form['VAR7'])
        var8 = datatype(request.form['VAR8'])
        var9 = datatype(request.form['VAR9'])
        var10 = datatype(request.form['VAR10'])
        var=np.asarray([var4,var5,var6,var7,var8,var9,var10,var1,var2,var3]).reshape(1,-1)
        print(var)
        model=app.config["model"]
        result=model.predict(var)
        prodict=model.predict_proba(var)
        return render_template("result.html", result=result, prodict="{0:.1f}%".format(prodict[0][0]*100))

if __name__ == '__main__':
    df=getdataframe()
    #data,target=np.split(df.values, (10,), axis=1)
    a, target = np.split(df.values, (10,), axis=1)
    #x_train, x_test, y_train, y_test = train_test_split(data, target.reshape(-1), test_size=0.3, random_state=1)
    model=RandomForestClassifier(n_estimators=200, max_features=4,criterion='gini')
    rf_clf=model.fit(a, target.reshape(-1))
    procentage="{0:.1f}%".format(rf_clf.score(a, target.reshape(-1))*100)
    print("The Random Forest prodict accuracy procentage:"+procentage)
    app.config["model"]=rf_clf
    app.config["tt"] = "erer"
    #re=predictrate(x_test, y_test.reshape(-1), rf_clf)
    app.run()
