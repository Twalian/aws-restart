"""
implementare una corretta gestione degli errori su quanto fatto finora;
implementare una chiamata alla lista completa dei prodotti;
mostrare a video la lista completa dei prodotti (solo ID e titolo);
inserire un input per scegliere quale prodotto visualizzare;
stampare le informazioni del singolo prodotto;
dividere il progetto in pacchetti e moduli;
"""

from requests import get, post, Response
from requests.exceptions import  HTTPError, ConnectionError, Timeout, RequestException

BASE_URL : str = "https://api.escuelajs.co/api/v1/products"
URL_CATEGORIES : str = "https://api.escuelajs.co/api/v1/categories/"

def get_data(URL : str) -> Response:

    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    
    try:
        response = get(URL)
        response.raise_for_status()
        return response
    
    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}: {response.reason}"
        ) from e

    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")
    
    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}")
    
def get_lista_prodotti(URL: str) -> list[dict[str, any]]:
    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    try:
        response : Response = get_data(URL)
        return response.json()
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")
    
def get_lista_categorie(URL: str) -> list[dict[str, any]]:
    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    try:
        response : Response = get_data(URL)
        return response.json()
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")
    
def get_prodotto(URL: str) -> dict[str, any]:
    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    try:
        response : Response = get_data(URL)
        return response.json()
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")
    
def get_categoria(URL: str) -> dict[str, any]:
    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    try:
        response : Response = get_data(URL)
        return response.json()
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

def product_model(product : dict[str, any]) -> dict[str, any] :
    return {
        "id": product["id"], 
        "title": product["title"], 
        "price":product["price"],
        "category": product["category"]["name"], 
        "description": product["description"]
    }

def category_model(category : dict[str, any]) -> dict[str, any] :
    return {
        "id": category["id"], 
        "name": category["name"] 
    }

def product_model_all(products : list[dict[str, any]]) -> list[dict[str, any]] :
    products_list : list[dict[str, any]] = []
    for product in products:
        products_list.append({
        "id": product["id"], 
        "title": product["title"] 
    })
    return products_list

def categories_model_all(categories : list[dict[str, any]]) -> list[dict[str, any]] :
    categories_list : list[dict[str, any]] = []
    for category in categories:
        categories_list.append({
        "id": category["id"], 
        "name": category["name"]  
    })
    return categories_list

def print_prodotto(product : dict[str, any]) -> None :
    print("*"*30)
    print("PRODOTTO")
    print("*"*30)
    print(f"ID: {product["id"]}")
    print(f"Titolo: {product["title"]}")
    print(f"Category: {product["category"]["name"]}")
    print(f"Prezzo: {product["price"]}€")
    print(f"Descrizione: {product["description"]}")

def print_categoria(category : dict[str, any]) -> None :
    print("*"*30)
    print("CATEGORIA")
    print("*"*30)
    print(f"ID: {category["id"]}")
    print(f"Name: {category["name"]}")

def print_product_list(products : list[dict[str, any]]) -> None :
    print("*"*30)
    print("PRODOTTI")
    print("*"*30)
    for product in products:
        print(f"ID: {product["id"]} - Titolo: {product["title"]}")

def print_categories_list(categories : list[dict[str, any]]) -> None :
    print("*"*30)
    print("CATEGORIE")
    print("*"*30)
    for category in categories:
        print(f"ID: {category["id"]} - Name: {category["name"]}")

def post_data(URL: str, data: dict) -> Response:
    try:
        response = post(URL, headers={"Content-Type":"application/json"}, json=data)
        response.raise_for_status()
        return response.json()
    
    except HTTPError as e:
        raise HTTPError(f"Errore HTTP {response.status_code} su {URL}: {response.reason}"
        ) from e

    except ConnectionError:
        raise ConnectionError(f"Impossibile connettersi a {URL}")
    
    except Timeout:
        raise Timeout(f"Timeout nella richiesta a {URL}")
    
    except RequestException as e:
        raise RequestException(f"Errore di rete imprevisto: {e}")

def create_product(URL : str, data: dict) -> dict[str, any] :
    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    if data is None:
        raise ValueError("Data non può essere vuoto")
    if not isinstance(data, dict):
        raise TypeError(f"Risposta inattesa: mi aspettavo un dict, ma ho ricevuto un {type(data).__name__}")
    try:
        response = post_data(URL,data)
        return response
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

def create_category(URL : str, data: dict) -> dict[str, any] :
    if URL is None:
        raise ValueError("L'URL non può essere vuoto")
    if data is None:
        raise ValueError("Data non può essere vuoto")
    if not isinstance(data, dict):
        raise TypeError(f"Risposta inattesa: mi aspettavo un dict, ma ho ricevuto un {type(data).__name__}")
    try:
        response = post_data(URL,data)
        return response
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

product = {
  "title": "Prova prova prodotto prodotto",
  "price": 10,
  "description": "A description",
  "categoryId": 10,
  "images": ["https://placehold.co/600x400"]
}

category = {
  "name": "Giocattoli",
  "image": "https://placeimg.com/640/480/any"
}

def main() -> None :
    try:
        """
        products = product_model_all(get_lista_prodotti(BASE_URL))
        print_product_list(products)
        #id = input("Inserisci l'id del prodotto da visualizzare: ")
        #product = product_model(get_prodotto(f"{BASE_URL}/{id}"))
        #print_prodotto(product)
        print_prodotto(create_product(BASE_URL, product))
        """
        categories = categories_model_all(get_lista_categorie(URL_CATEGORIES))
        print_categories_list(categories)
        print_categoria(create_category(URL_CATEGORIES, category))
    except ValueError as e:
        print(f"{e}")
    
    except FileNotFoundError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__" :
    main()