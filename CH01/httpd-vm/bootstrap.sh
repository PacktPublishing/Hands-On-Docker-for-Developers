#!/usr/bin/env bash

dnf -y update
dnf install -y httpd
systemctl start httpd.service
systemctl enable httpd.service
