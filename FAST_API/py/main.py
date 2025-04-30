from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

# Устанавливаем русский язык для Wikipedia
wikipedia.set_lang("ru")

# Модель для POST запроса
class ArticleRequest(BaseModel):
    title: str

# 1. роут с параметром path
@app.get("/article/{title}")
def get_article(title: str):
    """Получить статью по названию"""
    return {"article": wikipedia.summary(title)}

# 2. роут с параметром query
@app.get("/search")
def search_article(query: str, sentences: int = 3):
    """Поиск статьи с указанием количества предложений"""
    return {"result": wikipedia.summary(query, sentences=sentences)}

# 3. роут с передачей параметров в теле запроса
@app.post("/article")
def create_article_request(request: ArticleRequest):
    """Получить статью по названию из тела запроса"""
    return {"requested_article": wikipedia.summary(request.title)}