terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "nikkiautomatesthings"

    workspaces {
      name = "custom-street-bot-foundation"
    }
  }
}

module "foundation" {
  source = "../../../modules/foundation"

  environment = "production"
  kms_key_id  = "arn:aws:kms:us-east-2:632957227412:key/d27060b4-054c-49f8-b3a0-5fdb1261e01e"
}
