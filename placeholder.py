from flask import Flask
from flask import request
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def get_clients():
    print('connect')
    join_room('ZotBoard')

@socketio.on('message')
def send_drawing(drawing_msg):
    print('message')
    send(drawing_msg, room='ZotBoard')
    
if __name__ == '__main__':
    socketio.run(app)
