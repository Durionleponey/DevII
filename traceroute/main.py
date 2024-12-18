#!/usr/bin/env python3

import argparse
import subprocess
import re
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="tracert simplifié affichant uniquement les adresses IP des sauts.")
    parser.add_argument("target", help="URL ou adresse IP cible pour le tracert.")
    parser.add_argument("-p", "--progressive", action="store_true", help="Affiche les adresses IP au fur et à mesure.")
    parser.add_argument("-o", "--output-file", type=str, help="Fichier pour enregistrer les adresses IP.")
    return parser.parse_args()

def extract_ip(line):
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ipv6_pattern = r'\b(?:[A-Fa-f0-9]{1,4}:){1,7}[A-Fa-f0-9]{1,4}\b'
    match = re.search(ipv4_pattern, line) or re.search(ipv6_pattern, line)
    return match.group(0) if match else None

def write_ip(ip, output_file):
    if output_file:
        with open(output_file, 'a') as f:
            f.write(ip + '\n')

def tracert_progressive(target, output_file):
    process = subprocess.Popen(["tracert", target], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in iter(process.stdout.readline, ''):
        ip = extract_ip(line)
        if ip:
            print(ip)
            write_ip(ip, output_file)
    process.wait()

def tracert_non_progressive(target, output_file):
    try:
        result = subprocess.run(["tracert", target], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)
    ips = [extract_ip(line) for line in result.stdout.splitlines()]
    ips = [ip for ip in ips if ip]
    for ip in ips:
        print(ip)
    if output_file:
        try:
            with open(output_file, 'w') as f:
                f.write('\n'.join(ips) + '\n')
        except IOError as e:
            print(f"Erreur d'écriture: {e}", file=sys.stderr)
            sys.exit(1)

def main():
    args = parse_arguments()
    if args.progressive:
        tracert_progressive(args.target, args.output_file)
    else:
        tracert_non_progressive(args.target, args.output_file)

if __name__ == "__main__":
    sys.argv = ['main.py', 'ephec.be', '-p', '-o', 'resultat.txt']
    main()
