"""Download World Bank indicators for all countries (one year) into data/raw."""
import requests
import pandas as pd

YEAR = 2019
INDICATORS = {
    "life_expectancy": "SP.DYN.LE00.IN",
    "gdp_per_capita": "NY.GDP.PCAP.CD",
    "health_spending_pct_gdp": "SH.XPD.CHEX.GD.ZS",
    "electricity_access": "EG.ELC.ACCS.ZS",
    "basic_water": "SH.H2O.BASW.ZS",
    "basic_sanitation": "SH.STA.BASS.ZS",
    "female_secondary_enrollment": "SE.SEC.ENRR.FE",
    "urban_population_pct": "SP.URB.TOTL.IN.ZS",
}


def fetch_indicator(code, year):
    """Return {country_code: value} for one indicator and one year."""
    url = f"https://api.worldbank.org/v2/country/all/indicator/{code}"
    params = {"format": "json", "date": year, "per_page": 500}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    records = response.json()[1] or []
    return {r["countryiso3code"]: r["value"] for r in records if r["countryiso3code"]}


def main():
    table = pd.DataFrame()
    for name, code in INDICATORS.items():
        values = fetch_indicator(code, YEAR)
        table[name] = pd.to_numeric(pd.Series(values))
        print(f"{name}: {table[name].notna().sum()} countries with data")
    table.index.name = "Country Code"
    table.to_csv(f"data/raw/wdi_{YEAR}.csv")
    print("Saved data/raw/wdi_2019.csv", table.shape)


if __name__ == "__main__":
    main()