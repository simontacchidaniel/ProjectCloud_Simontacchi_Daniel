import redis
import time
import random
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis-0.redis-service")

def main():
    r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
    print(f"Connesso a Redis su {REDIS_HOST}")

    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        co2 = random.randint(400, 1000)
        
        data_string = f"Temp: {temp}C, CO2: {co2}ppm"
        r.lpush("sensor_data", data_string)
        r.ltrim("sensor_data", 0, 9) # Teniamo solo gli ultimi 10 messaggi
        
        print(f"Inviato: {data_string}")
        time.sleep(5)

if __name__ == "__main__":
    main()