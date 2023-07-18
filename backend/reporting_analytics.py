```python
from flask import Flask, jsonify, request
from database.db import get_db

app = Flask(__name__)

@app.route('/reporting', methods=['GET'])
def generateReport():
    db = get_db()
    user = request.args.get('user')
    agent = request.args.get('agent')

    # Fetch agent performance data
    agent_performance_data = db.execute(
        'SELECT * FROM agent_performance WHERE user_id = ? AND agent_id = ?',
        (user, agent)
    ).fetchall()

    # Fetch task outcome data
    task_outcome_data = db.execute(
        'SELECT * FROM task_outcomes WHERE user_id = ? AND agent_id = ?',
        (user, agent)
    ).fetchall()

    # Prepare the report
    report = {
        'agent_performance': [dict(row) for row in agent_performance_data],
        'task_outcomes': [dict(row) for row in task_outcome_data]
    }

    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)
```