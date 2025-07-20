#!/usr/bin/env python3
"""
TaskMaster - A beautiful and modern task management application
"""

import os
from api import app

if __name__ == "__main__":
    # Set default database URL if not provided
    if not os.getenv("DATABASE_URL"):
        os.environ["DATABASE_URL"] = "sqlite:///taskmaster.db"
    
    print("🚀 Starting TaskMaster...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("✨ Enjoy your beautiful task management experience!")
    
    app.run(debug=True, host='0.0.0.0', port=5000) 