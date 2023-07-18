```python
import time
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    skills = db.Column(db.String(120))
    tasks = db.Column(db.String(120))
    performance_metrics = db.Column(db.String(120))

class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/performance', methods=['GET'])
def get_performance():
    start_time = time.time()
    users = User.query.all()
    agents = Agent.query.all()
    nfts = NFT.query.all()
    end_time = time.time()
    execution_time = end_time - start_time
    return jsonify({'execution_time': execution_time, 'users': len(users), 'agents': len(agents), 'nfts': len(nfts)})

if __name__ == '__main__':
    app.run(debug=True)
```