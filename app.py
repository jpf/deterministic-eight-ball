import hashlib
import struct
import os
from flask import Flask, request, Response

app = Flask(__name__)


class Deterministic:
    def seed(self, input):
        byte = struct.unpack('8H', hashlib.md5(input).digest())[0]
        two_bits = byte >> 14
        self.decision = two_bits

    def choice(self, input_array):
        return input_array[self.decision]


@app.route("/sms.php", methods=['POST'])
def answer_for():
    question = request.form['Body']
    answers = ['Yes', 'No', 'Maybe', 'Perhaps']
    determine = Deterministic()
    determine.seed(question)
    answer = determine.choice(answers)
    rv = ("<Response><Sms>"
          "You asked: '%s', the answer is: '%s'"
          "</Sms></Response>\n") % (question, answer)
    return Response(rv, mimetype='text/xml')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)
