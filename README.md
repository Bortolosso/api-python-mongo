# api-crud-python

___________________________________________________________________________________

(Backend)Api run:
Pre-requisitos:
- Python 3.8.5
- pip    20.1.1 

1. Esteja no diretorio -> \web-app\python-api-mongo\

2.A Ative sua maquína virtual com o comando:
OBS: Como a api foi feita em um amabiente Windows os diretorios do maquina virtual sao diferentes do Macos e Linux. Portanto segue o passo 2.B.
- Windows -> $ .\venv\Scripts\activate

2.B Caso esteja no ambiente Macos ou Linux:
Macos: 
-(Cria maquina virtual) Rode o comando -> $ python -m env env
-(Inicia maquina virtual) Rode o comando -> $ source env/bin/activate

Linux: 
-(Cria maquina virtual) Rode o comando -> $ python3 -m env env
-(Inicia maquina virtual) Rode o comando -> $ source env/bin/activate

3. Instale todas as depencias e bibliotecas do projeto com o comando:
-Windowns, MacOs, Linux -> $ pip install -r requirements.txt

4. Rode a API com o comando -> $ python app/main.py

Api Restfull -> http://127.0.0.1:8000

Documentação da API(SWAGGER) -> http://127.0.0.1:8000/docs

___________________________________________________________________________________