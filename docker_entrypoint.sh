#!/bin/sh

set -e # fail on error
#set -x # debug prints

KEY_TYPE="${SSH_KEY_TYPE:-rsa}"

mkdir -p ~/.ssh
echo "${SSH_KEY:?}" > ~/.ssh/"id_$KEY_TYPE"
chmod 600 ~/.ssh/"id_$KEY_TYPE"

cat > ~/.ssh/known_hosts <<EOF
# gerrit-ssh.volvocars.biz:22 SSH-2.0-GerritCodeReview_3.4.3 (APACHE-SSHD-2.6.0)
gerrit-ssh.volvocars.biz ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYa/+ixG3zYeStMak5HJolI9YJtEE9NP83kGAyDc/UEV8Vj5koAeOO7YUEj9asq714fTZYP/e8MCzPl14YfpSAfaYPpZIUTe9nZzdf0UGzQAVw/90sot9NxceGc6rpl5ZXS0Sq6qRqPUijw0Eijpqu5jgrq8+MkN8d5InpXskyCZFEsEbxHqtLAd7mFrqZ5Bs939OlOZ0y7iy7R8idyq9lrhYArBeUFK3cI8in3n4mOCAmKJ1ibzhZ15ggR1HDTa78ZlTPRTt6Ym0EIO2eHmK7uc9mj+MwyW7/m/nKP/pImNY2/99++olBvjYeNA9VTqiSF0IETSh4htIKThDtQ2R/
# gerrit-ssh.volvocars.biz:22 SSH-2.0-GerritCodeReview_3.4.3 (APACHE-SSHD-2.6.0)
gerrit-ssh.volvocars.biz ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNgTw9M7imDUNVtOIVVCqVAEDJssPlEbtSlQYYhlxr+j7ECKtmiGc9ECE3YEySZdd75gbA4irlnxv8arq5so9Qs=
# gerrit-ssh.volvocars.biz:22 SSH-2.0-GerritCodeReview_3.4.3 (APACHE-SSHD-2.6.0)
# gerrit-ssh.volvocars.biz:22 SSH-2.0-GerritCodeReview_3.4.3 (APACHE-SSHD-2.6.0)
gerrit-ssh.volvocars.biz ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKHt9ujSMROQRo4iiGseIE8YqoFRY32Ier9Fjf68dGJt
# gerrit-ssh.volvocars.biz:22 SSH-2.0-GerritCodeReview_3.4.3 (APACHE-SSHD-2.6.0)
EOF

exec "$@"
