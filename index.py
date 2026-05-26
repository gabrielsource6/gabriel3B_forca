# ============================================================
# JOGO DA FORCA - VERSÃO APRIMORADA
# Disciplina: Programação no Desenvolvimento de Sistemas
# Turma: 3º Ano do Ensino Médio Técnico
# ============================================================

import random
import unicodedata

# 1ª MELHORIA: Dicionário organizado por temas/categorias
banco_palavras = {
    "Tecnologia": ["python", "programação", "algoritmo", "software", "internet"],
    "Jogos": ["minecraft", "valorant", "tetris", "console", "futebol"],
    "Escola": ["professor", "caderno", "biblioteca", "caneta", "diretoria"],
    "Filmes": ["avatar", "titanic", "shrek", "matrix", "vingadores"]
}

# 2ª MELHORIA: Desenho da forca em formato ASCII
FORCA_DESENHOS = [
    """
       +---+

       |   |
           |

           |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |

           |
           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |

       |   |
           |

           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |

           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |

           |
           |
    =========
    """,
    """
       +---+

       |   |
       O   |
      /|\\  |
      /    |

           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def remover_acentos(texto):
    """3ª MELHORIA: Remove acentos para facilitar a validação da digitação."""
    return "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def escolher_tema_e_palavra():
    """Permite ao usuário escolher o tema do jogo."""
    print("Escolha um tema para jogar:")
    temas = list(banco_palavras.keys())
    
    for i, tema in enumerate(temas, 1):
        print(f"{i} - {tema}")
        
    while True:
        try:
            opcao = int(input("Digite o número do tema: "))
            if 1 <= opcao <= len(temas):
                tema_escolhido = themes = themes = temas[opcao - 1]
                palavra = random.choice(banco_palavras[tema_escolhido])
                return tema_escolhido, palavra
        except ValueError:
            pass
        print("Opção inválida. Tente novamente.")

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra ocultando as letras não descobertas."""
    resultado = ""
    for letra in palavra:
        letra_sem_acento = remover_acentos(letra)
        if letra_sem_acento in letras_acertadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogar():
    print("=" * 40)
    print("        JOGO DA FORCA - PYTHON")
    print("=" * 40)
    
    tema, palavra_secreta = escolher_tema_e_palavra()
    palavra_limpa = remover_acentos(palavra_secreta)
    
    letras_acertadas = []
    letras_tentadas = []
    erros = 0
    max_erros = 6
    pontos = 0

    print("\nJogo iniciado!")
    print(f"Tema escolhido: {tema}")

    while erros < max_erros:
        # Exibe o estado atual da forca
        print(FORCA_DESENHOS[erros])
        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
        print("Letras já tentadas:", letras_tentadas)
        print("Pontos:", pontos)
        print("-" * 40)

        letra = input("Digite uma letra: ").lower()
        letra = remover_acentos(letra)

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas UMA letra.")
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra_limpa:
            print("Boa! A letra existe na palavra.")
            letras_acertadas.append(letra)
            # Ganha pontos para cada ocorrência da letra
            pontos += palavra_limpa.count(letra) * 10
        else:
            print("Ops! Essa letra não está na palavra.")
            erros += 1
            pontos -= 2

        # Verifica vitória
        venceu = all(letra in letras_acertadas for letra in palavra_limpa)

        if venceu:
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU!")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)
            break

    if erros == max_erros:
        print(FORCA_DESENHOS[erros])
        print("=" * 40)
        print("FIM DE JOGO! VOCÊ FOI ENFORCADO!")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)
        print("=" * 40)

if __name__ == "__main__":
    jogar()
