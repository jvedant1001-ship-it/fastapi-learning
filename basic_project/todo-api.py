from fastapi import FastAPI

app = FastAPI()

todos = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "completed": False
    },
    {
        "id": 2,
        "title": "Practice Python",
        "completed": False
    }
]

#opening statement
@app.get("/")
def hello():
    return {"comment":"welcome to todo system"}

#get all todos
@app.get("/todos")
def all():
    return todos

#get one todo
@app.get("/todos/{todo_id}")
def single(todo_id:int):

    for todo in todos:
        return todo_id

    return "todo not found"

#creating a new todo
@app.post("/todos")
def create(todo:dict):
    new_todo={
        "id" : len(todos)+1,
        "tittle" : todo["tittle"] ,
        "completed" : todo["completed"]
    } 
    todos.append(new_todo)

    return new_todo

#updating todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,todo:dict):
    for item in todos:
        if item["id"] == todo_id:
            todo = {
                item["tittle"]:todo['tittle'],
                item['completed']:todo['completed']
            }
        return item
    return 'todo not found'

# delete todo

@app.delete("/todo/{todo_id}")
def del_todo(todo_id:int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return "'message':'todo removed'"
    return "todo not found"
