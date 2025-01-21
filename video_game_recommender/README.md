# Video Game Recommendation System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Streamlit App](#running-the-streamlit-app)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
The Game Recommendation System is a personalized recommendation engine built using machine learning. It helps users discover new video games based on their preferences, genres, and gameplay patterns. The app runs on **Streamlit**, providing an interactive and user-friendly web interface.

## Features
- **Interactive Web App:** Built with Streamlit for seamless user interaction.
- **Game Recommendations:** Tailored suggestions using collaborative and content-based filtering.
- **Search & Filters:** Enter preferences to receive curated recommendations.

## Technologies Used
- **Python:** Core programming language.
- **Streamlit:** For creating the web application interface.
- **Pandas & NumPy:** For data manipulation and analysis.
- **Scikit-learn:** For machine learning models.
- **Docker:** For containerizing the app and ensuring consistent deployment.

## Installation
To set up the project locally or in a containerized environment:

### Prerequisites
- Install [Docker](https://www.docker.com/get-started) (recommended) or Python 3.12 with pip.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/tadeni00/video_game_recommender.git
   cd game-recommendation-system
   ```

2. **For Docker Users**  
   Build the Docker image:
   ```bash
   docker build -t game-recommendation-system .

   ```
   The Docker image for this project has been pushed to Docker Hub. You can pull it and run it on your system using the following command:

   ```bash
   docker pull tadeni/game-recommendation-system:v1
   ```
   
   Run the container:
   ```bash
   docker run -p 8501:8501 game-recommendation-system
   ```

3. **For Python Users**  
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Run the app:
   ```bash
   streamlit run app.py
   ```

## Running the Streamlit App
After successfully building and running the Docker container or running the Python script, you can access the Streamlit app in your browser:

- **URL for Docker:**  
  [http://localhost:8501](http://localhost:8501)
  
- **URL for Python:**  
  Provided in the terminal upon running `streamlit run`.

Once on the app, explore the interface, input preferences, and view personalized game recommendations.

## Usage
1. **Launch the App:**  
   Open the app in your browser using the provided URL.
   
2. **Enter Preferences:**  
   Fill in the required fields, such as favorite genres or gameplay styles.

3. **Get Recommendations:**  
   Click "Get Recommendations" to see tailored game suggestions.


## How It Works
The app leverages a combination of machine learning techniques:
- **Collaborative Filtering:** Recommends games based on user behavior.
- **Content-Based Filtering:** Matches games with similar attributes to user preferences.

A preprocessed dataset of video games is used to train the models, ensuring relevant and accurate recommendations.

## Contributing
Contributions are always welcome! If you'd like to improve the app or add new features:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request describing your updates.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For support or questions, please reach out:
- **Name:** Tomisin Adeniyi
- **Email:** tomisin_adeniyi11@yahoo.com
- **GitHub:** [GitHub Profile](https://github.com/tadeni00)