import requests


url = "http://127.0.0.1:5000/"
data = {
    "sender_gst": "ABCDEFGHIJKLMNOP",
    "sender_mobile": "9810833220",
    "from_addr": {
        "addr": "Hamilton, New York",
        "company_name": "Python Tip",
        "state_code": 9,
        "gst": "EJOTYKSHVFENJYU"
    },
    "transport_details": {
        "transport": "",
        "pOrderNo": "",
        "numberOfPkgs.": "",
        "supplyDateTime": "",
        "supplyPlace": "",
        "vehicleNumber": "",
        "grNumber": ""
    },
    "invoice_number": 156,
    "items": [
        {
            "index": 0,
            "hsn": 3924,
            "qty": 234,
            "rate": 180.0,
            "title": "website design"
        },
        {
            "index": 1,
            "hsn": 3924,
            "qty": 24,
            "rate": 180.0,
            "title": "Water jug"
        },
    ],
    "amountInWords": "Twelve Crore Thirty Four Lakh Fifty Six Thousand Seven Hundred Ninety Nine only",
    "discount": 0,
    "extraCost": 0,
    "totalBeforeTax": 20000,
    "cgst": 0,
    "cgstAmount": 0,
    "sgst": 0,
    "sgstAmount": 0,
    "igst": 18,
    "igstAmount": 360,
    "netAmount": 2360,
}

html = requests.post(url, json=data)
with open("invoice.pdf", "wb") as f:
    f.write(html.content)
