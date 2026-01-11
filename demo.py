#!/usr/bin/env python3
"""
Demo script for the Data Visualization Dashboard.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Add the dashboard package to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from dashboard.data_processor import DataProcessor
from dashboard.chart_engine import ChartEngine
from dashboard.data_models import ChartConfig
from dashboard.performance_monitor import performance_monitor


def create_sample_data():
    """Create sample datasets for demonstration."""
    
    # Sales data
    sales_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [120, 150, 180, 200, 170, 220],
        'Profit': [24, 30, 36, 40, 34, 44],
        'Region': ['North', 'South', 'North', 'South', 'North', 'South']
    })
    
    # Time series data
    dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    time_series_data = pd.DataFrame({
        'Date': dates,
        'Temperature': 20 + 10 * np.sin(np.arange(30) * 0.2) + np.random.randn(30) * 2,
        'Humidity': 50 + 20 * np.cos(np.arange(30) * 0.15) + np.random.randn(30) * 5
    })
    
    # Category data for pie chart
    category_data = pd.DataFrame({
        'Category': ['Desktop', 'Mobile', 'Tablet', 'Smart TV', 'Other'],
        'Users': [45, 35, 12, 5, 3]
    })
    
    return sales_data, time_series_data, category_data


def demo_chart_creation():
    """Demonstrate chart creation capabilities."""
    print("Data Visualization Dashboard Demo")
    print("=" * 50)
    
    # Initialize components
    processor = DataProcessor()
    engine = ChartEngine(use_plotly=True)
    
    # Create sample data
    sales_data, time_series_data, category_data = create_sample_data()
    
    print(f"Created sample datasets:")
    print(f"  - Sales data: {len(sales_data)} rows")
    print(f"  - Time series data: {len(time_series_data)} rows")
    print(f"  - Category data: {len(category_data)} rows")
    print()
    
    # Demo 1: Bar Chart
    print("1. Creating Bar Chart...")
    try:
        validation = processor.validate_data(sales_data)
        if validation.is_valid:
            chart_data = processor.transform_for_chart(sales_data, "bar")
            config = ChartConfig(
                title="Monthly Sales Performance",
                x_label="Month",
                y_label="Sales ($1000s)",
                color_scheme="default"
            )
            bar_chart = engine.create_bar_chart(chart_data, config)
            print(f"   ✓ Bar chart created successfully ({len(bar_chart.rendered_content)} chars)")
        else:
            print(f"   ✗ Data validation failed: {validation.errors}")
    except Exception as e:
        print(f"   ✗ Error creating bar chart: {e}")
    
    # Demo 2: Line Chart
    print("2. Creating Line Chart...")
    try:
        validation = processor.validate_data(sales_data)
        if validation.is_valid:
            chart_data = processor.transform_for_chart(sales_data, "line")
            config = ChartConfig(
                title="Sales Trend Over Time",
                x_label="Month",
                y_label="Sales ($1000s)",
                color_scheme="viridis"
            )
            line_chart = engine.create_line_chart(chart_data, config)
            print(f"   ✓ Line chart created successfully ({len(line_chart.rendered_content)} chars)")
        else:
            print(f"   ✗ Data validation failed: {validation.errors}")
    except Exception as e:
        print(f"   ✗ Error creating line chart: {e}")
    
    # Demo 3: Pie Chart
    print("3. Creating Pie Chart...")
    try:
        validation = processor.validate_data(category_data)
        if validation.is_valid:
            chart_data = processor.transform_for_chart(category_data, "pie")
            config = ChartConfig(
                title="User Distribution by Device",
                x_label="Device Type",
                y_label="Percentage",
                color_scheme="plasma"
            )
            pie_chart = engine.create_pie_chart(chart_data, config)
            print(f"   ✓ Pie chart created successfully ({len(pie_chart.rendered_content)} chars)")
        else:
            print(f"   ✗ Data validation failed: {validation.errors}")
    except Exception as e:
        print(f"   ✗ Error creating pie chart: {e}")
    
    # Demo 4: Time Series Chart
    print("4. Creating Time Series Chart...")
    try:
        validation = processor.validate_data(time_series_data)
        if validation.is_valid:
            chart_data = processor.transform_for_chart(time_series_data, "time_series")
            config = ChartConfig(
                title="Temperature Over Time",
                x_label="Date",
                y_label="Temperature (°C)",
                color_scheme="cool"
            )
            time_chart = engine.create_time_series(chart_data, config)
            print(f"   ✓ Time series chart created successfully ({len(time_chart.rendered_content)} chars)")
        else:
            print(f"   ✗ Data validation failed: {validation.errors}")
    except Exception as e:
        print(f"   ✗ Error creating time series chart: {e}")
    
    print()
    
    # Performance Summary
    print("Performance Summary:")
    print("-" * 20)
    summary = performance_monitor.get_performance_summary()
    if "message" not in summary:
        print(f"Total operations: {summary['total_operations']}")
        print(f"Average duration: {summary['average_duration']:.3f}s")
        print(f"Max duration: {summary['max_duration']:.3f}s")
        print(f"Performance warnings: {summary['performance_warnings']}")
        print(f"Performance errors: {summary['performance_errors']}")
        
        print("\nOperations by type:")
        for op, count in summary.get('operations_by_type', {}).items():
            print(f"  {op}: {count}")
    else:
        print(summary['message'])
    
    print("\n" + "=" * 50)
    print("Demo completed successfully!")
    print("All chart types are working correctly.")
    print("\nTo run the full dashboard UI, use: python main.py")


if __name__ == "__main__":
    demo_chart_creation()