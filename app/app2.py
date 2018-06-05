import flask
from flask import request
import pickle
import datetime
from chart import logg_import as logg_import,logg_import2
# import matplotlib.pyplot as plt
import pandas as pd

# Initialize the app

app = flask.Flask(__name__)




# @app.route("/")
# def hello():
#     return """welcome"""


# Let's turn this into an API where you can post input data and get
# back output data after some calculations.

# If a user makes a POST request to http://127.0.0.1:5000/predict, and
# sends an X vector (to predict a class y_pred) with it as its data,
# we will use our trained LogisticRegression model to make a
# prediction and send back another JSON with the answer. You can use
# this to make interactive visualizations.

@app.route("/", methods=["POST", "GET"])
def predict():

    video_num = 263708483
    fail_1 = 0

    if (request.args):
        video_num = int(request.args.get('video_num')) or 263708483
        # fail_1 = int(request.args.get('myRange')) or 0

    # if (request.args):
    #     video_num = int(request.args.get('video_num')) or 0
    #     fail_1 = int(request.args.get('myRange')) or 0
    # else:
    #     video_num = 0
    #     fail_1 = 0
    #


    time_play=(datetime.timedelta(seconds=fail_1))
    fail_2= fail_1 * 30
    hour_play=fail_2//3600
    minute_play=(fail_2%3600) // 60
    second_play=(fail_2%3600)%60



    # group_seconds=logg_import(fail_1,video_num)
    df4,comments,df3=logg_import2(fail_1,video_num)
    df5= df4[pd.notnull(df4['outcome'])]

    return flask.render_template('predictor.html',
    data = df3.to_json(),
    data2=df4.to_json(),
    data3=df5.to_json(),
    word_data = comments,
    video_num =video_num  ,  min_time = 0, max_time =len(df3),max_time2 =len(df4)*30,
    fail_2=fail_2,

    )


# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:
app.run(debug=True)
app.run(host='0.0.0.0',port='8001')
# For public web serving:
# app.run(host='0.0.0.0')
