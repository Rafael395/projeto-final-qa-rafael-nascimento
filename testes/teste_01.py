import requests

# Configuração
url = "https://jsonplaceholder.typicode.com/posts/1"

# Execução
response = requests.get(url)

# Testes
if response.status_code == 200:
    print("✅ Status 200 OK")
else:
    print(f"❌ Falha: Status {response.status_code}")

if response.json()["userId"] == 1:
    print("✅ userId correto (== 1)")
else:
    print("❌ userId incorreto")

print("\nResposta completa da API:", response.json())
