# terraform {
#   required_providers {
#     google = {
#       source  = "hashicorp/google"
#       version = "~> 4.0"  # use an appropriate version
#     }
#   }
#   required_version = ">= 1.0"
# }

# provider "google" {
#   project     = "suzano-challenge-teste1"
#   region      = "us-central1"  # choose your region
# }

resource "google_storage_bucket" "auto-expire" {
  name          = "tf-suzano-challenge-bucket-teste"
  location      = "us-central1"
  force_destroy = true
  project       = "suzano-challenge-teste1"
  public_access_prevention = "unspecified"
  uniform_bucket_level_access = true

}

resource "google_project_service" "enable_bigquery" {
  project            = "tf-suzano-challenge-bucket-teste"
  service            = "bigquery.googleapis.com"
  disable_on_destroy = false
}