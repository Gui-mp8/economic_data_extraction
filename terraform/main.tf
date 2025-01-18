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
#   credentials = file("./suzano-challenge.json")
#   project     = "suzano-challenge"
#   region      = "us-central1"  # choose your region
# }

resource "google_storage_bucket" "auto-expire" {
  name          = "tf-suzano-challenge-bucket"
  location      = "US"
  force_destroy = true
  project       = "suzano-challenge"

  public_access_prevention = "enforced"
}