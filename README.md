# eBay Price Tracker

A simple Python script that searches eBay for products using the **eBay Browse API** and saves the results to a CSV file.

## Features
- Search for products on eBay (Sandbox or Production).
- Filter results by minimum and maximum price.
- Save results (title, price, currency, link) into a timestamped CSV file.
- Shows a preview of the first 5 results in the terminal.

## Requirements
- Python 3.8+
- eBay Developer Account (Sandbox or Production App Keys)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/Best_Ebay_Prices.git
   cd Best_Ebay_Prices
````

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

3. Create a `requirements.txt` with the following:

   ```
   requests
   ```

4. Open the script `Ebay.py` and replace the placeholders:

   ```python
   CLIENT_ID     = "YOUR_CLIENT_ID"
   CLIENT_SECRET = "YOUR_CLIENT_SECRET"
   ```

## Usage

Run the script:

```bash
python Ebay.py
```

Example run:

```
Enter product keyword (e.g. 'xiaomi 14'): iphone 16 pro max
Minimum price (blank for none): 300
Maximum price (blank for none): 1000
Getting OAuth token...
Searching eBay Sandbox...
Found 5 items.
Saved results to ebay_results_20250913_153055.csv
- iPhone Test Item | 499.99 USD | https://sandbox.ebay.com/itm/123456789
...
```

The results are saved to a CSV file named like:

```
ebay_results_20250913_153055.csv
```

with the following format:

| Title       | Price  | Currency | Link         |
| ----------- | ------ | -------- | ------------ |
| iPhone Test | 499.99 | USD      | https\://... |

## Sandbox vs Production

* **Sandbox**: For testing with fake listings.
  Token & API calls use `https://api.sandbox.ebay.com/...`.

* **Production**: For real eBay listings.
  Requires Production App Keys from the eBay Developer Dashboard.
  Token & API calls use `https://api.ebay.com/...`.

Switch between Sandbox and Production by updating:

* `BASE_URL` in the script
* `CLIENT_ID` and `CLIENT_SECRET` values

## License

MIT


