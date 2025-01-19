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
  location      = "US"
  force_destroy = true
  project       = "suzano-challenge-teste1"
  public_access_prevention = "enforced"
}

resource "google_artifact_registry_repository" "my_repository" {
  name     = "suzano"
  location = "us-central1"
  format   = "DOCKER"
  project  = "suzano-challenge-teste1"
}
