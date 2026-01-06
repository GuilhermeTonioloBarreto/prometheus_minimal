# Prometheus Minimal
O objetivo deste código é disponibilizar um código mínimo possível para o entendimento do banco de dados prometheus

## Pré requisitos
- Conhecimentos básicos em git, docker, dockerfile e docker compose
- Conhecimentos básicos em python

## Funcionamento
- O Prometheus é um banco de dados otimizado em gravação de séries temporais. Ou seja, ele armazena valores (tensão, corrente, temperatura, qualquer dado número) em função do tempo
- O Prometheus realiza uma busca de dados periódica em um servidor http para retirar os dados. O servidor http precisa expor um endpoint chamado /metrics utilizando o método GET. Já a forma da mensagem a ser resgatada via método GET deve estar no formato Prometheus Exposition Format. Um exemplo deste formato se encontra abaixo. 

```
# HELP temperatura Temperatura Ambiente
# TYPE temperatura gauge
temperatura{sensor="sala"} 24.7
temperatura{sensor="cozinha"} 26.1
```

- Neste exemplo, o servidor http foi feito em python

## Como rodar o código
- Clone o repositório em uma pasta do seu computador
- Dentro desta pasta, rode o comando docker compose up -d
- Para verificar o funcionamento do servidor http, verifique a mensagem exibida no link http://localhost:8000/metrics e veja se ele retorna valores de temperatura (a temperatura está aleatória entre 20 e 30 °C)
- Para verificar o funcionamento do banco de dados prometheus, veja se a interface do prometheus aparece no http://localhost:9090/
- Para verificar se os dados estão sendo gravados no banco de dados, na aba Query, escreva a função up e clique no botão "Execute"
   - Se retornar o valor 1, o servidor está sendo lido pelo prometheus
   - Se retornar o valor 0, está tendo algum problemana conexão do prometheus

## Alterando os dados do servidor http
Para alterar os dados sendo lidos pelo prometheus, deve-se alterar os valores gerados pelo servidor http. Desta forma, adicione ou remova valores no código localizado na pasta python/main.py
