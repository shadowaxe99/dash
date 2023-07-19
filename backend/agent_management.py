```python
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Agent(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    skills = Column(String)
    tasks = Column(String)
    performance_metrics = Column(Float)

class AgentSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    skills = fields.Str()
    tasks = fields.Str()
    performance_metrics = fields.Float()

agent_schema = AgentSchema()
agents_schema = AgentSchema(many=True)

@app.route('/agent', methods=['POST'])
def add_agent():
    name = request.json['name']
    skills = request.json['skills']
    tasks = request.json['tasks']
    performance_metrics = request.json['performance_metrics']

    new_agent = Agent(name, skills, tasks, performance_metrics)
    db.session.add(new_agent)
    db.session.commit()

    return agent_schema.dump(new_agent)

@app.route('/agent/<id>', methods=['PUT'])
def update_agent(id):
    agent = Agent.query.get(id)

    if 'name' in request.json:
        agent.name = request.json['name']
    if 'skills' in request.json:
        agent.skills = request.json['skills']
    if 'tasks' in request.json:
        agent.tasks = request.json['tasks']
    if 'performance_metrics' in request.json:
        agent.performance_metrics = request.json['performance_metrics']

    db.session.commit()

    return agent_schema.dump(agent)

@app.route('/agent/<id>', methods=['DELETE'])
def delete_agent(id):
    agent = Agent.query.get(id)
    db.session.delete(agent)
    db.session.commit()

    return {
        'message': f'Agent {agent.name} has been deleted'
    }

if __name__ == '__main__':
    app.run(debug=True)
```