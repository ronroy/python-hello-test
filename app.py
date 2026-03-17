from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python on Railway</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            h1 { font-size: 48px; margin-bottom: 20px; }
            p { font-size: 24px; }
            .info {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 10px;
                margin-top: 30px;
            }
        </style>
    </head>
    <body>
        <h1>🐍 Hello from Python on Railway! 🎉</h1>
        <p>Your Python Flask app is running on Railway.app FREE tier!</p>
        <div class="info">
            <p>Framework: Flask</p>
            <p>Language: Python 3</p>
            <p>Platform: Railway.app</p>
            <p>Status: ✅ Running Successfully</p>
        </div>
    </body>
    </html>
    '''

@app.route('/test')
def test():
    return {
        'message': 'Hello from Python API!',
        'status': 'success',
        'framework': 'Flask'
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
