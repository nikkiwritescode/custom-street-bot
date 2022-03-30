## Foundation

## This module is designed to host things that need to exist prior to
## the instantiation of the application's infrastructure. Log Groups and
## Secrets are things that we'd really like not to lose should we need to
## terraform destroy and re-create everything. By separating Secrets from
## the actual infrastructure, this gives you time to manually populate them
## so that Terraform never has to know what those values are. (And thus
## these secret values stay out of Terraform's state.)

##
## CloudWatch Log Group
##

module "logging" {
  source  = "app.terraform.io/nikkiautomatesthings/app-logging/aws"
  version = "1.0.0"

  application_name    = "custom-street-bot"
  create_logging_role = false
  task_type           = "ECS"
}

##
## Secrets for Bot Configuration
##

module "bot_secrets" {
  source  = "app.terraform.io/nikkiautomatesthings/secretsmanager-secrets/aws"
  version = "1.0.0"

  application_name = "custom-street-bot"
  environment      = var.environment
  kms_key_id       = var.kms_key_id
  region           = "us-east-2"
  secrets          = ["bot_secrets"]
}
