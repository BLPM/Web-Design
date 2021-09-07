import os
from app import create_app

app = create_app()
# app = create_app('development')
port = int(os.environ.get('PORT', 8001))

if __name__ == '__main__':
    app.run(debug=True,threaded=True, host='127.0.0.1', port=port)
