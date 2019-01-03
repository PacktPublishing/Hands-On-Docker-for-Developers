from flask import render_template, Flask
import random
app = Flask(__name__)

kinds = {1: chr(0x1F308), 2: chr(0x1F984), 3: chr(0x1F308)+chr(0x1F984)}
start_over = False
retries_num = 0

def give_me_a_rainbow_unicorn():
 r = random.randint(1,3)
 return kinds[r]

@app.route('/')
def hello_world():
    global start_over
    global retries_num
    if start_over:
        retries_num = 0
    else:
        retries_num += 1
    kind=give_me_a_rainbow_unicorn()
    if kind == 'Rainbow Unicorn':
        start_over = True
    else:
        start_over = False
    return render_template('form.html', kind=kind, retries_num=retries_num)
