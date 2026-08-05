variable "ec2_instance_type" {
  default = "m7i-flex.large"
  type= string
}
variable "ami_id"{
    default = "ami-01a00762f46d584a1"
    type= string
}
variable "volume_size"{
    default = "25"
    type= string
}