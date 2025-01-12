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

$ head wl_claro.txt                                                                                                              
ftp:ftp
ftp:anonymous
ftp:msfadmin
ftp:123456789
ftp:service
ftp:postgres
ftp:batman
ftp:shelby
ftp:genesis
ftp:147258

$ head wl_b64.txt  
ZnRwOmZ0cAo=
ZnRwOmFub255bW91cwo=
ZnRwOm1zZmFkbWluCg==
ZnRwOjEyMzQ1Njc4OQo=
ZnRwOnNlcnZpY2UK
ZnRwOnBvc3RncmVzCg==
ZnRwOmJhdG1hbgo=
ZnRwOnNoZWxieQo=
ZnRwOmdlbmVzaXMK
ZnRwOjE0NzI1OAo=

$ echo ZnRwOjE0NzI1OAo= | base64 -d
ftp:147258
