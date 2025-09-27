# Green Team Hackathon - MLSysOps Application

An intelligent application orchestration system that leverages machine learning for dynamic workload management and system optimization in Kubernetes environments.

## Overview

This project implements a smart policy engine for MLSysOps that combines:
- **Intelligent Policy Management**: Dynamic decision-making for application placement and resource optimization
- **ML-Powered Predictions**: Time-series forecasting and system metrics prediction using Random Forest and Gradient Boosting models
- **Automated Container Orchestration**: Seamless deployment and management of detector and classifier applications
- **Real-time Telemetry Integration**: Continuous monitoring and adaptive response to system performance metrics

## Architecture

The system consists of several key components working together:

### Core Components

1. **Policy Engine** (`src/policy.py`)
   - Implements intelligent decision-making algorithms
   - Manages application placement and movement decisions
   - Integrates with ML models for predictive analytics
   - Handles telemetry data analysis and planning

2. **ML Prediction System** (`ml_example/predict.py`, `src/model_test.py`)
   - Time-series forecasting using trained ML models
   - Random Forest classifier for predictive maintenance
   - Feature engineering and data preprocessing
   - Model deployment and inference endpoints

3. **Application Components** (Deployed via `yaml/HackAppGroup3.yaml`)
   - **Detector App**: Real-time video processing and object detection
   - **Classifier App**: AI-powered image classification using ResNet18
   - Inter-component communication via TCP protocols

### System Flow

```
[Video Stream] → [Detector App] → [Classifier App] → [Policy Engine] → [ML Models] → [Orchestration Decisions]
                      ↓                ↓                    ↓              ↓
                [Telemetry] ← [Metrics Collection] ← [System Monitoring] ← [Adaptive Responses]
```

## Project Structure

```
green-team-hackathon/
├── src/                          # Core source code
│   ├── policy.py                 # Main policy engine with analyze() and plan() functions
│   ├── model_test.py             # ML model testing and validation
│   ├── requirements.txt          # Python dependencies for policy engine
│   ├── models-analysis.ipynb     # Data analysis and model evaluation
│   └── show_me_the_data_baby.ipynb  # Data exploration notebook
├── ml_example/                   # ML model deployment
│   ├── predict.py                # Time-series prediction engine
│   ├── kpi_pipeline.joblib       # Trained ML pipeline model
│   ├── model.json                # Model configuration and metadata
│   ├── deploy.json               # ML model deployment configuration
│   └── requirements-.txt         # ML-specific dependencies
├── yaml/                         # Kubernetes deployment configurations
│   └── HackAppGroup3.yaml        # Application deployment specification
└── utils/                        # Utility files and documentation
    └── Cli-commands.txt          # MLSysOps CLI usage examples
```

## Key Features

### 🤖 Intelligent Policy Management
- **Dynamic Component Placement**: Automatically decides optimal node placement for applications
- **Adaptive Resource Management**: Responds to system load and performance metrics
- **ML-Driven Decisions**: Uses trained models to predict optimal configurations

### 📊 Advanced Analytics
- **Time-Series Forecasting**: Predicts future system behavior and resource needs
- **Performance Monitoring**: Tracks frame classification latency and CPU utilization
- **Anomaly Detection**: Identifies unusual system behavior patterns

### 🚀 Automated Deployment
- **Container Orchestration**: Manages detector and classifier application lifecycle
- **Service Discovery**: Handles inter-service communication automatically
- **Scalable Architecture**: Supports multi-node cluster deployments

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Kubernetes cluster access
- MLSysOps CLI tools

### Environment Setup

1. **Create Virtual Environment**
   ```bash
   sudo apt install python3.10-venv
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   # Install MLSysOps CLI
   pip install mlsysops-cli
   
   # Install core dependencies
   pip install -r src/requirements.txt
   
   # Install ML dependencies (if using prediction features)
   pip install -r ml_example/requirements-.txt
   ```

3. **Configure Kubernetes Access**
   ```bash
   export KUBECONFIG=kubeconfig.yaml
   ```

## Usage

### Application Deployment

1. **Deploy the MLSysOps Application**
   ```bash
   mls apps deploy-app --path yaml/HackAppGroup3.yaml
   ```

2. **Set Policy on Agent**
   ```bash
   mls agent set-policy --agent cluster --file src/policy.py
   ```

3. **Monitor Application Status**
   ```bash
   mls apps list-all
   ```

### Policy Management

The policy engine (`src/policy.py`) provides three main functions:

- **`initialize()`**: Sets up initial context and configuration
- **`analyze()`**: Processes telemetry data and makes analytical assessments
- **`plan()`**: Creates deployment plans based on analysis results

### ML Model Usage

```python
# Load and use the trained model
from src.model_test import prepare_data_for_prediction
import joblib

# Load the model
model = joblib.load('ml_example/kpi_pipeline.joblib')

# Make predictions
predictions = prepare_data_for_prediction(model, "data_cleaned_to_test.pkl")
```

### Configuration

Key configuration parameters in the policy engine:

```python
{
    "telemetry": {
        "metrics": ["node_cpu_seconds_total", "frame_classify_latency"],
        "system_scrape_interval": "1s"
    },
    "mechanisms": ["fluidity"],
    "configuration": {
        "analyze_interval": "10s"
    },
    "scope": "application"
}
```

## Application Components

### Detector Application
- **Purpose**: Real-time video stream processing and object detection
- **Technology**: YOLO-based detection algorithm
- **Input**: RTSP video stream from camera-app
- **Output**: Detected objects forwarded to classifier

### Classifier Application  
- **Purpose**: AI-powered image classification
- **Technology**: ResNet18 model via TIMM framework
- **Features**: Real-time classification with telemetry integration
- **Scaling**: Supports horizontal scaling across cluster nodes

## Monitoring & Telemetry

The system continuously monitors:
- **CPU Utilization**: Per-node CPU usage tracking
- **Memory Usage**: Available memory monitoring
- **Application Latency**: Frame classification performance metrics
- **Network Performance**: Inter-service communication latency

## Management Commands

### Application Management
```bash
# List all deployed applications
mls apps list-all

# Remove application
mls apps remove-app <AppId>
```

### Policy Management
```bash
# Set policy
mls agent set-policy --agent cluster --file src/policy.py

# Remove policy
mls agent delete-policy --agent cluster policy.py
```

## Development

### Model Training & Analysis
- `src/models-analysis.ipynb`: Comprehensive model evaluation and performance analysis
- `src/show_me_the_data_baby.ipynb`: Data exploration and visualization
- `src/model_test.py`: Model validation and testing framework

### Key Dependencies
- **scikit-learn**: Machine learning algorithms and pipelines
- **pandas/numpy**: Data processing and numerical computations
- **mlsysops-cli**: MLSysOps platform integration
- **requests**: HTTP client for API communications
- **matplotlib/seaborn**: Data visualization

## Contributing

This project was developed as part of a hackathon focused on intelligent system orchestration and ML-driven application management.

## License

This project is part of the Green Team Hackathon submission.