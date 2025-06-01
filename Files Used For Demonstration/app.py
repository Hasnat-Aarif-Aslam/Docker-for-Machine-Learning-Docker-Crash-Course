from flask import Flask, request, render_template_string

app = Flask(__name__)

# A very simple HTML template with an input form and conditional result display.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Multiplication Table Generator</title>
</head>
<body>
    <h1>Enter an Integer to Generate Its Multiplication Table</h1>
    <form action="/table" method="get">
        <label for="number">Number:</label>
        <input 
            type="text" 
            id="number" 
            name="number" 
            placeholder="e.g. 7" 
            required 
            pattern="\\d+"
            title="Please enter a positive integer."
        />
        <button type="submit">Generate Table</button>
    </form>

    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}

    {% if table %}
        <h2>Multiplication Table for {{ original_number }}</h2>
        <table border="1" cellpadding="5" cellspacing="0">
            <thead>
                <tr>
                    <th>n</th>
                    <th>n × {{ original_number }}</th>
                </tr>
            </thead>
            <tbody>
                {% for i, row in table %}
                    <tr>
                        <td>{{ i }}</td>
                        <td>{{ row }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    """
    Renders the HTML form. No table is shown here until the user
    submits a value to /table.
    """
    return render_template_string(HTML_TEMPLATE, error=None, table=None, original_number=None)


@app.route("/table", methods=["GET"])
def show_table():
    """
    Reads the 'number' query parameter, validates it as an integer,
    builds a multiplication table (1 through 10), and re-renders the same template
    with the table data.
    """
    number_str = request.args.get("number", "").strip()
    if not number_str:
        # No input provided
        return render_template_string(
            HTML_TEMPLATE,
            error="Please enter a number.",
            table=None,
            original_number=None
        )

    # Validate that the input is an integer (only digits, no sign or spaces).
    if not number_str.isdigit():
        return render_template_string(
            HTML_TEMPLATE,
            error=f"“{number_str}” is not a valid positive integer. Please enter digits only.",
            table=None,
            original_number=None
        )

    # Convert to int
    n = int(number_str)

    # Build a list of tuples: (multiplier, product)
    # For example: [(1, 7), (2, 14), …, (10, 70)] if n=7
    multiplication_table = [(i, i * n) for i in range(1, 11)]

    return render_template_string(
        HTML_TEMPLATE,
        error=None,
        table=multiplication_table,
        original_number=n
    )


if __name__ == "__main__":
    # Run the Flask development server in debug mode on http://localhost:5000/
    app.run(host = '0.0.0.0', debug=True)
