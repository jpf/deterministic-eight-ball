import sys
import requests

#url = 'http://localhost:5000/sms'
#url = 'http://ec2-54-248-154-115.ap-northeast-1.compute.amazonaws.com/sms.php'
url = sys.argv[1]

questions = {'Will I scream and shout?': 'Maybe',
             'Will I be successful?': 'Maybe',
             'Will I cry during Les Miserables?': 'Yes',
             'Will I catch stomach bug?': 'No',
             'Will I look good with blonde hair?': 'Yes',
             'Will I need an umbrella tomorrow?': 'No',
             'Will I run it?': 'Maybe',
             'Will I throw up?': 'Maybe',
             'Will I understand Assassins Creed?': 'No',
             'Will I win the lottery?': 'No',
             'Is the answer perhaps?': 'Perhaps',
             'Is the answer perhaps?????': 'No'
             }

print "Testing: %s ... " % url
for question in questions.keys():
    payload = {'Body': question}
    r = requests.post(url, data=payload)
    expect = "You asked: '%s', the answer is: '%s'\n" % (question,
                                                         questions[question])
    answer = r.text
    if answer != expect:
        print "Expected:\n%s\nGot:\n%s" % (expect, answer)
print "done."
