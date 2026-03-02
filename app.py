import sys
import os
import json
from flask import Flask, render_template, request

# Ensure src in python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.io.parser import Parser
from src.core.scorer import Scorer
from src.explain.sensitivity import SensitivityAnalyzer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    analysis = None
    error = None
    
    # default template values for GET to prepopulate the form
    default_domain = "Cloud Infrastructure for E-Commerce"
    default_criteria = [
        {"name": "Monthly Cost", "weight": "0.4", "is_cost": "true", "description": "Lower is better"},
        {"name": "Reliability", "weight": "0.35", "is_cost": "false", "description": "Uptime percentage"},
        {"name": "Team Skill", "weight": "0.25", "is_cost": "false", "description": "Internal team expertise (1-10)"}
    ]
    default_options = [
        {"name": "AWS", "values": {"Monthly Cost": "5000", "Reliability": "99.99", "Team Skill": "9"}},
        {"name": "GCP", "values": {"Monthly Cost": "4500", "Reliability": "99.9", "Team Skill": "7"}},
        {"name": "Azure", "values": {"Monthly Cost": "5500", "Reliability": "99.95", "Team Skill": "8"}}
    ]

    form_data = {
        "domain": default_domain,
        "criteria": default_criteria,
        "options": default_options
    }

    if request.method == "POST":
        try:
            # Parse the form data back into a structured dictionary
            req_data = {
                "domain": request.form.get("domain", "Unknown Domain"),
                "criteria": [],
                "options": []
            }
            
            # Reconstruct Criteria
            criteria_names = request.form.getlist("crit_name[]")
            criteria_weights = request.form.getlist("crit_weight[]")
            criteria_types = request.form.getlist("crit_type[]")
            criteria_desc = request.form.getlist("crit_desc[]")
            
            for i in range(len(criteria_names)):
                name = criteria_names[i].strip()
                if not name: continue
                
                req_data["criteria"].append({
                    "name": name,
                    "weight": float(criteria_weights[i]) if criteria_weights[i] else 0.0,
                    "is_cost": criteria_types[i] == "cost",
                    "description": criteria_desc[i]
                })
                
            # Reconstruct Options
            option_names = request.form.getlist("opt_name[]")
            for i in range(len(option_names)):
                opt_name = option_names[i].strip()
                if not opt_name: continue
                
                opt_values = {}
                for crit in req_data["criteria"]:
                    # Form fields for values are named like: val_<opt_index>_<crit_name>
                    val_key = f"val_{i}_{crit['name']}"
                    raw_val = request.form.get(val_key, "0")
                    try:
                        opt_values[crit["name"]] = float(raw_val)
                    except ValueError:
                        opt_values[crit["name"]] = 0.0
                        
                req_data["options"].append({
                    "name": opt_name,
                    "values": opt_values
                })

            # Create JSON string to pass to the parser (which expects a JSON string right now)
            json_input = json.dumps(req_data)
            
            req = Parser.from_json(json_input)
            scorer = Scorer(req)
            result = scorer.score()
            analysis = SensitivityAnalyzer.analyze(req, result)
            
            # Pass the parsed form data back so it stays populated
            form_data = {
                "domain": req_data["domain"],
                "criteria": [
                    {
                        "name": c["name"],
                        "weight": str(c["weight"]),
                        "is_cost": "true" if c["is_cost"] else "false",
                        "description": c.get("description", "")
                    } for c in req_data["criteria"]
                ],
                "options": [
                    {
                        "name": o["name"],
                        "values": {k: str(v) for k, v in o["values"].items()}
                    } for o in req_data["options"]
                ]
            }
            
        except Exception as e:
            error = str(e)
            
    return render_template("index.html", form_data=form_data, result=result, analysis=analysis, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
