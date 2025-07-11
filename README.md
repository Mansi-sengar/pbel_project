🏏 IPL_MATCH_PREDICTUION

create an autoai model using watson studio.
In this project i have use the ibm watson studio which make my work easier and aslo help in the creation of (linear regression,logistic regression, random forest) etc.In this model the watson studio use the MULTICLASS classifier.


🎯 OBJECTIVE
The objective of this project is to leverage IBM Watson Studio's AutoAI to automatically build, train, and deploy a machine learning model that predicts the outcome of IPL (Indian Premier League) matches. By using AutoAI, this project automates key stages of the ML lifecycle — including data preprocessing, algorithm selection, feature engineering, and hyperparameter tuning — enabling efficient and accurate model development without manual coding.

⚫️ This solution is designed to:

⚫️ Enable fast and reproducible model training

⚫️ Provide explainable predictions

⚫️ Support easy deployment for real-time or batch scoring

⚫️ Make machine learning accessible to users with limited coding experience


📌 IPL_MATCH_DEPLOYMENT_LINK

https://au-syd.dai.cloud.ibm.com/ml-runtime/deployments/15cf68e8-da86-40cc-95be-5626f522db7c?space_id=9a5c788c-7ad4-40c7-a0b2-f71a3fcffdfe&context=cpdaas


🔍 Model Experience
This project uses IBM Watson Studio AutoAI, which provides a fully automated machine learning pipeline builder. The AutoAI experiment was configured with the IPL match dataset (matches_csv_shaped) and set to predict match winners based on input features like team names, venue, toss decision, and other match-specific data.


📌Key Highlights:
✅ Data Ingestion: AutoAI automatically detected data types and handled missing values.

🧠 Feature Engineering: AutoAI generated and evaluated multiple feature transformations (e.g., one-hot encoding, normalization).

⚙️ Algorithm Selection: Multiple algorithms (Logistic Regression, Random Forest, XGBoost, etc.) were automatically tested.

🎯 Model Selection: The best pipeline was selected based on accuracy and other performance metrics (e.g., ROC AUC, F1-score).

📊 Leaderboard: AutoAI generated a leaderboard showing the top-performing model pipelines for easy comparison.

📈 Explainability: The final model includes insights like feature importance, helping interpret how the model makes predictions.

🚀 Deployment Ready: The best model was exported and integrated with a custom GUI for real-time IPL match outcome prediction.

