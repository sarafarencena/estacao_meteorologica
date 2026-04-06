import serial
import json
import requests
import time

PORTA = 'COM5'
BAUD  = 9600
URL   = 'http://localhost:5000/leituras'

def ler_serial():
    print(f'Conectando em {PORTA}...')
    try:
        with serial.Serial(PORTA, BAUD, timeout=2) as ser:
            print('Conectado. Aguardando dados do Arduino...')
            while True:
                linha = ser.readline().decode('utf-8').strip()
                if linha:
                    try:
                        dados = json.loads(linha)
                        resposta = requests.post(URL, json=dados)
                        print(f'Enviado: {dados} → status {resposta.status_code}')
                    except json.JSONDecodeError:
                        print(f'Linha inválida ignorada: {linha}')
                time.sleep(0.1)
    except serial.SerialException as e:
        print(f'Erro de conexão serial: {e}')

if __name__ == '__main__':
    ler_serial()