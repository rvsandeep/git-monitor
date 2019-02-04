rsync -avL --progress -e "ssh -i /Users/rvsandeep/.ssh/rvsandeep-IAM-keypair.pem" \
      --exclude='.git/' \
      --exclude='dist/' \
      --exclude='env/' \
      --exclude='src/libs/' \
      --exclude='*/__pycache__/' \
      /Users/rvsandeep/git-monitor/ ubuntu@ec2-52-34-246-118.us-west-2.compute.amazonaws.com:/home/ubuntu/git-monitor/
