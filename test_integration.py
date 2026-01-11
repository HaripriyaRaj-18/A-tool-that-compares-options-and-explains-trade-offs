#!/usr/bin/env python3
"""
Integration test for the complete Data Visualization Dashboard.
"""

import sys
import tempfile
import json
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Add the dashboard package to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from dashboard.environment_manager import EnvironmentManager
from dashboard.data_processor import DataProcessor
from dashboard.chart_engine import ChartEngine
from dashboard.data_models import ChartConfig, ChartType
from dashboard.performance_monitor import performance_monitor, DataOptimizer


def test_environment_setup():
    """Test environment management."""
    print("Testing Environment Management...")
    
    env_manager = EnvironmentManager()
    
    # Test environment creation
    assert env_manager.create_environment("test_env"), "Failed to create test environment"
    
    # Test dependency verification
    missing = env_manager.verify_dependencies()
    print(f"Missing dependencies: {missing}")
    
    print("✓ Environment management working")


def test_data_processing():
    """Test data processing functionality."""
    print("Testing Data Processing...")
    
    processor = DataProcessor()
    
    # Create test CSV data
    test_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [10, 25, 15, 30, 20],
        'Date': pd.date_range('2024-01-01', periods=5),
        'Random': np.random.randn(5)
    })
    
    # Test CSV parsing (save and load)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        test_data.to_csv(f.name, index=False)
        loaded_data = processor.parse_csv(f.name)
        assert len(loaded_data) == 5, "CSV parsing failed"
    
    # Test JSON parsing
    json_data = test_data.to_json(orient='records')
    loaded_json = processor.parse_json(json_data)
    assert len(loaded_json) == 5, "JSON parsing failed"
    
    # Test data validation
    validation = processor.validate_data(test_data)
    assert validation.is_valid, f"Data validation failed: {validation.errors}"
    
    # Test data transformation for different chart types
    bar_data = processor.transform_for_chart(test_data, "bar")
    assert len(bar_data.x_values) == 5, "Bar chart transformation failed"
    
    pie_data = processor.transform_for_chart(test_data, "pie")
    assert len(pie_data.x_values) == 5, "Pie chart transformation failed"
    
    print("✓ Data processing working")


def test_chart_generation():
    """Test chart generation functionality."""
    print("Testing Chart Generation...")
    
    engine = ChartEngine(use_plotly=True)
    
    # Create test data
    from dashboard.data_models import ChartData
    
    test_chart_data = ChartData(
        x_values=['A', 'B', 'C', 'D', 'E'],
        y_values=[10, 25, 15, 30, 20]
    )
    
    config = ChartConfig(
        title="Test Chart",
        x_label="Categories",
        y_label="Values"
    )
    
    # Test all chart types
    bar_chart = engine.create_bar_chart(test_chart_data, config)
    assert bar_chart.chart_type == ChartType.BAR, "Bar chart creation failed"
    assert bar_chart.rendered_content is not None, "Bar chart rendering failed"
    
    line_chart = engine.create_line_chart(test_chart_data, config)
    assert line_chart.chart_type == ChartType.LINE, "Line chart creation failed"
    assert line_chart.rendered_content is not None, "Line chart rendering failed"
    
    pie_chart = engine.create_pie_chart(test_chart_data, config)
    assert pie_chart.chart_type == ChartType.PIE, "Pie chart creation failed"
    assert pie_chart.rendered_content is not None, "Pie chart rendering failed"
    
    # Test time series with datetime data
    time_data = ChartData(
        x_values=[datetime.now() - timedelta(days=x) for x in range(5, 0, -1)],
        y_values=[10, 25, 15, 30, 20]
    )
    
    time_chart = engine.create_time_series(time_data, config)
    assert time_chart.chart_type == ChartType.TIME_SERIES, "Time series creation failed"
    assert time_chart.rendered_content is not None, "Time series rendering failed"
    
    print("✓ Chart generation working")


