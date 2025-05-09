from app import app, db
from models import User
from flask_login import login_required
from routes import *  # Import all routes
import logging

# Set up basic application logging
logging.basicConfig(level=logging.DEBUG)

# Register the user_loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
        # Create admin user if it doesn't exist
        User.create_admin()
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)