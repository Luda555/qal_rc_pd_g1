import logging
import time
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

def chronicle(name = "Анонімний"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(f"[Літописець: {name}] Викликано: {func.__name__}{args}")
            result = func(*args, **kwargs)
            logging.info(f"[Результат]: {result}")
            return result
        return wrapper
    return decorator    
@chronicle("Самійло Величко")
def make_decision(action, target):
    return f"Рішення: {action} → {target}"

@chronicle()
def count_warriors(regiment):
    return 500

make_decision("Атакувати", "Перекоп")
count_warriors("Полтавський")  

def guard(secret):
    def decoret (func):
        def wrapper(*args, **kwargs):
            password = input("Введіть пароль")
            if password == secret:
                logging.info(f"Пароль вірний: {func.__name__}")
                result = func(*args, **kwargs)
                return result
            else:
                logging.warning(f"Стій! Доступ заборонено: {func.__name__}")
                print("Стій! Доступ заборонено.")
                return None
        return wrapper
    return decoret   

@guard(secret="Мамай")
def open_treasury():
    print("Скарбниця відчинена!")
    return "золото, срібло, зброя"

result = open_treasury() 

def retry(times=3, delay=1.0):
    def decoret (func):
        def wrapper(*args, **kwargs):
            for i in range(1, times +1):
                try:
                    result = func(*args, **kwargs)
                    logging.info(f"Успіх на спробі: {i}/ {times}")
                    return result
                except Exception as e:
                     logging.warning(f"Спроба {i}/ {times} не вдалася: {e}")
                     if i == times:
                        logging.error("Всі спроби вичерпано!")
                        raise e
                     time.sleep(delay)
        return wrapper
    return decoret        




