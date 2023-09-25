# Author Panagiotopoulos Ioannis
# Tampere University | Security Protocols Fall 23'
# Exercise 2, Tutorial 3
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# Question
#The CA is a trusted entity that issues digital certificates and performs key management of public keys.
#The CA is well known and trusted by all principals in a communication instance. In this exercise, you
#are tasked with creating your own root CA to issue and sign certificates for your use.
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
#Once you have created the root CA, you will be ready to sign digital certificates. To do so:
#• Generatea private and public key pair for a user;
#• Generate a Certificate Signing Request (CSR). In a real world scenario, the CSR
#will be sent to the CA for verification and digital signature creation.
#• Generate a certificate based on the CSR.The certificate is generated by the CA signing the CSR.
#Hint: Use the linux command line for this task.


#!/bin/sh

mkdir certs
cd certs

# generate an RSA 2048 key
openssl genrsa -des3 -out ex2CA.key 2048
# generate a root x509 cert with 1024 days until expiration | In other words we generate the public key which is exposed to the users who can acess this host name by the given network
openssl req -x509 -new -nodes -key ex2CA.key -sha256 -days 1024 -out ex2CA.crt
#generate a server certificate key
openssl genrsa -out ioannispanagiotopoulos.com.key  2048
#generate a CSR
openssl req -new -key ioannispanagiotopoulos.com.key -out ioannispanagiotopoulos.com.csr
#generate the server crt along with the root CA key | public key of the server
openssl x509 -req -in ioannispanagiotopoulos.com.csr -CA ex2CA.crt -CAkey ex2CA.key -CAcreateserial -out ioannispanagiotopoulos.com.crt -days 1024 -sha256

