# gerar_dicionario
Craição de Wordlist com saída no formato user:pass e tambem encodado em base64 para ataque basic authentication

# Download
$ git clone https://github.com/thiagosmith/gerar_dicionario.git
$ cd gerar_dicionario

# modo de uso
Uso: python gerar_dicionario.py <arquivo_usuarios> <arquivo_senhas> <arquivo_claro> <arquivo_base64>
Exemplo: python gerar_dicionario.py usuarios.txt senhas.txt dicionario_claro.txt dicionario_base64.txt

# exemplo
$ python gerar_dicionario.py usuarios.txt senhas.txt wl_claro.txt wl_b64.txt
Processo concluído. Arquivos salvos:
- Texto claro: wl_claro.txt
- Base64: wl_b64.txt

$ head -n1 wl_claro.txt                                                                                                              
ftp:ftp

$ head -n1 wl_b64.txt  
ZnRwOmZ0cAo=

$ echo ZnRwOmZ0cAo= | base64 -d
ftp:ftp
