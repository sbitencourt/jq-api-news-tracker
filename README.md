# Event-Driven Alert System for US Crypto Regulation

<p align="center">
  <img alt="Status: In Progress" src="https://img.shields.io/static/v1?label=Status&message=IN%20PROGRESS&color=green&style=for-the-badge">
</p>

## English

This project implements a **server-side data acquisition pipeline** designed to continuously monitor global news headlines for key terms related to US politics (e.g., Trump, US Government) and cryptocurrency markets (e.g., Bitcoin, Crypto).

The system runs autonomously using **Crontab** and is built entirely using **Bash scripting**, leveraging **cURL** for API interaction and **JQ** for robust JSON processing. The primary goal is to demonstrate a self-contained, lightweight, and resilient data pipeline that collects, parses, and stores volatile, time-sensitive information for subsequent analysis.

## Portuguese

Este projeto implementa um **pipeline de aquisição de dados no lado do servidor** projetado para monitorar continuamente manchetes de notícias globais em busca de termos-chave relacionados à política dos EUA (por exemplo, Trump, Governo dos EUA) e aos mercados de criptomoedas (por exemplo, Bitcoin, Cripto).

O sistema funciona de forma autônoma usando **Crontab** e é construído inteiramente com **scripts Bash**, aproveitando **cURL** para interação com APIs e **JQ** para um processamento robusto de JSON. O objetivo principal é demonstrar um pipeline de dados autossuficiente, leve e resiliente, capaz de coletar, analisar e armazenar informações voláteis e sensíveis ao tempo para análises posteriores.

## How to Use

### Prerequisites

You need the following installed on your Linux system:

* **Bash:** (Default on most Linux distributions)
* **cURL:** For making HTTP requests to the NewsAPI.
* **JQ:** For parsing and manipulating the returned JSON data.
* **Crontab:** For scheduling the script execution.