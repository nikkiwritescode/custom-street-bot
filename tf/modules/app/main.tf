locals {
  application_name        = "custom-street-bot"
  application_description = "The Custom Street Bot is a Discord bot that performs a wide variety of tasks in the Custom Street server."
  container_port          = 8080
}

##
## ECS Module / Task Definition / Cluster / Service
##

module "custom_street_bot_ecs" {
  source  = "app.terraform.io/nikkiautomatesthings/ecs-task/aws"
  version = "1.0.2"

  app_version                         = var.app_version
  region                              = "us-east-2"
  module_name                         = local.application_name
  allow_cross_account_events          = false
  create_supporting_eventbridge_items = false
  create_log_groups                   = false
  log_group_name                      = "/aws/ecs/${local.application_name}"
  log_group_arn                       = var.log_group_arn

  # Task Definition Settings
  task_launch_type = "FARGATE"
  task_runtime     = "ARM64"
  task_definitions = {
    custom-street-bot = {
      command = []

      # Task Settings
      task_type      = "Service"
      task_cpu_units = 256
      task_memory    = 512
      task_policy    = ""

      # Desired Count if task_type is Service, Cron Expression if task_type is Scheduled
      desired_count_or_cron_expression = tostring(var.desired_count)

      # Load Balancer Settings for Services
      attach_lb_to_service        = false
      assign_public_ip_to_service = true
      target_group_arn            = ""

      # ECR Repo Settings
      ecr_repo_arn = var.ecr_repo_arn
      ecr_repo_uri = var.ecr_repo_uri

      # Container-level Settings
      container_cpu_units    = 0   # 0 in the container_cpu spot means managed by Fargate,
      container_memory       = 512 # but you can't put a 0 in the container_memory spot.
      container_is_essential = true

      # Network Settings
      container_port_mappings = {}
      network_mode    = "awsvpc"
      security_groups = ["sg-029d251194a216528"]
      subnets         = ["subnet-04af99511687f8a98", "subnet-09b5b228c5543e99f"]

      # Environment Variables
      env_vars = var.env_vars
      secrets  = var.secrets_config
    }
  }
}
