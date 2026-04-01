from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)


REDIS_HOST = os.getenv("REDIS_HOST", "redis-0.redis-service")

@app.route('/')
def index():
    return "Benvenuto nel Cloud Health Monitoring! Accedi a /api/data per i risultati."

@app.route('/api/data')
def get_data():
    try:
        r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
        data = r.lrange("sensor_data", 0, -1)
        return jsonify({
            "status": "success",
            "device": "IoT-Sensor-Environmental-01",
            "results": data
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
