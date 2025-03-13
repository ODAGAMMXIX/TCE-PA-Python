# TCE-PA-Python
Function "Ord()"

![image](https://github.com/user-attachments/assets/51743cae-3b38-4f93-931c-8577bb09bea4)

Exemplificação com os valores dados
Entrada: "Brasil", 3, 10

Execução da função f("BRASIL", 3, 10):

Iteração 1 (i='B'): r = ord('B') + 10 -> ord('L'); aux = ['L']; arg3 = 11 -> arg3 = 1

Iteração 2 (i='R'): r = ord('R') + 1 -> ord('S'); aux = ['L', 'S']; arg3 = 2

Iteração 3 (i='A'): r = ord('A') + 2 -> ord('C'); aux = ['L', 'S', 'C']; arg3 = 3

Iteração 4 (i='S'): r = ord('S') + 3 -> ord('V'); aux = ['L', 'S', 'C', 'V']; arg3 = 4

Iteração 5 (i='I'): r = ord('I') + 4 -> ord('M'); aux = ['L', 'S', 'C', 'V', 'M']; arg3 = 5

Iteração 6 (i='L'): r = ord('L') + 5 -> ord('Q'); aux = ['L', 'S', 'C', 'V', 'M', 'Q']; arg3 = 6

Resultado final: "LSCVMQ"

![image](https://github.com/user-attachments/assets/34993811-c775-4524-b393-824fe835edea)

Claro, vamos detalhar a execução do script com as entradas fornecidas. Considerando as entradas “Brasil”, “3” e “10”, aqui está o que será escrito na tela e a explicação de cada trecho do código:

### a) O que será escrito na tela

**Será escrito na tela: "LSCVMQ"**

### Justificativa

1. **Função `f(arg1, arg2, arg3)`**
   - `arg1 = "Brasil"`
   - `arg2 = 3`
   - `arg3 = 10`

2. **Processo dentro da função `f()`**

   - **Inicializa lista auxiliar**: `aux = []`
   - **Converte `arg1` para maiúsculas e itera sobre cada letra**:
     - `arg1.upper() = "BRASIL"`

3. **Iteração sobre as letras de `BRASIL`**

   - **Iteração 1 (i='B')**
     - `ord('B') = 66`
     - `(66 - 65 + 1) + 10 = 12` (valor ajustado para dentro do intervalo de 1 a 26)
     - `chr(12 + 65 - 1) = 'L'`
     - `aux = ['L']`
     - `arg3 += 1 -> arg3 = 11 -> arg3 = 1` (reseta arg3 para 1 porque `arg3 = arg2 + 1`)

   - **Iteração 2 (i='R')**
     - `ord('R') = 82`
     - `(82 - 65 + 1) + 1 = 19`
     - `chr(19 + 65 - 1) = 'S'`
     - `aux = ['L', 'S']`
     - `arg3 += 1 -> arg3 = 2`

   - **Iteração 3 (i='A')**
     - `ord('A') = 65`
     - `(65 - 65 + 1) + 2 = 3`
     - `chr(3 + 65 - 1) = 'C'`
     - `aux = ['L', 'S', 'C']`
     - `arg3 += 1 -> arg3 = 3`

   - **Iteração 4 (i='S')**
     - `ord('S') = 83`
     - `(83 - 65 + 1) + 3 = 22`
     - `chr(22 + 65 - 1) = 'V'`
     - `aux = ['L', 'S', 'C', 'V']`
     - `arg3 += 1 -> arg3 = 4`

   - **Iteração 5 (i='I')**
     - `ord('I') = 73`
     - `(73 - 65 + 1) + 4 = 13`
     - `chr(13 + 65 - 1) = 'M'`
     - `aux = ['L', 'S', 'C', 'V', 'M']`
     - `arg3 += 1 -> arg3 = 5`

   - **Iteração 6 (i='L')**
     - `ord('L') = 76`
     - `(76 - 65 + 1) + 5 = 17`
     - `chr(17 + 65 - 1) = 'Q'`
     - `aux = ['L', 'S', 'C', 'V', 'M', 'Q']`
     - `arg3 += 1 -> arg3 = 6`

4. **Concatena a lista `aux` em uma string e retorna**:
   - `return "".join(aux) -> "LSCVMQ"`

5. **Bloco `__main__`**
   - `s = input()` retorna `"Brasil"`
   - `n = int(input())` retorna `3`
   - `c = int(input())` retorna `10`
   - `print(f(s, n, c))` imprime o resultado `"LSCVMQ"`

Espero que essa explicação tenha esclarecido o funcionamento do código e como chegamos ao resultado final. Se precisar de mais alguma coisa, estou aqui para ajudar! 🚀
E se não tivesse a tabela ASCII memorizada?

