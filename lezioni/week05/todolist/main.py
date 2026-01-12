import uuid
import datetime

projects : list[dict] = [{'id': 'a95fbfff-c187-4748-a376-d685746f1f86', 'name': 'pippo', 'description': 'boh', 'createdAt': '2026-01-08T09:05:13.056Z'}]

tasks: list[dict] = []

def check_task_title(title: str, projects: list[dict]) -> bool:
    """verifica che non esista una task con lo stesso title"""
    result : bool = False

    for t in tasks:
        if t['title'] == title:
            result = True
            break
    return result

def create_task(title: str, project_id: str, tags: list) -> dict:
    """crea un elemento task"""
     
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {'id' : str(uuid.uuid4()),
            'title' : title,
            'isCompleted' : False,
            'project_id' : project_id,
            'tags': tags,
            'createdAt' : clean_date,
            'completedAt' : None}

def save_task(title: str, project_id: str, tags: list) -> None:
    """salva la task nel db"""
    if check_task_title(title, tasks):
        raise ValueError(f"Attenzione: la task '{title}' esiste già!")
    task = create_task(title, project_id, tags)
    tasks.append(task)
    print(tasks)

def check_project_name(name: str, projects: list[dict]) -> bool:
    """verifica che non esista un progetto con lo stesso nome"""
    result : bool = False

    for p in projects:
        if p['name'] == name:
            result = True
            break
    return result

def create_project(name: str, description: str = "") -> dict:
    """crea un elemento progetto"""
     
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    return {'id' : str(uuid.uuid4()),
            'name' : name,
            'description' : description,
            'createdAt' : clean_date}

def save_project(name: str, description: str = "") -> None:
    """salva il progetto nel db"""
    if check_project_name(name, projects):
        raise ValueError(f"Attenzione: il progetto '{name}' esiste già!")
    project = create_project(name, description)
    projects.append(project)
    print(projects)
    
def main() -> None:
    print(save_task("titolo task", 'a95fbfff-c187-4748-a376-d685746f1f86', {"spesa"}))

if __name__ == "__main__":
    main()