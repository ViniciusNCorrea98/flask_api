from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask('GlobalSolution01')
api = Api(app)

@app.route('/loading-nlp', methods=['POST'])
def ai_endpoint():
    data = request.json
    text = data.get('text')

    if not text:
        return jsonify({'error': "There's any data"}), 400

    #result = nlp_model(text)

    #return jsonify(result), 201

if __name__ == '__main__':
    app.run(debug=True)

