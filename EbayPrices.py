#!/usr/bin/env python3
import requests
import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
EBAY_CLIENT_ID = os.getenv("EBAY_CLIENT_ID")
EBAY_CLIENT_SECRET = os.getenv("EBAY_CLIENT_SECRET")

# ===== Replace these with your SANDBOX credentials from eBay Developer Dashboard =====
CLIENT_ID     = "***"
CLIENT_SECRET = "***"

# Base URL for SANDBOX environment
BASE_URL = "https://api.sandbox.ebay.com"

# Get OAuth2 token
def get_oauth_token():
    url = f"{BASE_URL}/identity/v1/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    r = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    r.raise_for_status()
    return r.json()["access_token"]

# Search eBay
def search_ebay(token, query, min_price=None, max_price=None, limit=20):
    url = f"{BASE_URL}/buy/browse/v1/item_summary/search"
    params = {"q": query, "limit": str(limit)}
    filters = []
    if min_price is not None and max_price is not None:
        filters.append(f"price:[{min_price}..{max_price}]")
    elif min_price is not None:
        filters.append(f"price:[{min_price}..]")
    elif max_price is not None:
        filters.append(f"price:[..{max_price}]")
    if filters:
        params["filter"] = ",".join(filters)

    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    return r.json()

# Save to CSV
def save_to_csv(items, filename=None):
    if filename is None:
        filename = f"ebay_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Title", "Price", "Currency", "Link"])
        for it in items:
            title = it.get("title", "")
            price = it.get("price", {}).get("value", "")
            currency = it.get("price", {}).get("currency", "")
            link = it.get("itemWebUrl", "")
            w.writerow([title, price, currency, link])
    return filename

# Run search from UI
def run_search():
    query = entry_query.get().strip()
    min_p = entry_min.get().strip()
    max_p = entry_max.get().strip()

    if not query:
        messagebox.showerror("Error", "Please enter a product keyword.")
        return

    try:
        min_price = float(min_p) if min_p else None
        max_price = float(max_p) if max_p else None
    except ValueError:
        messagebox.showerror("Error", "Invalid price format.")
        return

    try:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Getting OAuth token...\n")
        token = get_oauth_token()

        text_output.insert(tk.END, "Searching eBay Sandbox...\n")
        data = search_ebay(token, query, min_price, max_price, limit=20)

        items = data.get("itemSummaries", [])
        text_output.insert(tk.END, f"Found {len(items)} items.\n")

        if items:
            filename = save_to_csv(items)
            text_output.insert(tk.END, f"Saved results to {filename}\n\n")

            for it in items[:5]:
                title = it.get("title", "")
                price = it.get("price", {}).get("value", "")
                currency = it.get("price", {}).get("currency", "")
                link = it.get("itemWebUrl", "")
                text_output.insert(tk.END, f"- {title} | {price} {currency}\n  {link}\n\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---- Tkinter UI ----
root = tk.Tk()
root.title("eBay Price Tracker (Sandbox)")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

# Product keyword
ttk.Label(frame, text="Product keyword:").grid(row=0, column=0, sticky="w", padx=(0,5))
entry_query = ttk.Entry(frame, width=40)
entry_query.grid(row=0, column=1, columnspan=2, sticky="w")

# Min price
ttk.Label(frame, text="Min price:").grid(row=1, column=0, sticky="w", padx=(0,5))
ttk.Label(frame, text="$").grid(row=1, column=1, sticky="e")
entry_min = ttk.Entry(frame, width=20)
entry_min.grid(row=1, column=2, sticky="w")

# Max price
ttk.Label(frame, text="Max price:").grid(row=2, column=0, sticky="w", padx=(0,5))
ttk.Label(frame, text="$").grid(row=2, column=1, sticky="e")
entry_max = ttk.Entry(frame, width=20)
entry_max.grid(row=2, column=2, sticky="w")

# Search button
btn_search = ttk.Button(frame, text="Search", command=run_search)
btn_search.grid(row=3, column=0, columnspan=3, pady=10)

# Output text box
text_output = tk.Text(frame, width=80, height=20)
text_output.grid(row=4, column=0, columnspan=3)

root.mainloop()
