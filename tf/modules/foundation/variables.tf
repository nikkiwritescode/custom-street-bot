variable "environment" {
  type        = string
  description = "The environment you'd like to deploy into. Value must be one of Development, Staging, or Production."

  validation {
    condition     = upper(var.environment) == "DEVELOPMENT" || upper(var.environment) == "STAGING" || upper(var.environment) == "PRODUCTION"
    error_message = "The environment must be set to Development, Staging, or Production. Capitalization does not matter."
  }
}

variable "kms_key_id" {
  type        = string
  description = "The KMS key that should be used to encrypt this application's secrets."
}
