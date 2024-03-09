variable "credentials" {
  description = "Service account credentials"
  default     = "./keys/gcp-servic-acc-key.json"
}

variable "project" {
  description = "project"
  default     = "kinetic-bond-416323"
}

variable "region" {
  description = "project region"
  default     = "us-central1"
}

variable "location" {
  description = "project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "BigQuery dataset name"
#   type        = string
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Storage bucket name"
  default     = "kinetic-bond-416323-terra-bucket"
}

variable "gcs_storage_class"{
    description = "Storage class for GCS bucket"
    default    = "STANDARD"
}