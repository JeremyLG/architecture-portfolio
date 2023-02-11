resource "google_compute_firewall" "portfolio-iam-ssh" {
  project       = var.project
  name          = "allow-portfolio-ssh-from-iap"
  network       = google_compute_network.portfolio.id
  source_ranges = ["35.235.240.0/20"]
  target_tags   = ["portfolio"]
  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
}

resource "google_compute_network" "portfolio" {
  name                    = "portfolio"
  provider                = google-beta
  auto_create_subnetworks = false
  depends_on = [
    google_project_service.services
  ]
}

resource "google_compute_subnetwork" "portfolio" {
  name          = "portfolio"
  provider      = google-beta
  ip_cidr_range = "10.0.0.0/16"
  region        = var.region
  network       = google_compute_network.portfolio.id
  log_config {
    aggregation_interval = "INTERVAL_10_MIN"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
  depends_on = [
    google_project_service.services
  ]
}

resource "google_compute_instance" "portfolio_instance" {
  name                      = "portfolio"
  machine_type              = local.portfolio_machine_type
  project                   = var.project
  metadata_startup_script   = file("../scripts/pynecone.sh")
  allow_stopping_for_update = true

  depends_on = [
    google_project_service.services,
  ]

  metadata = {
    block-project-ssh-keys = true
    enable_vtpm            = true
    enable-oslogin         = true
  }
  shielded_instance_config {
    enable_integrity_monitoring = true
  }

  boot_disk {
    initialize_params {
      image = data.google_compute_image.debian_image.self_link
      size  = 50
      type  = "pd-balanced"
    }
  }
  network_interface {
    network    = google_compute_network.portfolio.id
    subnetwork = google_compute_subnetwork.portfolio.id
  }
  tags = ["portfolio"]
}
