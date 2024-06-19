from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
from pydantic import BaseModel
# from models import Base, Task
# from database import engine, get_db
from rabbitmq import send_notification
import logging

# Base.metadata.create_all(bind=engine)

app = FastAPI()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tasks = {}

class TaskCreate(BaseModel):
    title: str
    description: str = None

@app.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate):
    logger.info(f"Creating task: {task.title}")
    try:
        task_id = len(tasks) + 1
        tasks[task_id] = {"title": task.title, "description": task.description}
        send_notification(f'Task created: {task.title}')
        logger.info(f"Task created: {task.title}")
        return task
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Error creating task")
# def create_task(task: TaskCreate, db: Session = Depends(get_db)):
#     db_task = Task(title=task.title, description=task.description)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     send_notification(f'Task created: {db_task.title}')
#     return db_task
# This is an alchemy model instance, not pydantic, so might need to change it?

@app.get("/tasks/")
def read_tasks():
    return tasks

# def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     tasks = db.query(Task).offset(skip).limit(limit).all()
#     return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# def read_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = {"title": task.title, "description": task.description}
    send_notification(f'Task updated: {task.title}')
    return task
# def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
#     db_task = db.query(Task).filter(Task.id == task_id).first()
#     if db_task is None:
#         raise HTTPException(status_code=404, detail="Task not found")
#     db_task.title = task.title
#     db_task.description = task.description
#     db.commit()
#     db.refresh(db_task)
#     send_notification(f'Task udpated: {db_task.title}')
#     return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"ok": True}
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     db_task = db.query(Task).filter(Task.id == task_id).first()
#     if db_task is None:
#         raise HTTPException(status_code=404, detail="Task not found")
#     db.delete(db_task)
#     db.commit()
#     return {"ok": True}


