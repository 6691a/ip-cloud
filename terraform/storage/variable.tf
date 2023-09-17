variable "root" {
    description = "The root path of the project"
    type = string
    default = "/Users/kimjun/Documents/projects/playhub"
}

variable "credentials_path" {
  type = string
  default = "gcp_credential.json"
}

variable "region" {
  type = string
  default = "asia-northeast1"
}

variable "folder_name" {
  type = string
  default = "statics"
}

variable "location" {
  type = string
  default = "ASIA"
}

variable "storage_class" {
  type = string
  default = "STANDARD"
}

locals {
  credentials_path = "${var.root}/${var.credentials_path}"
  credentials = jsondecode(file(local.credentials_path))
  project = local.credentials.project_id
  folder = "${var.folder_name}/"

}
