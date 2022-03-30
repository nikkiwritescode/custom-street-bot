locals {
  kms_key_arn = "arn:aws:kms:us-east-2:632957227412:key/d27060b4-054c-49f8-b3a0-5fdb1261e01e"
}

terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "nikkiautomatesthings"

    workspaces {
      name = "custom-street-bot"
    }
  }
}

data "terraform_remote_state" "foundation" {
  backend = "remote"

  config = {
    organization = "nikkiautomatesthings"
    workspaces = {
      name = "custom-street-bot-foundation"
    }
  }
}

module "custom_street_bot" {
  source = "../../../modules/app"

  environment          = "production"
  app_version          = var.app_version
  attach_custom_domain = false
  desired_count        = 1

  log_group_arn        = data.terraform_remote_state.foundation.outputs.log_group_arn
  kms_key_arn          = local.kms_key_arn

  ecr_repo_arn = "arn:aws:ecr:us-east-2:632957227412:repository/custom-street-bot"
  ecr_repo_uri = "632957227412.dkr.ecr.us-east-2.amazonaws.com/custom-street-bot"

  secrets_config = {
    bot-secrets = {
      kms_key_arn = local.kms_key_arn
      secret_arn  = data.terraform_remote_state.foundation.outputs.bot_secret_arns["bot_secrets"]
      secret_vars = {
        DEEPL_AUTH_KEY = { var_name_in_secret = "DEEPL_AUTH_KEY" },
        DISCORD_TOKEN  = { var_name_in_secret = "DISCORD_TOKEN" }
      }
    }
  }
}
