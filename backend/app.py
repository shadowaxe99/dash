```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import agent_dashboard
import real_time_communication
import nft_integration
import agent_management
import reporting_analytics
import user_interface
import performance
import security

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    user = User.query.filter_by(username=session['username']).first()
    agent_dashboard.loadDashboard(user)

@app.route('/communication')
def communication():
    real_time_communication.initiateCommunication()

@app.route('/nft')
def nft():
    nft_integration.tradeNFT()

@app.route('/agent-management')
def agent_management():
    agent_management.manageAgent()

@app.route('/reporting-analytics')
def reporting_analytics():
    reporting_analytics.generateReport()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            if security.authenticateUser(user, request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('dashboard'))
    return render_template('authentication.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```