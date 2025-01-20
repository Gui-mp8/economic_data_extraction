import requests

response = requests.get("https://economic-extraction-135061216385.us-central1.run.app/scraper")

print(response.status_code)

# import os
# from google.cloud import storage

# def write_empty_file(bucket_name, file_name, credentials_path):
#     # Set the environment variable for the service account key
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

#     # Initialize a Cloud Storage client with the service account credentials
#     storage_client = storage.Client()

#     # Get the bucket
#     bucket = storage_client.get_bucket(bucket_name)

#     # Create an empty blob (file) in the bucket
#     blob = bucket.blob(file_name)

#     # Upload an empty content to the blob
#     blob.upload_from_string('')

#     print(f"Empty file '{file_name}' has been written to bucket '{bucket_name}'.")

# # Example usage
# bucket_name = 'teste-suzano1'  # Replace with your Cloud Storage bucket name
# file_name = 'test.txt'      # Replace with the desired file name
# credentials_path = 'suzano-challenge.json'  # Path to your service account key file

# write_empty_file(bucket_name, file_name, credentials_path)
