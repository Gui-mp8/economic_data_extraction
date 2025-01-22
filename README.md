# Economic data Extraction

This project uses Terraform with GCP to scraps data from [Chinese Index](https://br.investing.com/economic-calendar/chinese-caixin-services-pmi-596), [Bloomberg Commodity Index](https://br.investing.com/indices/bloomberg-commodity) and [USD/CNY Index](https://br.investing.com/currencies/usd-cny) make available these 3 tables at **BigQuery** for analysis.

## Archtecture
![Image](https://github.com/user-attachments/assets/08d53b91-442d-46b4-9380-f595ccd9dffa)

## Pre-Requisites

Before running the code, ensure you have the following tools installed:

- [Docker](https://docs.docker.com/engine/install/ubuntu/)

- [Google Cloud Account](https://cloud.google.com/free?hl=en)

- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

## Configuration

After creating the Google Cloud Account you will need pass trough some steps

- Step 1 : [Create a service account key](https://youtu.be/dj9fxiuz4WM?t=66)

- Step 2 : at terraform directory, if not created, create a directory inside of it called `credentials`, and save the service account key with the name of `suzano-challenge.json`, or change the key name.

- Step 3 : Modify the file `config.yaml` at the main directory with the respective data of your project

- Step 4 : install make to run Makefile's

    ```
    sudo apt -y install make
    ```

## Execution

Step 1 -  Clone the repository:
```
git clone git@github.com:Gui-mp8/economic_data_extraction.git
```

Step 2 -  Run terraform (Run each line separately):
```
make infra
make infra_plan
make infra_apply
```

> **OBS:** Wait about 5 minutes to airflow become available

Step 3 - Enter at airflow in the IP Address that'll appear at your CMD like `35.192.180.114`, and put at the url like this, `http://35.192.180.114:8081`, and then do the login using admin admin

Step 4 - Run the suzano_challenge dag

## Pipeline
The DAG invoke the Cloud Run API to make the extraction with selenium and requets, and then save this data at Cloud Storage. After saving at Cloud Storage as Parquet, the DAG writes the Tables at BigQuery for the analysis.