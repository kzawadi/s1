from flask import Flask, request, jsonify

app = Flask(__name__)


def avg_abs_diff(answers1, answers2):
    # Calculate the average absolute difference between two sets of answers
    return sum(abs(a - b) for a, b in zip(answers1, answers2)) / len(answers1)


@app.route('/compare', methods=['POST'])
def compare():
    # Get the data from the POST request
    data = request.get_json(force=True)
    # Calculate the average absolute difference
    result = avg_abs_diff(data['answers1'], data['answers2'])
    # Return the result as JSON
    return jsonify(result)


if __name__ == '__main__':
    app.run()
