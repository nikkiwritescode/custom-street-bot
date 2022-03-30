
provider "aws" {
  region = "us-east-2"

  dynamic "assume_role" {
    for_each = var.assume_role_arn == null ? [] : [1]
    content {
      role_arn    = var.assume_role_arn
      external_id = var.assume_role_external_id
    }
  }

  default_tags {
    tags = {
      CreatedBy   = "Terraform"
      Environment = "production"
      Project     = "custom-street-bot-foundation"
    }
  }
}
