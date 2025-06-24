
# 📦 DHL CSV Generator (for Fashion Dropshipping)

This Streamlit app allows you to upload a spreadsheet (e.g. from Numbers or Excel), automatically fills in key DHL shipment details, and lets you review and edit the data before exporting a final DHL-compatible CSV file.

---

## ✅ Features

- 📤 Upload Excel file with item descriptions, prices, quantities, etc.
- 🧠 Auto-fill:
  - UK Commodity Code via official API
  - Estimated weight (based on item type)
  - Default country of origin = CN
- ✏️ Real-time manual edits in browser (Streamlit frontend)
- 📥 Export DHL-ready CSV file (no header, correct column order)

---

## 📁 How to Use Locally

```bash
git clone https://github.com/yourusername/dhl-editor-app.git
cd dhl-editor-app
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this folder to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and deploy
4. Upload an `.xlsx` file (must contain: Item Description, Quantity, Value, Currency)

---

## 📌 Output Format (no header)

```
1,INV_ITEM,"LV SPEEDY BAG",42022100,1,PCS,1200,GBP,0.9,,CN,,,N
```

Ready for upload to: [mydhl.express.dhl](https://mydhl.express.dhl/gb/en/shipment/item-upload-file-guidelines.html#/csv_txt)
