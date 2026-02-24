programa {
    funcao inicio(){
      real valorImovel, salario, prestacaoMensal
      inteiro anos, meses

      escreva("Digite o valor da casa? ")
      leia(valorImovel)

      escreva("Qaunto é o seu salário? ")
      leia(salario)

      escreva("Em quantos anos deseja pagar o imovel? ")
      leia(anos)

      meses = anos * 12
      prestacaoMensal = valorImovel / meses

      se(prestacaoMensal > salario * 0.30) {
        escreva("Emprestimo negado!")
      } senao{
        escreva("Emprestimo aceito!")
      }

    }
}