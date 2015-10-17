import os
import sys
from cStringIO import StringIO

from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = os.getenv('DEBUG', True)


@app.route('/')
def home():
    return render_template('index.html', content='')


@app.route('/test-numpy')
def test_numpy():
    import numpy as np
    return str(np.zeros([5, 5]))
    # old_stdout = sys.stdout
    # old_stderr = sys.stderr
    # sys.stdout = sys.stderr = test_output = StringIO()
    #
    # import numpy as np
    # np.test()
    #
    # sys.stdout = old_stdout
    # sys.stderr = old_stderr
    # return '<pre>{0}</pre>'.format(test_output.getvalue())


if __name__ == '__main__':
    app.run()
