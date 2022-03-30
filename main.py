# Project: SimpliFracaoGUI / main
# By: Marco Antonio Benevenuto de Oliveira (Chufretalas)
# Version: 1.0

# O arquivo main é responsável por gerar a GUI e lidar com o I/O de dados

from SimpliFracao import SimpliFracao
import re
import PySimpleGUI as sg


def valida_fracao(fracao):  # Essa função garante que não serão inseridas frações inválidas ou que dividam por 0
    fracao = fracao.strip()
    padrao_fracao = re.compile("[0-9]{1,100}/[0-9]{1,100}")
    match = padrao_fracao.match(fracao)
    if match and fracao[fracao.find("/") + 1:] != "0":
        return True
    else:
        return False


def extrai_valores(fracao):  # Extrai os valores da entrada do usuário
    indexb = fracao.find("/")
    num = int(fracao[:indexb])
    den = int(fracao[indexb + 1:])
    return num, den


def simpl(num, den):  # Instancia a classe SimpliFracao e formata o resultado
    instancia = SimpliFracao()
    instancia.simplifica(num, den)
    num, den, div = instancia.get_resultados()

    # Para melhorar a experiência do usuário, resolvi mostrar o passo-a-passo da simplificação,
    # então foi preciso formatar os valores recebidos pela função get_resultados()
    resultado_str = ""
    for i in range(len(num)):
        resultado_str += f"{num[i]}/{den[i]}" if i == 0 else f"  |{div[i]}->|  {num[i]}/{den[i]}"
    if den[-1] == 1:  # Se a última fração for x/1 é adicionado mais uma string ao resultado que mostra somente x
        resultado_str += f"  |->|  {num[-1]}"
    return resultado_str


def main():
    layout = [[sg.Text("Fração (exemplo: 54/8):")],
              [sg.Input(key="-INPUT-")],
              [sg.Button("Simplifique!")],
              [sg.Text(size=(40, 2), key='-OUT-', background_color="#ffffff", text_color="#000000")]]

    window = sg.Window("Simplificador de Fração", layout)

    while True:
        event, values = window.read()

        if event == "Simplifique!":
            fracao = values["-INPUT-"]
            if valida_fracao(fracao):
                num, den = extrai_valores(fracao)
                resultado_str = simpl(num, den)
                window["-OUT-"].update(resultado_str)
            else:
                window["-OUT-"].update("Fração inválida. Digite novamente.")

        elif event == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    main()
