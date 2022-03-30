# Project: SimpliFracaoGUI / SimpliFracao
# By: Marco Antonio Benevenuto de Oliveira (Chufretalas)
# Version: 1.0

# O objetivo dessa classe é que ela possa ser usada facilmente em qualquer outro projeto,
# então se sinta livre para usar somente esse arquivo em seu projeto e descartar o main que cria a GUI

class SimpliFracao:
    def __init__(self):
        self.numerador = 0
        self.denominador = 0
        self.numerador_solucoes = []
        self.denominador_solucoes = []
        self.divisores = []

    def _guarda_solucoes(self, num, den, div):
        self.numerador_solucoes.append(num)
        self.denominador_solucoes.append(den)
        self.divisores.append(div)

    def _limpa_resultados(self):
        self.numerador_solucoes.clear()
        self.denominador_solucoes.clear()

    def simplifica(self, num, den):
        # Método principal da classe, ele recebe o numerador e o denominador,
        # simplifica a fração e guarda os resultados

        self._limpa_resultados()  # Em caso da mesma instância chamar simplifica() novamente,
        # é preciso limpar os resulatdos anteriores
        self._guarda_solucoes(num, den, 0)
        self.numerador = num
        self.denominador = den

        if self.numerador > self.denominador:
            menor = self.denominador
            maior = self.numerador
            label = 1

        elif self.numerador < self.denominador:
            menor = self.numerador
            maior = self.denominador
            label = 2

        elif self.numerador == self.denominador:
            label = 3

        divisor = 2
        if label != 3:
            while divisor <= menor:
                if menor % divisor == 0:
                    if maior % divisor == 0:
                        menor = int(menor / divisor)
                        maior = int(maior / divisor)
                        if label == 1:
                            self._guarda_solucoes(maior, menor, divisor)
                        elif label == 2:
                            self._guarda_solucoes(menor, maior, divisor)
                        divisor = 2
                    else:
                        divisor += 1
                else:
                    divisor += 1
        else:
            self._guarda_solucoes(1, 1, self.numerador)

    def get_resultados(self):
        # Devolve o passo-a-passo completo da solução em forma de listas
        return self.numerador_solucoes, self.denominador_solucoes, self.divisores

    def get_resultado_final(self):
        # Devolve somente a fração simplificada (resultado final)
        return self.numerador_solucoes[-1], self.denominador_solucoes[-1]
