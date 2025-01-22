output "ssh_command" {
  value = "gcloud compute ssh ${google_compute_instance.airflow.name} --zone=${google_compute_instance.airflow.zone}"
}