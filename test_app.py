#!/usr/bin/env python3
"""
Test script for TaskMaster application
"""

import os
import sys

def test_imports():
    """Test if all required modules can be imported"""
    try:
        from models import User, Task, session
        print("✅ Models imported successfully")
        
        from api import app
        print("✅ Flask app imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_database():
    """Test database connection and table creation"""
    try:
        from models import session, User, Task
        
        # Test creating a user
        test_user = User(username="test_user", password="test_password")
        session.add(test_user)
        session.commit()
        
        # Test creating a task
        test_task = Task(
            title="Test Task",
            details="This is a test task",
            user_id=test_user.id,
            completed=False
        )
        session.add(test_task)
        session.commit()
        
        # Clean up test data
        session.delete(test_task)
        session.delete(test_user)
        session.commit()
        
        print("✅ Database operations successful")
        return True
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing TaskMaster Application...")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("❌ Import tests failed")
        sys.exit(1)
    
    # Test database
    if not test_database():
        print("❌ Database tests failed")
        sys.exit(1)
    
    print("=" * 40)
    print("✅ All tests passed! Application is ready to run.")
    print("🚀 Run 'python run.py' to start the application.")

if __name__ == "__main__":
    main() 