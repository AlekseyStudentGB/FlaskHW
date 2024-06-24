from fastapi.responses import JSONResponse
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import Optional
from fastapi.openapi.utils import get_openapi
app = FastAPI(openapi_url="/api/v1/openapi.json")

"""
Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. 
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic."""

def custom_openapi():
    if app.openapi_schema:
      return app.openapi_schema
    openapi_schema = get_openapi(
        title="HomeWork",
        version="1.0.0",
        description="This is homework schema",
        routes=app.routes)
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi

tasks = []


class Task(BaseModel):
    task_id: int
    title: str
    description: str
    status: Optional[bool] = False


@app.get('/tasks', response_model=list[Task])
async def get_tasks():
    return tasks


@app.get('/tasks/{id}', response_model=list[Task])
async def get_task(task_id: int):
    task = [t for t in tasks if t.task_id == task_id]
    return task


@app.post('/tasks', response_model=list[Task])
async def add_task(title: str, description: str, status: bool=False):
    task = Task(task_id=len(tasks), title=title, description=description)
    if status:
        task.status = True
    tasks.append(task)
    return tasks


@app.put("/tasks/{id}", response_model=list[Task])
async def update_task(task_id: int):
    for t in tasks:
        if task_id == t.task_id:
            t.status = True
    return tasks


@app.delete("/tasks/{id}", response_model=list[Task])
async def delete_task(task_id: int):
    for i in range(len(tasks)):
        if task_id == tasks[i].task_id:
            tasks.pop(i)
    return tasks

if __name__ == '__main__':
    uvicorn.run('HW_5:app', host='localhost', port=8000, reload=True)

