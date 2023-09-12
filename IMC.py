import tkinter as tk


# Definições da Calsse IMC Calculator
class IMCCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        # Rótulo e campo de entrada para o nome
        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        # Rótulo e campo de entrada para a altura em metros
        self.altura_label = tk.Label(root, text="Altura (metros):")
        self.altura_label.pack()
        self.altura_entry = tk.Entry(root)
        self.altura_entry.pack()

        # Rótulo e campo de entrada para o peso em quilogramas
        self.peso_label = tk.Label(root, text="Peso (quilogramas):")
        self.peso_label.pack()
        self.peso_entry = tk.Entry(root)
        self.peso_entry.pack()

        # Botão para calcular o IMC
        self.calcular_button = tk.Button(
            root, text="Calcular IMC", command=self.calcular_imc)
        self.calcular_button.pack()

        # Rótulo para exibir o resultado do IMC
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()

    # Método para calcular o IMC
    def calcular_imc(self):
        nome = self.nome_entry.get()
        altura = float(self.altura_entry.get())
        peso = float(self.peso_entry.get())

        # Cálculo do IMC
        imc = peso / (altura ** 2)
        resultado = f"{nome}, seu IMC é: {imc:.2f}"

        # Determinação da categoria do IMC
        if imc < 18.5:
            resultado += " - Abaixo do Peso"
        elif imc < 24.9:
            resultado += " - Peso Normal"
        elif imc < 29.9:
            resultado += " - Sobrepeso"
        else:
            resultado += " - Obesidade"

        # Exibir o resultado na interface gráfica
        self.resultado_label.config(text=resultado)

# Fundo principal


def main():
    root = tk.Tk()
    root.geometry("400x300")  # Definindo o tamanho da janela
    app = IMCCalculator(root)
    root.mainloop()


# Verificar se o script está sendo executado diretamente
if __name__ == "__main__":
    main()

