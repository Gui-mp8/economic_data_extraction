def scrape_china_index(self, **kwargs):
    """Scrape Chinese Caixin Services Index data and return as JSON."""
    url = "https://sbcharts.investing.com/events_charts/eu/596.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        if "attr" in data:
            df = pd.DataFrame(data['attr'])

            colunas_relevantes = {
                'timestamp': 'date',
                'actual': 'actual_state',
                'actual_formatted': 'close',
                'forecast_formatted': 'forecast'
            }

            df_filtrado = df[list(colunas_relevantes.keys())].rename(columns=colunas_relevantes)

            df_filtrado['date'] = pd.to_datetime(df_filtrado['date'], unit='ms')

            df_filtrado.to_csv('include/csv/china_index.csv', index=False)
            print("Dados filtrados e salvos com sucesso.")
        else:
            print("Erro: Dados não encontrados no JSON.")
    else:
        print(f"Erro ao acessar a URL. Código de status: {response.status_code}")