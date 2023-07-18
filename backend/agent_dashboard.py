```python
from flask import Flask, render_template, request
from database import db, UserSchema, AgentSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

@app.route('/dashboard', methods=['GET'])
def loadDashboard():
    user_id = request.args.get('user_id')
    user = UserSchema.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    agents = AgentSchema.query.filter_by(user_id=user_id).all()
    agent_data = [agent.to_dict() for agent in agents]

    return render_template('dashboard.html', user=user.to_dict(), agents=agent_data)

if __name__ == "__main__":
    app.run(debug=True)
```