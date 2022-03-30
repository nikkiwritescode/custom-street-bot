variable "app_version" {
  type        = string
  default     = null
  description = "This variable is supplied by CircleCI and is used by ECS to point the Service's container to the latest version of the ECR image."
}

variable "assume_role_arn" {
  type        = string
  default     = null
  description = "The ARN of the role you would like to use to deploy your Prod environment. This role should live inside your Production account and your Terraform user should have permission to assume it."
}

variable "assume_role_external_id" {
  type        = string
  default     = null
  description = "Some roles require an external ID in order to assume them. If the role you specified in dev_assume_role_arn requires one, specify it here. Otherwise you can omit this value."
}
