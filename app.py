from flask import Flask, render_template, request, jsonify, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'nexus_pc_secret_key_2026'

# Store user sessions
user_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name', '').strip()
    
    if not name:
        return jsonify({'success': False, 'message': 'Please enter your name'}), 400
    
    # Store session
    session_id = datetime.now().isoformat()
    user_sessions[session_id] = {
        'name': name,
        'login_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return jsonify({
        'success': True,
        'name': name,
        'session_id': session_id
    })

@app.route('/api/time')
def get_time():
    now = datetime.now()
    return jsonify({
        'time': now.strftime('%I:%M:%S %p'),
        'date': now.strftime('%A, %B %d, %Y')
    })

@app.route('/api/sessions')
def get_sessions():
    return jsonify(user_sessions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
