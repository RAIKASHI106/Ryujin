from flask import render_template
import sys, os
# ensure project root is on sys.path when running from scripts/
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import main

with main.app.app_context():
    out = render_template('index.html', movies=[])
    if out and 'LocalFlix' in out:
        print('RENDER_OK')
    else:
        print('RENDER_FAILED')
