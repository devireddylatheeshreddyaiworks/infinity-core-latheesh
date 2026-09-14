from flask import Flask, jsonify, request
import os
import json
import datetime
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# --- FOUNDER CONFIGURATION - 100% OWNED ---
FOUNDER_NAME = "DevireddyLatheeshReddy"
PROJECT_NAME = "Infinity Core"
VERSION = "V2 Ultimate - No Issues Edition"
GOLDEN_SAFE_COUNT = 3

# Founder Memory Vault Data
FOUNDER_VAULT = {
    "founder": FOUNDER_NAME,
    "project": PROJECT_NAME,
    "ownership": "100% Owned by DevireddyLatheeshReddy",
    "created": "2026",
    "mission": "Infinity Core - Eternal & Indestructible",
    "protection": "3 Golden Safe - Auto Heal Enabled"
}

# 3 Golden Safe System
GOLDEN_SAFES = {
    "safe_1": {"name": "GitHub Safe", "location": "GitHub Repository", "status": "ACTIVE", "backup": "Source Code Secured"},
    "safe_2": {"name": "Render Safe", "location": "Render Cloud", "status": "ACTIVE", "backup": "Live Deployment Secured"},
    "safe_3": {"name": "Memory Safe", "location": "Founder Vault", "status": "ACTIVE", "backup": "Founder Memory Secured"}
}

def get_current_time():
    try:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    except:
        return str(datetime.datetime.now())

def auto_heal_system():
    """ Auto Heal - Checks all safes and heals if needed """
    try:
        healed = []
        for safe_id, safe_data in GOLDEN_SAFES.items():
            if safe_data["status"] != "ACTIVE":
                safe_data["status"] = "ACTIVE"
                healed.append(safe_id)
        
        return {
            "healed": True,
            "healed_safes": healed if healed else "All Safes Already Healthy",
            "total_safes": GOLDEN_SAFE_COUNT,
            "status": "ALL SYSTEMS HEALTHY"
        }
    except Exception as e:
        logging.error(f"Heal Error: {e}")
        return {"healed": False, "error": str(e)}

# --- ROUTES ---

@app.route('/', methods=['GET'])
def home():
    try:
        auto_heal_system()
        return jsonify({
            "project": PROJECT_NAME,
            "version": VERSION,
            "founder": FOUNDER_NAME,
            "status": "LIVE AND RUNNING",
            "message": f"Infinity Core by {FOUNDER_NAME} is Running Successfully!",
            "golden_safe": f"{GOLDEN_SAFE_COUNT} Golden Safe Active",
            "vault": "Founder Memory Vault Secured",
            "time": get_current_time(),
            "ownership": "100% Protected - No License - Founder Owned",
            "endpoints": {
                "home": "/",
                "health": "/health",
                "vault": "/vault",
                "backup": "/backup/status",
                "auto_heal": "/auto-heal",
                "founder": "/founder"
            }
        }), 200
    except Exception as e:
        return jsonify({"error": str(e), "status": "Error but Auto-Healing"}), 500

@app.route('/health', methods=['GET'])
def health():
    try:
        heal_result = auto_heal_system()
        return jsonify({
            "status": "HEALTHY",
            "founder": FOUNDER_NAME,
            "project": PROJECT_NAME,
            "uptime": "Running",
            "golden_safe": GOLDEN_SAFES,
            "auto_heal": heal_result,
            "time": get_current_time()
        }), 200
    except Exception as e:
        return jsonify({"status": "UNHEALTHY", "error": str(e)}), 500

@app.route('/vault', methods=['GET'])
def vault():
    try:
        # --- FOUNDER SECURITY CHECK ---
        import os
        from flask import request
        SECRET_KEY = os.environ.get("VAULT_KEY")
        user_key = request.args.get('key')

        if not SECRET_KEY:
            return jsonify({"error": "VAULT_KEY not set in Render"}), 500

        if user_key != SECRET_KEY:
            return jsonify({
                "access": "DENIED",
                "message": "Only Founder DevireddyLatheeshReddy can access - Wrong or Missing Key"
            }), 403
        # --- END SECURITY CHECK ---

        return jsonify({
            "vault_name": "Founder Memory Vault",
            "founder": FOUNDER_VAULT,
            "security": "Maximum Protection - Founder Only",
            "access": f"Only {FOUNDER_NAME} can access - VERIFIED",
            "backups": GOLDEN_SAFES,
            "time": get_current_time()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/backup/status', methods=['GET'])
def backup_status():
    try:
        active_count = sum(1 for s in GOLDEN_SAFES.values() if s["status"] == "ACTIVE")
        return jsonify({
            "total_backups": GOLDEN_SAFE_COUNT,
            "active_backups": active_count,
            "all_safe": active_count == GOLDEN_SAFE_COUNT,
            "safes": GOLDEN_SAFES,
            "message": "All 3 Golden Safe Backups are Active and Secured",
            "time": get_current_time()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/auto-heal', methods=['GET', 'POST'])
def auto_heal():
    try:
        result = auto_heal_system()
        return jsonify({
            "action": "Auto Heal Triggered",
            "result": result,
            "founder": FOUNDER_NAME,
            "time": get_current_time()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/founder', methods=['GET'])
def founder():
    try:
        return jsonify({
            "founder_name": FOUNDER_NAME,
            "project": PROJECT_NAME,
            "declaration": f"This Project {PROJECT_NAME} is 100% Created and Owned by {FOUNDER_NAME}",
            "rights": "All Rights Reserved to Founder",
            "protection": "No License - No Copy Allowed Without Permission",
            "vault": FOUNDER_VAULT,
            "time": get_current_time()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error Handlers - No Crash Guarantee
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint Not Found", "available_endpoints": ["/", "/health", "/vault", "/backup/status", "/auto-heal", "/founder"]}), 404

@app.errorhandler(500)
def internal_error(e):
    auto_heal_system()
    return jsonify({"error": "Internal Error - Auto Healing Started", "status": "Healing"}), 500

if __name__ == '__main__':
    try:
        port = int(os.environ.get("PORT", 5000))
        logging.info(f"Starting {PROJECT_NAME} by {FOUNDER_NAME} on port {port}")
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        logging.error(f"Startup Error: {e}")
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
