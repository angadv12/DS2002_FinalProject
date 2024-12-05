from google.cloud import storage
import os

# set up gcp credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dsaproj-443805-d8bcb4ccde8c.json"

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to Google Cloud Storage.
    
    Parameters:
        bucket_name (str): Name of the GCS bucket.
        source_file_name (str): Local path to the file to be uploaded.
        destination_blob_name (str): Name of the file in the GCS bucket.
    """
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # upload the file
        blob.upload_from_filename(source_file_name)
        print(f"File '{source_file_name}' successfully uploaded to '{bucket_name}/{destination_blob_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    BUCKET_NAME = "dsaprojfinal"

    # upload cleaned_average_annual_income.csv
    upload_to_gcs(
        bucket_name=BUCKET_NAME,
        source_file_name="cleaned_data/cleaned_average_annual_income.csv",
        destination_blob_name="cleaned_average_annual_income.csv"
    )

    # upload cleaned_average_annual_CPI.csv
    upload_to_gcs(
        bucket_name=BUCKET_NAME,
        source_file_name="cleaned_data/cleaned_average_annual_CPI.csv",
        destination_blob_name="cleaned_average_annual_CPI.csv"
    )
