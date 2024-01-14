# AI-Powered-SQL-Query-Generation-with-GeminiAI

## Overview

This project leverages the GeminiAI Generative Model by GOOGLE to generate SQL queries from English questions. The application is designed to take user input in the form of questions related to a predefined SQLite database named STUDENT. The GeminiAI API is used to convert these questions into meaningful SQL queries, and the results are displayed based on the executed queries.

### Prerequisites

Before running the code, ensure you have the required libraries installed. You can install them using:

```bash
pip install -r requirements.txt
```

### Setting up Environment Variables

Create a `.env` file in the project directory and add your Google API key:

```dotenv
GOOGLE_API_KEY=your_api_key_here
```

### Running the Application
Run the main.py file:
```run
streamlit run app.py
