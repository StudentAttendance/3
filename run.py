import os
from webapp import create_app
from webapp.db import init_db


app = create_app()

# Initialize DB at startup (Flask 3 removed before_first_request)
with app.app_context():
    try:
        init_db()
    except Exception as e:
        print(f"Database initialization warning: {e}")

# For Railway/Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)


