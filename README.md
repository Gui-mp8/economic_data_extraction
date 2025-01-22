# Economic data Extraction

This project uses Terraform with GCP to scraps data from [Chinese Index](https://br.investing.com/economic-calendar/chinese-caixin-services-pmi-596), [Bloomberg Commodity Index](https://br.investing.com/indices/bloomberg-commodity) and [USD/CNY Index](https://br.investing.com/currencies/usd-cny) make available these 3 tables at **BigQuery** for analysis.

## Pre-Requisites

Before running the code, ensure you have the following tools installed:

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [Google Cloud Account](https://cloud.google.com/free?hl=en)

## Configuration

After creating the Google Cloud Account you will need pass trough some steps

- Step 1 : [Create a service account key](https://youtu.be/dj9fxiuz4WM?t=66)

- Step 2 : at terraform directory, if not created, create a directory inside of it called `credentials`, and save the service account key with the name of `suzano-challenge.json`, or change the key name.

- Step 3 : Modify the file `config.yaml` at the main directory with the respective data of your project