programa {
  funcao inicio() {
     // declarando as variáveis
    real peso, altura, imc
    cadeia nome

    escreva("Digite seu nome: ")
    leia(nome)

    escreva("Digite seu peso: ")
    leia(peso)
    escreva("Digite sua altura: ")
    leia(altura)

    // não esquecer de colocar a multiplicação entre parênteses (altura * altura)
    imc = peso / (altura * altura)
    escreva("---Bem vindo---", nome, "\nSeu imc é: ", imc)


  }
}
