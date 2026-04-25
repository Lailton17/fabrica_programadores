programa {
  funcao inicio() {
    inteiro a,b

    escreva("Digite o primeiro valor: ")
    leia(a)
    escreva("Digite o segundo valor: ")
    leia(b)

    escreva("---Comparações--- \n")
    escreva(" a > b = ", (a>b ou a==b), "\n") //falso
    escreva(" a >= b = ", (a>=b ou a!=b), "\n") //verdadeiro
    escreva(" a < b = ", (a<b ou a>b), "\n") //verdadeiro
    escreva(" a <= b = ", (a<=b ou a==b), "\n") //verdadeiro
    escreva(" a == b = ", (a==b ou a!=b), "\n") //verdadeiro
    escreva(" a != b = ", (a!=b ou a<b), "\n") //verdadeiro
  }
}
