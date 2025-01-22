resource "google_compute_instance" "airflow" {
  name         = "ingestdata"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2004-lts"
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral public IP
    }
  }
  metadata_startup_script   = templatefile("compute_engine/start.sh", {"repos" = var.github_full_repo})
  allow_stopping_for_update = true
  service_account {
    email = var.account
    scopes = ["cloud-platform"]
  }
  tags = ["airflow", "http-server", "https-server"]
}


resource "google_compute_firewall" "allow_all_8080" {
  name    = "allow-all-8080"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["8080"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["airflow"]
}
