from flask import Flask, request, jsonify, render_template
# Enable CORS to allow frontend-backend communication (e.g., during development)
from flask_cors import CORS
from models import session, User, Task
import datetime

app = Flask(__name__)
CORS(app)

# Serve the login/signup page
@app.route("/")
def home():
    return render_template("login.html")

# Serve the task dashboard (requires user_id in query param)
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ------------------------------
# AUTH API
# ------------------------------
@app.post("/register")
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    existing = session.query(User).filter_by(username=username).first()
    if existing:
        return jsonify({"error": "Username already exists"}), 400

    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    return jsonify({"message": "Registered successfully", "user_id": user.id})

@app.post("/login")
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"error": "Invalid credentials"}), 401

# ------------------------------
# TASK API
# ------------------------------
@app.get("/tasks/<int:user_id>")
def get_tasks(user_id):
    tasks = session.query(Task).filter_by(user_id=user_id).all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "details": task.details,
        "deadline": task.deadline.strftime("%Y-%m-%d") if task.deadline else None,
        "completed": task.completed
    } for task in tasks])

@app.post("/tasks")
def add_task():
    data = request.json
    title = data.get("title")
    details = data.get("details", "")
    deadline = data.get("deadline")
    user_id = data.get("user_id")

    if not title or not deadline or not user_id:
        return jsonify({"error": "Missing fields"}), 400

    task = Task(
        title=title,
        details=details,
        deadline=datetime.datetime.strptime(deadline, "%Y-%m-%d").date(),
        user_id=user_id,
        completed=False
    )
    session.add(task)
    session.commit()
    return jsonify({"message": "Task added", "task_id": task.id})

@app.patch("/tasks/<int:task_id>/toggle")
def toggle_task(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.completed = not task.completed
        session.commit()
        return jsonify({"message": "Task updated", "completed": task.completed})
    return jsonify({"error": "Task not found"}), 404

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
