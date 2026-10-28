## Data Quality Notes
- Source: World Bank World Development Indicators (CC BY 4.0), year 2019 (chosen to avoid COVID-era distortions).
- Scope: 48 Sub-Saharan Africa countries (World Bank regional grouping).
- Female secondary enrollment was dropped: 29 of 48 countries had no value.
- Eritrea, Equatorial Guinea and South Sudan were dropped for missing values (45 countries remain).
- GDP per capita is highly skewed, so its natural log is used.
- The Central African Republic reports a life expectancy of 31.5 years in 2019, far below neighbours and its own values in other years. It is kept in the data, and models are checked with and without it.