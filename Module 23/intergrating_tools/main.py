from fastapi import FastAPI
from model import Developers,Projects

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developers):
    return  {"message": "Developer created successfully", "developer":developer}


@app.post("/Projects/")
def create_project(project: Projects):
    return  {"message": "Project created successfully", "Project":project}


@app.get("/projects/")
def get_projects():
    sample_project = Projects(
        title = "Sample Project",
        description = "This is a sample project",
        language = ["HTML","CSS","JAVASCRIPT"],
        lead_developer = Developers(name="Jhon Doe",experience=5)

    )

    return{"projects":[sample_project]}