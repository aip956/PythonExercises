from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .models import Base, Task
from .database import engine, get_db
from .rabbitmq import send_notification

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str = None

@app.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    send_notification(f'Task created: {db_task.title}')
    return db_task

