#!/usr/bin/env python3
"""
Basic test to verify the project setup is working correctly.
"""

import sys
from pathlib import Path

# Add the dashboard package to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from dashboard.environment_manager import EnvironmentManager
from dashboard.data_models import ChartData, ChartConfig, ValidationResult, ChartType


def test_environment_manager():
    """Test basic EnvironmentManager functionality."""
    print("Testing EnvironmentManager...")
    
    env_manager = EnvironmentManager()
    
    # Test that the manager initializes correctly
    assert env_manager.project_root.exists(), "Project root should exist"
    assert env_manager.requirements_file.exists(), "Requirements file should exist"
    
    print("✓ EnvironmentManager initialization successful")


def test_data_models():
    """Test basic data model functionality."""
    print("Testing data models...")
    
    # Test ChartData
    chart_data = ChartData(
        x_values=[1, 2, 3, 4],
        y_values=[10, 20, 15, 25]
    )
    assert len(chart_data.x_values) == len(chart_data.y_values), "Data lengths should match"
    
    # Test ChartConfig
    config = ChartConfig(
        title="Test Chart",
        x_label="X Axis",
        y_label="Y Axis"
    )
    assert config.title == "Test Chart", "Title should be set correctly"
    assert config.width > 0 and config.height > 0, "Dimensions should be positive"
    
    # Test ValidationResult
    validation = ValidationResult(is_valid=True)
    validation.add_warning("Test warning")
    assert len(validation.warnings) == 1, "Warning should be added"
    
    validation.add_error("Test error", "Test fix")
    assert not validation.is_valid, "Should be invalid after adding error"
    assert len(validation.errors) == 1, "Error should be added"
    assert len(validation.suggested_fixes) == 1, "Fix should be added"
    
    print("✓ Data models working correctly")


def test_chart_types():
    """Test chart type enumeration."""
    print("Testing chart types...")
    
    assert ChartType.BAR.value == "bar", "Bar chart type should be correct"
    assert ChartType.LINE.value == "line", "Line chart type should be correct"
    assert ChartType.PIE.value == "pie", "Pie chart type should be correct"
    assert ChartType.TIME_SERIES.value == "time_series", "Time series type should be correct"
    
    print("✓ Chart types working correctly")


def main():
    """Run all basic tests."""
    print("Running basic setup tests...")
    print("=" * 40)
    
    try:
        test_environment_manager()
        test_data_models()
        test_chart_types()
        
        print("=" * 40)
        print("✅ All basic tests passed!")
        print("Project setup is working correctly.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()