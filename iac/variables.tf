variable "google_account" {
  type        = string
  sensitive   = true
  description = "Your google account"
}

variable "billing_id" {
  type        = string
  description = "Your billing ID"
}

variable "folder_id" {
  type        = string
  description = "Your folder ID"
}

variable "org_id" {
  type        = string
  description = "Your organization ID"
}

variable "project" {
  type        = string
  description = "Your project"
}

variable "region" {
  type        = string
  description = "The region where to deploy your infrastructure"
}

variable "zone" {
  type        = string
  description = "The zone where to deploy your infrastructure"
}

variable "repository_id" {
  type        = string
  description = "The artifact registry repo of your project"
}

variable "dns" {
  type        = string
  description = "Personal DNS to deploy HTTPS modules like Airbyte, Lightdash"
}
