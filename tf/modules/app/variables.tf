variable "app_version" {
  type        = string
  default     = null
  description = "This variable is supplied by CircleCI and is used by ECS to point the Service's container to the latest version of the ECR image."
}

variable "attach_custom_domain" {
  type        = bool
  description = "If set to True, a custom domain will be attached to your function, which can be specified via var.domain_name and var.hosted_zone."
}

variable "desired_count" {
  type        = number
  description = "Desired Count is the number of containers you'd like to keep running. This should be between 1 and 4 and should match the number of subnet_cidrs you pass into var.subnet_cidrs."
  validation {
    condition     = var.desired_count > 0 && var.desired_count < 5
    error_message = "Desired Count must be set to a value between 1 and 4, inclusive. This number should match the number of subnet cidrs you pass into var.subnet_cidrs."
  }
}

variable "ecr_repo_arn" {
  type        = string
  description = "The ARN of the ECR Repo you'd like to pull from."
}

variable "ecr_repo_uri" {
  type        = string
  description = "The URI of the Image that you'd like to pull from ECR."
}

variable "environment" {
  type        = string
  description = "The environment you'd like to deploy into. Value must be one of Development, Staging, or Production."

  validation {
    condition     = upper(var.environment) == "DEVELOPMENT" || upper(var.environment) == "STAGING" || upper(var.environment) == "PRODUCTION"
    error_message = "The environment must be set to Development, Staging, or Production. Capitalization does not matter."
  }
}

variable "env_vars" {
  type        = map(string)
  default     = null
  description = "(Optional) The environment variables you'd like to pass into the function."
}

variable "kms_key_arn" {
  type        = string
  description = "The ARN of the KMS key that should be used to encrypt this application's secrets."
}

variable "log_group_arn" {
  type        = string
  description = "The ARN of the log group you'd like your application to log to."
}

variable "secrets_config" {
  type = map(object({
    secret_arn  = string
    kms_key_arn = string
    secret_vars = map(object({
      var_name_in_secret = string
    }))
  }))
  default     = {}
  description = "Pass the secrets that you'd like your container to use through here, along with a Secrets Manager ARN and a KMS Key to use in decryption processes. For an in-depth explanation of how to supply this variable, see README.md."
}
