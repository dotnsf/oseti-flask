# -*- coding: utf-8 -*-
import oseti

from flask import *

app = Flask(__name__)

@app.route( "/" )
def main():
    return "Hello, World!"
    
@app.route( "/np" )
def negaposi():
    analyzer = oseti.Analyzer()
    text = ''
    if request.method == 'GET':
        text = request.args.get('text')
    else:
        text = request.form['text']

    ret = analyzer.analyze_detail( text )  # [ {'positive': [ '美味しい' ], 'negative': [], 'score': 1.0 } ]
    return jsonify( ret )

if __name__ == "__main__":
    app.run( debug=True, host='0.0.0.0', port=8080, threaded=True )

