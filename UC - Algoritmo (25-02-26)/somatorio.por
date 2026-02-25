programa{
    funcao inicio(){
        inteiro numero, i, soma

        escreva("Digite um número: ")
        leia(numero)

        soma = 0
        i = 1

        enquanto(i <= numero) {
           soma = soma + i
           i = i + 1  
        }

        escreva("A soma de 1 até ", numero, " é ", soma)
    }
}