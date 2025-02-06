# CurrencyConverter API

Цей веб-сервіс дозволяє конвертувати суми між різними валютами за допомогою REST API.

## Кінцеві точки

### 1. GetExchangeRate

**URL:** `/api/getExchangeRate`

**Метод:** GET

**Параметри:**
- `baseCurrency`: Валюта, з якої конвертуємо (наприклад, "USD").
- `targetCurrency`: Валюта, в яку конвертуємо (наприклад, "EUR").

**Приклад:**
