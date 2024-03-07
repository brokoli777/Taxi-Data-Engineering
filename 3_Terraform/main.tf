terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.19.0"
    }
  }
}

provider "google" {
  
  # Configuration options
  project = "kinetic-bond-416323"
  region  = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "kinetic-bond-416323-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}