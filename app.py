import sys
import hashlib
import struct


class Deterministic:
    def seed(self, input):
        byte = struct.unpack('8H', hashlib.md5(input).digest())[0]
        two_bits = byte >> 14
        self.decision = two_bits

    def choice(self, input_array):
        return input_array[self.decision]


def answer_for(question):
    answers = ['Yes', 'No', 'Maybe', 'Perhaps']
    determine = Deterministic()
    determine.seed(question)
    answer = determine.choice(answers)
    return "You asked: '%s', the answer is: '%s'" % (question, answer)

print answer_for(sys.argv[1])
