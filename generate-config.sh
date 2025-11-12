#!/bin/bash
# Usage: ./generate-config.sh 192.168.1.150
# Replaces <VM_IP> in the template and writes config/prometheus.yml
if [ -z "$1" ]; then
  echo "Palun anna VM IP (näide: 192.168.1.150)"
  echo "Kasutamine: $0 <VM_IP>"
  exit 1
fi
VM_IP="$1"
mkdir -p config
sed "s/<VM_IP>/${VM_IP}/g" config/prometheus.yml.template > config/prometheus.yml
echo "Kirjutas config/prometheus.yml koos IP-ga ${VM_IP}"
echo "Kui Prometheus on juba käimas, lae konfiguratsioon uuesti:"
echo "curl -X POST http://localhost:9090/-/reload"
