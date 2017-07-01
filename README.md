# Looking glass

looking-glass, também conhecidos por router-server, são roteadores de backbone disponibilizados por algumas operadoras para acesso público, e que possibilitam a verificação de informações bastante úteis para engenheiros de rede mundo afora.


## Funcionalidades
 - Checar o as-path (ou o caminho entre as diversas operadoras) de uma rota anunciada;
 - Testar a conectividade, via PING;
 - Fazer diagnostico de rota, via TRACEROUTE;
 - Checar o tamanho da tabela de roteamento global;


## Instalação
Depois de fazer o clone do projeto, `git clone git@github.com:juniormj/looking_glass.git` Precisará instalar algumas dependências, para o caso Debian/Ubuntu, a instalação do virtualen.

Primeiramente, para a instalação do virtualenv será necessário a instalação do **python-setuptools** com o comando `sudo apt-get install python-setuptools`, após isso poderemos instalar o _virtualenv_, `sudo easy_install virtualenv` e agora isolaremos nosso diretório de trabalho para depois instalarmos as bibliotecas que o sistema depende para ser executado.
`virtualenv nomeDoDiretorio` e para ativar o diretório `source bin/activate`.

Agora vamos instalar algumas dependências do Debian/Ubuntu. `sudo apt-get install build-essential libssl-dev libffi-dev python-dev`. Após isso, já poderemos instalar as dependências do projeto, que se encontra no arquivo requiriment.txt:
```
pip install requiriment.txt

```
