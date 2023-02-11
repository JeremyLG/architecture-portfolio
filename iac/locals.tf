locals {
  portfolio_machine_type = "e2-small"
  services = toset(split("\n", trimspace(file("resources/services.txt"))))
}
