import sys
import base64

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]

def criar_dicionario_usuarios_senhas(usuarios, senhas, arquivo_claro, arquivo_base64):
    # Cria o dicionário em texto claro
    with open(arquivo_claro, 'w') as f_claro:
        for usuario in usuarios:
            for senha in senhas:
                f_claro.write(f"{usuario}:{senha}\n")
    
    # Lê o dicionário em texto claro e converte para base64
    with open(arquivo_claro, 'r') as f_claro:
        linhas = f_claro.readlines()
    
    with open(arquivo_base64, 'w') as f_base64:
        for linha in linhas:
            linha_base64 = base64.b64encode(linha.encode()).decode()
            f_base64.write(f"{linha_base64}\n")
    
    print(f"Processo concluído. Arquivos salvos:\n- Texto claro: {arquivo_claro}\n- Base64: {arquivo_base64}")

if __name__ == "__main__":
    # Verifica se todos os argumentos foram fornecidos
    if len(sys.argv) != 5:
        print("Uso: python gerar_dicionario.py <arquivo_usuarios> <arquivo_senhas> <arquivo_claro> <arquivo_base64>")
        print("Exemplo: python gerar_dicionario.py usuarios.txt senhas.txt dicionario_claro.txt dicionario_base64.txt")
        sys.exit(1)
    
    # Recebe os argumentos da linha de comando
    arquivo_usuarios = sys.argv[1]
    arquivo_senhas = sys.argv[2]
    arquivo_claro = sys.argv[3]
    arquivo_base64 = sys.argv[4]
    
    # Lê os usuários e senhas dos arquivos
    usuarios = ler_arquivo(arquivo_usuarios)
    senhas = ler_arquivo(arquivo_senhas)
    
    criar_dicionario_usuarios_senhas(usuarios, senhas, arquivo_claro, arquivo_base64)
