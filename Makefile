SHELL := /bin/bash

include .env
include includes/gcloud.mk
include includes/iac.mk

.EXPORT_ALL_VARIABLES:

.DEFAULT_GOAL := help

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# ---------------------------------------------------------------------------------------- #
# -- < Variables > --
# ---------------------------------------------------------------------------------------- #

# -- bucket definitions
DEPLOY_BUCKET   := $(PROJECT)-gcs-deploy

# ---------------------------------------------------------------------------------------- #
# -- < Feedback > --
# ---------------------------------------------------------------------------------------- #
# -- display environment variables only on local environment
ifeq ($(RUN_FROM), local)
$(info $(shell printf "=%.s" $$(seq 100)))

$(info BILLING_ID        = $(BILLING_ID))
$(info FOLDER_ID         = $(FOLDER_ID))
$(info ORG_ID            = $(ORG_ID))
$(info PROJECT           = $(PROJECT))
$(info ZONE              = $(ZONE))
$(info REGION            = $(REGION))
$(info DEPLOY_BUCKET     = $(DEPLOY_BUCKET))
$(info DBT_PROJECT       = $(DBT_PROJECT))
$(info DBT_DATASET       = $(DBT_DATASET))
$(info GITHUB_REPO       = $(GITHUB_REPO))

$(info $(shell printf "=%.s" $$(seq 100)))
endif

help: ## Displays the current message
	@awk -F ':.*?##' '/^[^\t].+?:.*?.*?##/ {printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF}' $(MAKEFILE_LIST)

# ---------------------------------------------------------------------------------------- #
# This target will perform the complete setup of the current repository.
# ---------------------------------------------------------------------------------------- #

all: gcloud-init configure-docker dbt-deploy iac-clean iac-deploy ## Initializes the application (project creation, bucket creation, docker upload and iac deployment)

docker:
	@docker build -t portfolio .
	@docker run -it --rm --privileged \
		--name portfolio \
		-p 8000:8000 \
		-p 3000:3000 \
		portfolio
