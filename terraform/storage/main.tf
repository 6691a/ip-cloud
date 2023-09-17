terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.82.0"
    }
  }
}

provider "google" {
  credentials = file(local.credentials_path)
  project     = local.project
  region      = var.region
}

resource "google_storage_bucket" "playhub_private" {
  name          = "playhub"
  location      = var.location
  storage_class = var.storage_class
  labels = {
    "type" = "private"
  }
}

resource "google_storage_bucket" "playhub_public" {
  name = "static.playhub.kr"
  location      = var.location
  storage_class = var.storage_class
  labels = {
    "type" = "public"
  }
}

resource "google_storage_bucket_iam_member" "public_read" {
  bucket = google_storage_bucket.playhub_public.name
  role   = "roles/storage.objectViewer"
  member = "allUsers"
}
