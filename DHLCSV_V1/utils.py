
import requests
import streamlit as st

@st.cache_data(show_spinner=False)
def search_commodity_code(query):
    url = "https://www.trade-tariff.service.gov.uk/api/v2/commodities/search"
    try:
        response = requests.get(url, params={"q": query}, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("data"):
            return data["data"][0]["attributes"]["commodity_code"]
    except Exception:
        pass
    return "UNKNOWN"

def get_commodity_code(desc):
    return search_commodity_code(desc)

def estimate_weight(desc):
    desc = desc.lower()
    if "shoes" in desc or "sneaker" in desc or "boot" in desc:
        return 1.3
    elif "jacket" in desc or "coat" in desc:
        return 1.5
    elif "bag" in desc or "handbag" in desc:
        return 0.9
    elif "watch" in desc:
        return 0.4
    elif "belt" in desc or "wallet" in desc:
        return 0.3
    elif "scarf" in desc:
        return 0.2
    elif "shirt" in desc or "t-shirt" in desc or "dress" in desc:
        return 0.7
    else:
        return 0.5
