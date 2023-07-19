```python
import socketio
from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

users = {}  # Dictionary to store user socket sessions

@socketio.on('connect')
def handle_connect():
    print('User connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')

@socketio.on('newAgent')
def handle_new_agent(data):
    emit('newAgent', data, broadcast=True)

@socketio.on('newNFT')
def handle_new_nft(data):
    emit('newNFT', data, broadcast=True)

@socketio.on('taskUpdate')
def handle_task_update(data):
    emit('taskUpdate', data, broadcast=True)

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
```