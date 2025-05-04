import os
import re
import pandas as pd
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Load dataset
df = pd.read_csv("data/Car_Models.csv")

@app.route("/")
def index():
    """
    Render the homepage with company dropdown
    """
    companies = sorted(df['Company'].unique())
    print(f"[DEBUG] Loaded companies: {companies}")
    return render_template("index.html", companies=companies)


@app.route("/help")
def help():
    """
    Render the help page
    """
    return render_template("help.html")


@app.route("/get_models", methods=["POST"])
def get_models():
    """
    Return a list of models based on selected company
    """
    company = request.form.get("company")
    models = df[df["Company"] == company]["Model"].unique().tolist()
    print(f"[DEBUG] Models for {company}: {models}")
    return jsonify(models)


def compute_hp_per_dollar(car: dict) -> str:
    """
    Compute Horsepower per $1000 for a given car dictionary
    """
    try:
        hp_match = re.search(r'(\d+)\s*hp', car.get('Horsepower', ''), re.IGNORECASE)
        hp = int(hp_match.group(1)) if hp_match else 0

        price_match = re.search(r'\$(\d+(?:,\d{3})*)', car.get('Price', ''))
        price = int(price_match.group(1).replace(',', '')) if price_match else 0

        if hp > 0 and price > 0:
            ratio = round(hp / (price / 1000), 2)
            return str(ratio)
    except Exception as e:
        print(f"[DEBUG] Error calculating HP per $1000: {e}")
    
    return "N/A"


@app.route("/compare", methods=["POST"])
def compare():
    """
    Compare selected car models and return performance metrics
    """
    selected_models = request.form.getlist("models[]")
    print(f"[DEBUG] Selected models for comparison: {selected_models}")

    comparison_data = df[df["Model"].isin(selected_models)].to_dict(orient="records")

    for car in comparison_data:
        car["HP per $1000"] = compute_hp_per_dollar(car)
    
    return jsonify(comparison_data)


@app.route("/chat", methods=["POST"])
def chat():
    """
    Use OpenAI GPT to provide car buying advice based on user input
    """
    user_message = request.json.get('message', '')
    print(f"[DEBUG] Chat input: {user_message}")

    system_prompt = (
        "You are a knowledgeable car buying advisor. Your role is to help users make informed decisions about vehicle purchases."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        message = response.choices[0].message.content
        print(f"[DEBUG] Chat response: {message}")
        return jsonify({"response": message})
    
    except Exception as e:
        print(f"[DEBUG] OpenAI API error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
