from flask import Flask, jsonify, request
from currency_converter.exchange import get_exchange_rate, convert_amount, get_supported_currencies

app = Flask(__name__)

@app.route('/api/getExchangeRate', methods=['GET'])
def get_exchange_rate_route():
    base_currency = request.args.get('baseCurrency')
    target_currency = request.args.get('targetCurrency')
    
    if not base_currency or not target_currency:
        return jsonify({'error': 'Missing required parameters: baseCurrency and targetCurrency'}), 400
    
    rate = get_exchange_rate(base_currency, target_currency)
    return jsonify({'exchangeRate': rate})

@app.route('/api/convertAmount', methods=['GET'])
def convert_amount_route():
    base_currency = request.args.get('baseCurrency')
    target_currency = request.args.get('targetCurrency')
    amount = request.args.get('amount', type=float)
    
    if not base_currency or not target_currency or amount is None:
        return jsonify({'error': 'Missing required parameters: baseCurrency, targetCurrency, and amount'}), 400
    
    converted_amount = convert_amount(base_currency, target_currency, amount)
    return jsonify({'convertedAmount': converted_amount})

@app.route('/api/getSupportedCurrencies', methods=['GET'])
def get_supported_currencies_route():
    currencies = get_supported_currencies()
    return jsonify({'supportedCurrencies': currencies})

if __name__ == '__main__':
    app.run(debug=True)
