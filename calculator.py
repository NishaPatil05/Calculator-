from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def add(a, b):
    """Perform addition operation"""
    return a + b

def subtract(a, b):
    """Perform subtraction operation"""
    return a - b

def multiply(a, b):
    """Perform multiplication operation"""
    return a * b

def divide(a, b):
    """Perform division operation with zero division handling"""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed")
    return a / b

@app.route('/')
def index():
    """Serve the calculator HTML page"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle calculation requests"""
    try:
        data = request.get_json()
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        operation = data.get('operation')
        
        # Perform the selected operation
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({'result': result})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)