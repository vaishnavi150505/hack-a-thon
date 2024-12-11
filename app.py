from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to fetch HackerRank details
@app.route('/get_details')
def get_details():
    username = request.args.get('username')

    # Simulate fetching details from HackerRank
    fake_hackerrank_data = {
        "john_doe": {"name": "John Doe", "country": "USA", "badges": ["Gold", "Silver", "Bronze"]},
        "jane_doe": {"name": "Jane Doe", "country": "Canada", "badges": ["Platinum", "Gold"]}
    }

    if username in fake_hackerrank_data:
        return jsonify(fake_hackerrank_data[username])
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
