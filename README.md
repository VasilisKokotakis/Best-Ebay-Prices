
***

# eBay Price Tracker

A simple Python script that searches eBay for products using the **eBay Browse API** and saves the results to a CSV file.

## Features

- Search for products on eBay (Sandbox or Production environment)
- Filter results by minimum and maximum price
- Save results (title, price, currency, link) into a timestamped CSV file
- Displays a preview of the first 5 results directly in the terminal

## Requirements

- Python 3.8 or higher
- eBay Developer Account with app keys (Sandbox or Production)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/VasilisKokotakis/Best_Ebay_Prices.git
   cd Best_Ebay_Prices
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # Linux/macOS
   .venv\Scripts\activate        # Windows
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Prepare `requirements.txt` with this content:

   ```
   requests
   ```

5. Open the script `Ebay.py` and replace the placeholder API credentials:

   ```python
   CLIENT_ID     = "YOUR_CLIENT_ID"
   CLIENT_SECRET = "YOUR_CLIENT_SECRET"
   ```

## Usage

Run the script:

```bash
python Ebay.py
```

Sample interaction:

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

The search results are saved to a CSV file named like:

```
ebay_results_YYYYMMDD_HHMMSS.csv
```

with columns:

| Title        | Price  | Currency | Link                      |
|--------------|--------|----------|---------------------------|
| iPhone Test  | 499.99 | USD      | https://sandbox.ebay.com/... |

## Sandbox vs Production

- **Sandbox:** For testing with fake listings.  
  - API base URL: `https://api.sandbox.ebay.com/`  
  - Use Sandbox app keys  
- **Production:** For real listings.  
  - API base URL: `https://api.ebay.com/`  
  - Use Production app keys from your eBay Developer Dashboard  

You can switch between Sandbox and Production by changing the following in `Ebay.py`:

- `BASE_URL`  
- `CLIENT_ID` and `CLIENT_SECRET`

## License

This project is licensed under the [MIT License](LICENSE).

***

