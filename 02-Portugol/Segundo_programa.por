programa {
  funcao inicio() {
      real valor_total, valor_parte, valor_final
      // valor do produto = R$ 350,00
      // percentual de desconto = 12%
      // valor do desconto = R$ 42,00
    
    escreva("Digite o valor total do produto: ")
    leia(valor_total)
    escreva("Digite o desconto do produto: ")
    leia(valor_parte)

    valor_final = valor_total * (valor_parte / 100)
    escreva("\nSeu valor final é: ", valor_final)
    
  }
}
