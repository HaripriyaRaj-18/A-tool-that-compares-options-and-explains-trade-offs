# Data Visualization Dashboard

A Python-based application for creating interactive charts and visualizations with clean dependency management and fast rendering performance.

## Features

- **Multiple Chart Types**: Bar charts, line graphs, pie charts, and time-series visualizations
- **Interactive Visualizations**: Built with Plotly for web-ready, interactive charts
- **Clean Data Processing**: Support for CSV and JSON input formats with validation
- **Virtual Environment Management**: Automatic dependency isolation and management
- **Performance Optimized**: Fast rendering for datasets up to 10,000 points

## Quick Start

1. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd data-visualization-dashboard
   python main.py
   ```

2. **Manual Setup** (if needed):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Project Structure

```
data-visualization-dashboard/
├── dashboard/
│   ├── __init__.py
│   ├── environment_manager.py    # Virtual environment management
│   └── data_models.py           # Data structures and models
├── main.py                      # Application entry point
├── requirements.txt             # Project dependencies
├── setup.py                     # Package configuration
└── README.md                    # This file
```

## Dependencies

- **plotly**: Interactive visualization library
- **pandas**: Data manipulation and analysis
- **matplotlib**: Fallback plotting library
- **numpy**: Numerical computing support
- **pytest**: Testing framework
- **hypothesis**: Property-based testing

## Development

This project follows a modular architecture with separate components for:
- Environment management and dependency isolation
- Data processing and validation
- Chart generation and rendering
- Dashboard user interface

## Testing

The project uses both unit tests and property-based tests for comprehensive validation:
- Unit tests for specific functionality and edge cases
- Property-based tests for universal correctness properties

## License

This project is licensed under the MIT License.