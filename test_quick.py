#!/usr/bin/env python3
"""
Quick test for core functionality.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add the dashboard package to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from dashboard.data_processor import DataProcessor
from dashboard.chart_engine import ChartEngine
from dashboard.data_models import ChartConfig, ChartData


def test_core_functionality():
    """Test core functionality quickly."""
    print("Testing Core Functionality...")
    
    # Test data processing
    processor = DataProcessor()
    
    # Create test data
    test_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [10, 25, 15, 30, 20]
    })
    
    # Validate data
    validation = processor.validate_data(test_data)
    assert validation.is_valid, f"Data validation failed: {validation.errors}"
    print("✓ Data validation working")
    
    # Transform data
    chart_data = processor.transform_for_chart(test_data, "bar")
    assert len(chart_data.x_values) == 5, "Data transformation failed"
    print("✓ Data transformation working")
    
    # Test chart generation
    engine = ChartEngine(use_plotly=True)
    
    config = ChartConfig(
        title="Test Chart",
        x_label="Categories",
        y_label="Values"
    )
    
    # Create bar chart
    chart = engine.create_bar_chart(chart_data, config)
    assert chart.rendered_content is not None, "Chart rendering failed"
    assert len(chart.rendered_content) > 100, "Chart content too short"
    print("✓ Chart generation working")
    
    # Test chart update
    new_config = ChartConfig(
        title="Updated Chart",
        x_label="Categories",
        y_label="Values",
        color_scheme="viridis"
    )
    
    updated_chart = engine.update_chart_config(chart, new_config)
    assert updated_chart.config.title == "Updated Chart", "Chart update failed"
    print("✓ Chart updates working")
    
    print("\n✅ All core functionality tests passed!")
    print(f"Chart content length: {len(chart.rendered_content)} characters")
    print(f"Chart type: {chart.chart_type.value}")
    print(f"Data points: {len(chart.data.x_values)}")


if __name__ == "__main__":
    test_core_functionality()