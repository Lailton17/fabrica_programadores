programa {
  funcao inicio() {
    inteiro nota, frequencia, aprovado, reprovado

    escreva("Digite a nota do aluno: ")
    leia(nota)
    escreva("Digite a frequencia do aluno: ")
    leia(frequencia)
  
    escreva("---Comparações--- \n")
    escreva("nota > frequencia = ", (nota>frequencia e nota==frequencia), "\n")
    escreva("nota < frequencia = ", (nota<frequencia ou nota!=frequencia), "\n")
    escreva("nota => frequencia = ", (nota==frequencia e nota>=frequencia), "\n")
    escreva("nota <=frequencia = ", (nota!=frequencia ou nota==frequencia), "\n")

  }
}