def test_performance_monitoring():
    """Test performance monitoring."""
    print("Testing Performance Monitoring...")
    
    # Performance monitor should have recorded metrics from chart generation
    summary = performance_monitor.get_performance_summary()
    
    if "message" not in summary:  # Has actual data
        assert summary["total_operations"] > 0, "No performance metrics recorded"
        print(f"Recorded {summary['total_operations']} operations")
        print(f"Average duration: {summary['average_duration']:.3f}s")
    
    print("✓ Performance monitoring working")


def test_data_optimization():
    """Test data optimization functionality."""
    print("Testing Data Optimization...")
    
    # Create large test dataset
    large_data = pd.DataFrame({
        'x': range(15000),
        'y': np.random.randn(15000),
        'category': ['A', 'B', 'C'] * 5000
    })
    
    # Test sampling
    sampled = DataOptimizer.sample_large_dataset(large_data, max_points=1000)
    assert len(sampled) <= 1000, "Data sampling failed"
    
    # Test data type optimization
    optimized = DataOptimizer.optimize_data_types(large_data)
    assert optimized is not None, "Data type optimization failed"
    
    print("✓ Data optimization working")


def test_end_to_end_workflow():
    """Test complete end-to-end workflow."""
    print("Testing End-to-End Workflow...")
    
    # Create components
    processor = DataProcessor()
    engine = ChartEngine()
    
    # Create sample data
    sample_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [100, 150, 120, 200, 180],
        'Profit': [20, 30, 25, 40, 35]
    })
    
    # Process data
    validation = processor.validate_data(sample_data)
    assert validation.is_valid, "End-to-end validation failed"
    
    # Transform for visualization
    chart_data = processor.transform_for_chart(sample_data, "bar")
    
    # Create chart
    config = ChartConfig(
        title="Monthly Sales",
        x_label="Month",
        y_label="Sales ($)"
    )
    
    chart = engine.create_bar_chart(chart_data, config)
    
    # Verify chart
    assert chart.rendered_content is not None, "End-to-end chart creation failed"
    assert len(chart.data.x_values) == 5, "End-to-end data integrity failed"
    
    # Test chart updates
    new_config = ChartConfig(
        title="Updated Monthly Sales",
        x_label="Month",
        y_label="Sales ($)",
        color_scheme="viridis"
    )
    
    updated_chart = engine.update_chart_config(chart, new_config)
    assert updated_chart.config.title == "Updated Monthly Sales", "Chart update failed"
    
    print("✓ End-to-end workflow working")


def test_error_handling():
    """Test error handling."""
    print("Testing Error Handling...")
    
    processor = DataProcessor()
    engine = ChartEngine()
    
    # Test invalid file
    try:
        processor.parse_csv("nonexistent_file.csv")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected
    
    # Test invalid JSON
    try:
        processor.parse_json("invalid json data")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected
    
    # Test empty data
    empty_data = pd.DataFrame()
    validation = processor.validate_data(empty_data)
    assert not validation.is_valid, "Empty data should be invalid"
    
    print("✓ Error handling working")


def main():
    """Run all integration tests."""
    print("Running Integration Tests for Data Visualization Dashboard")
    print("=" * 60)
    
    try:
        test_environment_setup()
        test_data_processing()
        test_chart_generation()
        test_performance_monitoring()
        test_data_optimization()
        test_end_to_end_workflow()
        test_error_handling()
        
        print("=" * 60)
        print("✅ ALL INTEGRATION TESTS PASSED!")
        print("The Data Visualization Dashboard is working correctly.")
        
        # Show performance summary
        print("\nPerformance Summary:")
        summary = performance_monitor.get_performance_summary()
        if "message" not in summary:
            print(f"  Total operations: {summary['total_operations']}")
            print(f"  Average duration: {summary['average_duration']:.3f}s")
            print(f"  Max duration: {summary['max_duration']:.3f}s")
            print(f"  Performance warnings: {summary['performance_warnings']}")
        else:
            print(f"  {summary['message']}")
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()