import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

# Replace with your actual API key and endpoint
API_KEY = "Xe_Q8ZfpuatSGxiICkmGpxYpeCAhspN7m5xjA1GsQ4dO"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/15cf68e8-da86-40cc-95be-5626f522db7c/predictions?version=2021-05-01"
def get_token():
    response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    )
    return response.json().get("access_token")

def predict():
    try:
        values = [
            int(entry_id.get()),
            int(entry_season.get()),
            entry_city.get(),
            entry_date.get(),
            entry_team1.get(),
            entry_team2.get(),
            entry_toss_winner.get(),
            entry_toss_decision.get(),
            entry_result.get(),
            int(entry_win_by_runs.get()),
            int(entry_win_by_wickets.get()),
            entry_player_of_match.get(),
            entry_venue.get()
        ]

        payload = {
            "input_data": [
                {
                    "fields": [
                        "id", "season", "city", "date", "team1", "team2",
                        "toss_winner", "toss_decision", "result",
                        "win_by_runs", "win_by_wickets", "player_of_match", "venue"
                    ],
                    "values": [values]
                }
            ]
        }

        token = get_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }

        response = requests.post(DEPLOYMENT_URL, json=payload, headers=headers)
        result = response.json()

        prediction = result['predictions'][0]['values'][0][0]
        messagebox.showinfo("Prediction Result", f"Predicted Winner: {prediction}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("IPL Match Winner Predictor")

labels = [
    "ID", "Season", "City", "Date (YYYY-MM-DD)", "Team1", "Team2",
    "Toss Winner", "Toss Decision", "Result",
    "Win by Runs", "Win by Wickets", "Player of Match", "Venue"
]

entries = []
for idx, label in enumerate(labels):
    tk.Label(app, text=label).grid(row=idx, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(app, width=40)
    entry.grid(row=idx, column=1, padx=10)
    entries.append(entry)

(
    entry_id, entry_season, entry_city, entry_date, entry_team1,
    entry_team2, entry_toss_winner, entry_toss_decision, entry_result,
    entry_win_by_runs, entry_win_by_wickets, entry_player_of_match, entry_venue
) = entries

tk.Button(app, text="Predict Winner", command=predict).grid(row=len(labels), columnspan=2, pady=20)

app.mainloop()
import pickle

def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model
