from google.cloud import storage
import os

def write_empty_txt_to_gcs(bucket_name, destination_blob_name):
    """
    Writes an empty .txt file to a Google Cloud Storage bucket.

    :param bucket_name: Name of the GCS bucket.
    :param destination_blob_name: Path in the bucket to save the empty file (e.g., "folder/empty_file.txt").
    """
    # Temporary local file path
    temp_file_path = "empty_file.txt"

    try:
        # Create an empty file locally
        with open(temp_file_path, "w") as file:
            pass

        # Initialize the GCS client
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # Upload the empty file to GCS
        blob.upload_from_filename(temp_file_path)
        print(f"Empty file uploaded to gs://{bucket_name}/{destination_blob_name}")

    finally:
        # Clean up the local file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print(f"Temporary file {temp_file_path} removed.")

# Example usage
bucket_name = "tf-suzano-challenge-bucket-teste"
destination_blob_name = "test.txt"
write_empty_txt_to_gcs(bucket_name, destination_blob_name)