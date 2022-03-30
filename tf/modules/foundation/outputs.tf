output "log_group_arn" {
  value = module.logging.log_group.arn
}

output "log_group_name" {
  value = module.logging.log_group.name
}

output "bot_secret_arns" {
  value = module.bot_secrets.secret_arns
}
