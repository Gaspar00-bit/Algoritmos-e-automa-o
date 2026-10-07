import subprocess


def executar(comando):
    resultado = subprocess.run(comando, shell=True)

    if resultado.returncode != 0:
        return False

    return True


print("================================")
print("          GIT DEPLOY")
print("================================")


# 1. Verificar alterações
resultado = subprocess.run(
    "git status --porcelain",
    shell=True,
    capture_output=True,
    text=True
)

if not resultado.stdout.strip():
    print()
    print("Nenhuma alteração encontrada.")
    print("Nada para fazer.")
    exit(0)

print()
print("Alterações encontradas.")

# 2. Mostrar alterações
print()
print("Arquivos modificados:")
subprocess.run("git status --short", shell=True)

# 3. Pedir mensagem do commit
print()
commit_message = input("Mensagem do commit: ")

# 4. Validar mensagem
if not commit_message.strip():
    print()
    print("Erro: a mensagem do commit não pode estar vazia.")
    exit(1)

# 5. Adicionar alterações
print()
print("→ git add .")

if not executar("git add ."):
    print("Erro ao adicionar os arquivos.")
    exit(1)

# 6. Criar commit
print("→ Criando commit...")

if not executar(f'git commit -m "{commit_message}"'):
    print("Erro ao criar o commit.")
    exit(1)

# 7. Fazer push
print()
print("→ Enviando para o GitHub...")

if not executar("git push -u origin main"):
    print()
    print("Erro ao fazer push.")
    exit(1)

print()
print("================================")
print("       DEPLOY CONCLUÍDO")
print("================================")