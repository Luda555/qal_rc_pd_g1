def make_voltage_converter(factor: float):
    def converter (voltage):
        return factor * voltage
    return converter

step_up   = make_voltage_converter(10.0)   
step_down = make_voltage_converter(0.5)    

print(step_up(22.0))     
print(step_down(220.0))  
print(step_up(11.0))
    
def make_electricity_meter(address: str, initial_kwh: float = 0.0):
    start_kwh = initial_kwh
    current_kwh = initial_kwh
    def add(kwh: float):
        nonlocal current_kwh 
        current_kwh += kwh    
        return current_kwh
    def reset():
        nonlocal current_kwh  
        current_kwh = start_kwh  
        return current_kwh
    def report() -> str: 
        return f"Адреса: {address} | Спожито: {current_kwh} кВт·год" 
    return add, reset, report           

add, reset, report = make_electricity_meter("вул. Франка, 12", 150.0)

print(add(30.5))    # 180.5
print(add(14.0))    # 194.5
print(report())     # Адреса: вул. Франка, 12 | Спожито: 194.5 кВт·год
print(reset())      # 150.0
print(report())


def make_dispatcher(station_name: str):
    def dispatch(event: str, callback):
        message = f"[{station_name}] {event}"
        callback(message)
    return dispatch

def log_to_console(message: str):
    """Виводить повідомлення в консоль."""
    print(message)


def log_to_file(message: str):
    """Дописує повідомлення у файл dispatch_log.txt."""
    with open("dispatch_log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")


dispatch = make_dispatcher("Підстанція №7 Івано-Франківськ")

dispatch("Перевищення напруги", log_to_console)

# [Підстанція №7 Івано-Франківськ] Перевищення напруги

dispatch("Коротке замикання", log_to_console)
# [Підстанція №7 Івано-Франківськ] Коротке замикання

dispatch("Відновлення живлення", log_to_file)
# (повідомлення записується у dispatch_log.txt)        


substations = [
    {"name": "Підстанція №3", "region": "Коломия",        "load_kw": 4500},
    {"name": "Підстанція №7", "region": "Івано-Франківськ", "load_kw": 8200},
    {"name": "Підстанція №1", "region": "Калуш",           "load_kw": 3100},
    {"name": "Підстанція №9", "region": "Надвірна",        "load_kw": 6700},
]
def make_sorter(field: str, reverse: bool = False):
    def sort_stations(stations: list) -> list:
         return sorted(stations, key=lambda station: station[field], reverse=reverse)
    return sort_stations

sort_by_load = make_sorter("load_kw", reverse=True)
for s in sort_by_load(substations):
    print(s["name"], s["load_kw"])

    # home work 19, part 2


from datetime import datetime
TIME_FORMAT = '%H:%M:%S' #формат часу

def analyze_heartbeats(log_file_path: str, report_file_path: str):
    last_seen = {}

    with open(log_file_path, 'r', encoding='utf-8') as infile, \
        open(report_file_path, 'w', encoding='utf-8') as report:
        
        report.write("Звіт \n") 

        for line in infile:
            if "Key" not in line:
                continue
                
            words = line.split()
            
            try:
                
                key_index = words.index("Key")
                raw_key = words[key_index + 1]
                key = raw_key.split('|')[0]
            except (ValueError, IndexError):
                continue
            
            timestamp_str = ""
            for word in words:
                if word.count(":") == 2:
                    timestamp_str = word
                    break
                    
            if not timestamp_str:
                continue
            
            try:
                current_time = datetime.strptime(timestamp_str, TIME_FORMAT)
            except ValueError:
                continue
            
            if key in last_seen:
                delta = (current_time - last_seen[key]).total_seconds()
                
                if delta < 0:
                    delta += 86400
                
                if 31 < delta <= 33:
                    report.write(f"[WARNING] Process: {key} | Heartbeat delay: {delta}s | Time: {timestamp_str}\n")
               
                elif delta > 33:
                    report.write(f"[ERROR]   Process: {key} | Heartbeat delay: {delta}s | Time: {timestamp_str}\n")
            
            
            last_seen[key] = current_time


analyze_heartbeats("hblog", "lesson_19_closur_datetime/hb_test.log.txt")




