from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

app = FastAPI()

tasks: Dict[int, dict] = {}

class Task(BaseModel):
    title: str
    deadline: Optional[datetime] = None  
    status: Optional[str] = "Not started"

@app.post("/tasks")
def create_task(task: Task):
    task_id = len(tasks) + 1  
    tasks[task_id] = task.dict()
    return {"task_id": task_id, **tasks[task_id]}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task.dict()
    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}


@app.get("/tasks")
def check_tasks():
    remaining_tasks = {id: task for id, task in tasks.items() if task["status"] != "Completed"}
    return remaining_tasks



