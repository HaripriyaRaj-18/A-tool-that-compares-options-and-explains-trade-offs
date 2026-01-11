#!/usr/bin/env python3
"""
Main entry point for the Data Visualization Dashboard.
"""

import sys
from pathlib import Path

# Add the dashboard package to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from dashboard.environment_manager import EnvironmentManager
from dashboard.dashboard_ui import Dashboard


def main():
    """Main application entry point."""
    print("Data Visualization Dashboard")
    print("=" * 40)
    
    # Initialize environment manager
    env_manager = EnvironmentManager()
    
    # Set up project environment
    print("Setting up environment...")
    if not env_manager.setup_project():
        print("Failed to set up project environment")
        sys.exit(1)
    
    # Verify dependencies
    missing_packages = env_manager.verify_dependencies()
    if missing_packages:
        print(f"Warning: Missing packages detected: {missing_packages}")
        print("Some features may not work properly.")
        print("Run 'pip install -r requirements.txt' to install missing dependencies")
    
    print("Environment setup complete!")
    print("Starting dashboard...")
    
    try:
        # Create and run dashboard
        dashboard = Dashboard()
        dashboard.run()
        
    except KeyboardInterrupt:
        print("\nShutting down dashboard...")
    except Exception as e:
        print(f"Error running dashboard: {e}")
        sys.exit(1)
    
    print("Dashboard closed successfully!")


if __name__ == "__main__":
    main()