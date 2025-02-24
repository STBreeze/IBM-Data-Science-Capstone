# SpaceX Falcon 9 First Stage Landing Prediction

## Project Overview
This project is the final capstone for the IBM Data Science Professional Certificate. The goal is to predict whether the Falcon 9 first stage will land successfully, which is crucial for reducing launch costs and enabling reusability. The project involves data collection, analysis, machine learning, and interactive visualizations.

## Features
### Data Collection & Wrangling
- Extracted SpaceX launch data using the SpaceX API.
- Scraped Falcon 9 launch records from Wikipedia using BeautifulSoup.
- Cleaned and formatted the data for further analysis.

### Exploratory Data Analysis (EDA)
- Analyzed launch trends, payload mass impact, and mission outcomes.
- Visualized launch success rates using Matplotlib and Seaborn.

#### Flight Number vs Orbit
![Flight Number vs Orbit](https://github.com/STBreeze/IBM-Data-Science-Capstone/blob/30ffaf00f705b7cb9367bef5cf6d9ef5df6f957e/C10%20Capstone/Flight%20Number%20vs%20Orbit.png)

#### Payload vs Success Outcome
![Payload vs Success Outcome](https://github.com/STBreeze/IBM-Data-Science-Capstone/blob/30ffaf00f705b7cb9367bef5cf6d9ef5df6f957e/C10%20Capstone/dash_payload%20vs%20succes%20outcome.png)

### SQL-Based Data Analysis
- Loaded data into an SQLite database.
- Executed SQL queries to extract insights about payload distribution and mission success trends.

### Geospatial Analysis with Folium
- Mapped launch sites and visualized launch successes/failures.
- Measured distances between launch sites and coastlines, highways, and cities.

#### Launch Sites & Outcomes
![Launch Sites](https://github.com/STBreeze/IBM-Data-Science-Capstone/blob/30ffaf00f705b7cb9367bef5cf6d9ef5df6f957e/C10%20Capstone/folium_launch%20sites.png)
![Launch Site Outcome](https://github.com/STBreeze/IBM-Data-Science-Capstone/blob/30ffaf00f705b7cb9367bef5cf6d9ef5df6f957e/C10%20Capstone/folium_colour%20launch%20outcomes.png)

### Machine Learning Prediction
- Created binary classification labels (`1 = success`, `0 = failure`).
- Trained multiple models: Logistic Regression, SVM, Decision Tree, and KNN.
- Evaluated models and selected KNN as the best based on accuracy and simplicity.

#### Accuracy of Different Classification Models
![Accuracy of Different Models](https://github.com/STBreeze/IBM-Data-Science-Capstone/blob/30ffaf00f705b7cb9367bef5cf6d9ef5df6f957e/C10%20Capstone/Accuracy%20of%20different%20classification%20models.png)

#### KNN Confusion Matrix
![KNN Confusion Matrix](https://github.com/STBreeze/IBM-Data-Science-Capstone/blob/30ffaf00f705b7cb9367bef5cf6d9ef5df6f957e/C10%20Capstone/KNN%20Confusion%20Matrix.png)

### Interactive Dashboard with Dash & Plotly
- Built a web-based dashboard to visualize:
  - Launch success rates per site.
  - Payload mass vs. success rate.
  - Scatter plots & pie charts for mission outcomes.

## Dataset
The project utilizes multiple datasets:
- **`spacex_launch_dash.csv`**: Main dataset containing SpaceX launch records.
- **`spacex_web_scraped.csv`**: Data collected from SpaceX's website.
- **`spacex_launch_geo.csv`**: Geolocation data of launch sites.
- **`dataset_part1.csv`, `dataset_part2.csv`, `dataset_part3.csv`**: Processed datasets used in machine learning models.

## How to Run the Project

### Prerequisites
Install required dependencies:
```bash
pip install pandas numpy matplotlib seaborn plotly dash folium scikit-learn sqlite3 beautifulsoup4 requests
```

### Running the SQL Analysis
```bash
python spacex_sql_analysis.py
```

### Running the Machine Learning Model
```bash
python spacex_ml_pipeline.py
```

### Running the Interactive Dashboard
```bash
python spacex_dash_app.py
```
Then, open **http://127.0.0.1:8050/** in your browser.

## Key Findings
- Falcon 9 **success rates have increased over time**.
- **Specific orbits and payload ranges** impact launch success.
- **Geographic location matters**: proximity to coastlines and infrastructure influences landing success.
- **Machine Learning models predict success with 83% accuracy using KNN**.

## Conclusion
This project integrates **data science, machine learning, and interactive visualization** to analyze and predict Falcon 9 landings. The insights gained are valuable for SpaceX competitors and space industry analysts.

---
🚀 Developed as part of the IBM Data Science Capstone Project.

