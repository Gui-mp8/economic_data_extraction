## Docker
docker_build_run:
	docker build -f api.Dockerfile -t suzano-challenge-448218 .
	docker run -p 8000:8000 suzano-challenge-448218

# docker_run:
# 	docker run -p 8000:8000 suzano-challenge-448218

### Terraform
infra:
	terraform -chdir=./terraform init

infra_plan:
	terraform -chdir=./terraform plan

infra_apply:
	terraform -chdir=./terraform apply -auto-approve

infra_destroy:
	terraform -chdir=./terraform destroy -auto-approve