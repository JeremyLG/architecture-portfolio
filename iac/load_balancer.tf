### These resources are created only if you specify a personal DNS
### and you want to redirect your instances to an https subdomain like 
### portfolio.yourdns, for example portfolio.example.com

# Put our instance in an unmanaged instance group
resource "google_compute_instance_group" "portfolio" {
  zone        = var.zone
  name        = "portfolio"
  description = "portfolio instance group"

  instances = [
    google_compute_instance.portfolio_instance.id,
  ]
  network = google_compute_network.portfolio.id

  named_port {
    name = "http3000"
    port = "3000"
  }
  depends_on = [
    google_project_service.services
  ]
}

# Give access to portfolio VM for our load balancer
resource "google_compute_firewall" "portfolio-lb" {
  name          = "allow-loadbalancerhttpportfolio"
  direction     = "INGRESS"
  network       = google_compute_network.portfolio.id
  source_ranges = ["130.211.0.0/22", "35.191.0.0/16"]
  target_tags   = ["portfolio"]
  allow {
    protocol = "tcp"
    ports    = ["3000"]
  }
  depends_on = [
    google_project_service.services
  ]
}

# Global adress IP for our DNS record creation
resource "google_compute_global_address" "portfolio" {
  name = "portfolio"
  depends_on = [
    google_project_service.services
  ]
}

output "ipv4_lb_portfolio" {
  value = google_compute_global_address.portfolio.address
}

# Health check to our portfolio VM
resource "google_compute_health_check" "portfolio" {
  name               = "portfolio-health-check"
  timeout_sec        = 1
  check_interval_sec = 1
  http_health_check {
    port               = 3000
    port_specification = "USE_FIXED_PORT"
    proxy_header       = "NONE"
    request_path       = "/"
  }
  depends_on = [
    google_project_service.services
  ]
}

# Back-end for our load balancer
resource "google_compute_backend_service" "portfolio" {
  name                  = "portfolio-backend"
  protocol              = "HTTP"
  port_name             = "http3000"
  load_balancing_scheme = "EXTERNAL_MANAGED"
  timeout_sec           = 30
  health_checks         = [google_compute_health_check.portfolio.id]
  backend {
    group           = google_compute_instance_group.portfolio.self_link
    balancing_mode  = "UTILIZATION"
    capacity_scaler = 1.0
  }
  depends_on = [
    google_project_service.services
  ]
}

resource "google_compute_url_map" "portfolio" {
  name            = "web-map-httpportfolio"
  default_service = google_compute_backend_service.portfolio.id
  depends_on = [
    google_project_service.services
  ]
}

resource "google_compute_managed_ssl_certificate" "portfolio" {
  provider = google-beta
  name     = "myservice-ssl-cert"

  managed {
    domains = [
      "portfolio.${var.dns}"
    ]
  }
  depends_on = [
    google_project_service.services
  ]
}

resource "google_compute_target_https_proxy" "portfolio" {
  provider = google-beta
  name     = "portfolio-https-proxy"
  url_map  = google_compute_url_map.portfolio.id
  ssl_certificates = [
    google_compute_managed_ssl_certificate.portfolio.name
  ]
  depends_on = [
    google_project_service.services
  ]
}

resource "google_compute_global_forwarding_rule" "portfolio" {
  name                  = "http-content-rule-portfolio"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL_MANAGED"
  port_range            = "443"
  target                = google_compute_target_https_proxy.portfolio.id
  ip_address            = google_compute_global_address.portfolio.id
  depends_on = [
    google_project_service.services
  ]
}
