from flask import Flask, request, redirect, jsonify
import string
import random

app = Flask(__name__)

# In-memory database to store URL mappings
url_database = {}
base_url = "http://localhost:5000/"

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url_code = ''.join(random.choice(characters) for _ in range(6))
    while short_url_code in url_database:
        short_url_code = ''.join(random.choice(characters) for _ in range(6))
    return short_url_code

@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.get_json()
    original_url = data.get('original_url')
    if not original_url:
        return jsonify({"error": "No URL provided"}), 400
    short_url_code = generate_short_url()
    url_database[short_url_code] = original_url
    return jsonify({"short_url": base_url + short_url_code})

@app.route('/<short_url_code>', methods=['GET'])
def redirect_to_original_url(short_url_code):
    original_url = url_database.get(short_url_code)
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({"error": "URL not found"}), 404

@app.route('/urls', methods=['GET'])
def get_all_url_mappings():
    return jsonify(url_database)

if __name__ == "__main__":
    app.run(debug=True)
