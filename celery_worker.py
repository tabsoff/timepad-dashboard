from celery import Celery
from app import app

def make_celery(app):
    # Создаем экземпляр Celery, указывая имя приложения, брокер и бэкенд
    celery = Celery(
        app.import_name,
        broker='redis://localhost:6379/0',   # адрес Redis
        backend='redis://localhost:6379/0'
    )
    # Передаем конфигурацию Flask-приложения Celery
    celery.conf.update(app.config)
    return celery

# Инициализируем Celery, передавая наше Flask-приложение
celery = make_celery(app)

# Пример простой фоновой задачи
@celery.task
def test_task():
    return "Celery работает!"

if __name__ == "__main__":
    celery.start()