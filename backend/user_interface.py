```python
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from .agent_dashboard import loadDashboard
from .security import authenticateUser

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
@authenticateUser
def index():
    user = request.args.get('user')
    dashboard_data = loadDashboard(user)
    return render_template('index.html', user=user, dashboard_data=dashboard_data)

@app.route('/dashboard')
@authenticateUser
def dashboard():
    user = request.args.get('user')
    dashboard_data = loadDashboard(user)
    return render_template('dashboard.html', user=user, dashboard_data=dashboard_data)

@app.route('/communication')
@authenticateUser
def communication():
    user = request.args.get('user')
    return render_template('communication.html', user=user)

@app.route('/nft')
@authenticateUser
def nft():
    user = request.args.get('user')
    return render_template('nft.html', user=user)

@app.route('/agent_management')
@authenticateUser
def agent_management():
    user = request.args.get('user')
    return render_template('agent_management.html', user=user)

@app.route('/reporting_analytics')
@authenticateUser
def reporting_analytics():
    user = request.args.get('user')
    return render_template('reporting_analytics.html', user=user)

@app.route('/authentication')
def authentication():
    return render_template('authentication.html')

@app.route('/encryption')
@authenticateUser
def encryption():
    user = request.args.get('user')
    return render_template('encryption.html', user=user)

if __name__ == '__main__':
    socketio.run(app)
```