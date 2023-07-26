from flask_cors import CORS
from forest_monitor.config import getCurrentConfig
from forest_monitor import create_app

app_config = getCurrentConfig()
app = create_app(app_config)
#CORS(app, resources={r'/d/*': {"origins": '*'}})
CORS(app)

if __name__ == "__main__":
    app.run(host=app_config.HOST, port=app_config.PORT, debug=app_config.DEBUG)