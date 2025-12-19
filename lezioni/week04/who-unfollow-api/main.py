import uuid, datetime, os, json
from requests import get

URL = "https://api.github.com/users/emanuelegurini/followers"

DATA = [
  {
    "login": "lmammino",
    "id": 205629,
    "node_id": "MDQ6VXNlcjIwNTYyOQ==",
    "avatar_url": "https://avatars.githubusercontent.com/u/205629?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/lmammino",
    "html_url": "https://github.com/lmammino",
    "followers_url": "https://api.github.com/users/lmammino/followers",
    "following_url": "https://api.github.com/users/lmammino/following{/other_user}",
    "gists_url": "https://api.github.com/users/lmammino/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/lmammino/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/lmammino/subscriptions",
    "organizations_url": "https://api.github.com/users/lmammino/orgs",
    "repos_url": "https://api.github.com/users/lmammino/repos",
    "events_url": "https://api.github.com/users/lmammino/events{/privacy}",
    "received_events_url": "https://api.github.com/users/lmammino/received_events",
    "type": "User",
    "user_view_type": "public",
    "site_admin": False
  },
  {
    "login": "luduvigo",
    "id": 1569913,
    "node_id": "MDQ6VXNlcjE1Njk5MTM=",
    "avatar_url": "https://avatars.githubusercontent.com/u/1569913?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/luduvigo",
    "html_url": "https://github.com/luduvigo",
    "followers_url": "https://api.github.com/users/luduvigo/followers",
    "following_url": "https://api.github.com/users/luduvigo/following{/other_user}",
    "gists_url": "https://api.github.com/users/luduvigo/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/luduvigo/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/luduvigo/subscriptions",
    "organizations_url": "https://api.github.com/users/luduvigo/orgs",
    "repos_url": "https://api.github.com/users/luduvigo/repos",
    "events_url": "https://api.github.com/users/luduvigo/events{/privacy}",
    "received_events_url": "https://api.github.com/users/luduvigo/received_events",
    "type": "User",
    "user_view_type": "public",
    "site_admin": False
  },
  {
    "login": "pfuhrmann",
    "id": 1627445,
    "node_id": "MDQ6VXNlcjE2Mjc0NDU=",
    "avatar_url": "https://avatars.githubusercontent.com/u/1627445?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/pfuhrmann",
    "html_url": "https://github.com/pfuhrmann",
    "followers_url": "https://api.github.com/users/pfuhrmann/followers",
    "following_url": "https://api.github.com/users/pfuhrmann/following{/other_user}",
    "gists_url": "https://api.github.com/users/pfuhrmann/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/pfuhrmann/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/pfuhrmann/subscriptions",
    "organizations_url": "https://api.github.com/users/pfuhrmann/orgs",
    "repos_url": "https://api.github.com/users/pfuhrmann/repos",
    "events_url": "https://api.github.com/users/pfuhrmann/events{/privacy}",
    "received_events_url": "https://api.github.com/users/pfuhrmann/received_events",
    "type": "User",
    "user_view_type": "public",
    "site_admin": False
  }]

def get_users(url: str) -> list[dict]:
    page = 1
    while True:
        response = get(f"{url}?page={page}")
        print(page)
        if not "next" in response.headers["Link"]:
            break
        page += 1


def extract_usernames(users: list[dict]) -> list[str]:
    usernames: list[str] = []
    for user in users:
        usernames.append(user["login"])
    return usernames

def create_record(usernames: list[str]) -> dict:

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    clean_date = now_utc.isoformat(timespec='milliseconds').replace('+00.00', 'Z')
    return {
        "id": str(uuid.uuid4()),
        "creationAt" : clean_date,
        "user" : usernames,
        "numberOfUsers" : len(usernames)
    }

def create_json_db(db_name: str) -> bool:
    """Crea un nuovo file db con lista vuota."""
    # Crea la cartella se non esiste
    os.makedirs(os.path.dirname(db_name), exist_ok=True)
    
    with open(db_name, "w") as f:
        f.write("[]")

    return True

def check_if_json_db_has_correct_shape(db_name: str) -> bool:
    """Verifica che il db esiste ed è nella forma corretta."""
    if not os.path.isfile(db_name):
        return False

    with open(db_name, "r") as f:
        data = json.load(f)
        return isinstance(data, list)

def save_json_db(db_name: str, new_record: dict) -> None:
    """Salva il nuovo oggetto nel db."""
    if not check_if_json_db_has_correct_shape(db_name):
        create_json_db(db_name)

    db_tmp: list[dict] = []

    with open(db_name, "r") as f:
        db_tmp.extend(json.load(f))

    db_tmp.append(new_record)

    with open(db_name, "w", encoding='utf-8') as f:
        json.dump(db_tmp, f, indent=4, ensure_ascii=False)

def main() -> None:
    print("Inizio programma")
    """
    lista_utenti = extract_usernames(DATA)
    record = create_record(lista_utenti)
    save_json_db("db/db.json", record)
    """
    get_users(URL)

if __name__ == "__main__":
    main()