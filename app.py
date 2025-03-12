# app.py - Flask application to serve the Market Analysis Dashboard

# 1. Import and configure Flask
from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Define the path to the data directory relative to app.py
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# 2. Serve the main dashboard page at the root route ("/")
@app.route("/")
def index():
    """
    Route for the root URL ("/").
    Renders the index.html template which is the main dashboard page.
    """
    return render_template('index.html')

# 3. API endpoint to serve market share data
@app.route("/api/marketShare")
def get_market_share():
    """
    API endpoint for fetching market share data.
    Reads marketShare.json from the /data directory and returns it as JSON.
    """
    try:
        with open(os.path.join(DATA_DIR, 'marketShare.json'), 'r') as f:
            market_share_data = json.load(f)
        return jsonify(market_share_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

# 3. API endpoint to serve revenue trends data
@app.route("/api/revenueTrends")
def get_revenue_trends():
    """
    API endpoint for fetching revenue trends data.
    Reads revenueTrends.json from the /data directory and returns it as JSON.
    """
    try:
        with open(os.path.join(DATA_DIR, 'revenueTrends.json'), 'r') as f:
            revenue_trends_data = json.load(f)
        return jsonify(revenue_trends_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

# 3. API endpoint to serve market segmentation data
@app.route("/api/marketSegmentation")
def get_market_segmentation():
    """
    API endpoint for fetching market segmentation data.
    Reads marketSegmentation.json from the /data directory and returns it as JSON.
    """
    try:
        with open(os.path.join(DATA_DIR, 'marketSegmentation.json'), 'r') as f:
            market_segmentation_data = json.load(f)
        return jsonify(market_segmentation_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

# 4. Serve static files (if needed - example for a 'static' folder)
# In this case, static files are not strictly needed as D3.js is loaded from CDN,
# but including this for potential future use of local static assets like CSS or images.
if __name__ == '__main__':
    app.run(debug=True) # Set debug=False in production

"""
Recommended Repository Structure for a GitHub Repository:

MarketAnalysisDashboard/  (Root directory of the repository)
├── app.py                # Flask application file
├── templates/            # Folder for HTML templates
│   └── index.html        # Main dashboard HTML file
├── data/                 # Folder for JSON data files
│   ├── marketShare.json
│   ├── revenueTrends.json
│   └── marketSegmentation.json
├── static/               # (Optional) Folder for static assets like CSS, images, etc.
│   └── (any static files, e.g., styles.css)
├── README.md             # (Optional but highly recommended) Project description and instructions
└── .gitignore            # (Optional but recommended) To ignore files like __pycache__, .env, etc.

Explanation:
- Root Directory (MarketAnalysisDashboard/): Contains all project files. It's the top-level folder in your GitHub repository.
- app.py: The main Python file for the Flask application.
- templates/: This folder is standard for Flask and should contain all HTML templates. 'index.html' is placed here.
- data/: This folder holds all the JSON data files required for the dashboard. Separating data makes the project organized.
- static/:  Although not used in this example for D3.js (CDN is used), it is good practice to have a 'static' folder for any static files like CSS stylesheets, JavaScript files (if you decide to host D3.js locally or add custom JS), images, etc. Flask automatically serves files from a folder named 'static' in the same directory as app.py, or within the application package.
- README.md: A good practice to include a README file in your repository root. It should describe what the project is, how to set it up, how to run it, and any other relevant information.
- .gitignore:  Useful for specifying intentionally untracked files that Git should ignore. Common for Python projects are virtual environment folders, __pycache__ directories, and potentially data files if they are large or frequently changed and not meant to be tracked in Git directly (though in this case, tracking data is appropriate).

This structure keeps the project organized by separating application logic (app.py), presentation (templates), and data (data), which is a clean and maintainable approach for web applications.
"""
