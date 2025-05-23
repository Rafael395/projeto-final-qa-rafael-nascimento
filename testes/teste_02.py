def soma(a, b):
    return a + b

# Testes (executados apenas se rodar com pytest)
def test_soma_positivos():
    assert soma(2, 3) == 5, "❌ 2 + 3 deve ser 5"

def test_soma_negativos():
    assert soma(-1, 1) == 0, "❌ -1 + 1 deve ser 0"

# Execução manual (para Google Colab/GitHub sem pytest)
if __name__ == "__main__":
    try:
        test_soma_positivos()
        test_soma_negativos()
        print("✅ Todos os testes de soma passaram!")
    except AssertionError as e:
        print(e)
