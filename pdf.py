from fpdf import FPDF
#Para usar a biblioteca acima é preciso dar o comando abaixo
#pip install fpdf
#Esse comando é executado no terminal, pode ser abaixo, no VSCode, onde tem a saída de dados do seu programa em Python;

def gerandoPDF():
    pdf = FPDF() #Essa linha cria uma variável que vai armazenar as informações da função FPDF da bibliotec
    pdf.add_page() #Essa linha cria uma página em PDF, em branco ainda.
    pdf.set_font("Arial", size=20) #Essa linha é definida que os textos irão aparecer na fonte Arial e no tamanho de 20pt (lembra do word? igual.)
    pdf.image('imagem.png', x = 85, y = None, w = 50, h = 50) # Essa linha é para adicionar uma imagem, é uma função, observe, abaixo vou explicar cada posiçõa:
    """
    'imagem.png' -> é o arquivo de imagem que você quer adicionar no seu PDF
    x = 85 -> isso é o deslocamento na horizontal (para direita ou esquerda), se você colocar None a imagem vai ficar à esquerda.
    y = None -> isso é o deslocamento na vertical (de cima para baixo), se colocar None a imagem vai ficar no canto superior do PDF
    w = 50 -> isso é a Width, ou Largura da imagem
    h = 50 -> isso é a Height, ou altura da imagem

    #OBS: O arquivo deve esta na mesma pasta onde você ta criando o seu código em python, observe se a imagem está aparecendo no explorador à esquerda no VScode.
    """
    cont = 0
    #abaixo vou criar uma string que vai aparecer no PDF:
    mensagem = (f'Primeira linha do pdf',
                f'Segunda linha do pdf'
                f'Terceira e última linha do pdf'
    )
    linhas = 3
    while cont < linhas:  
        pdf.cell(100, 10, txt=str(mensagem[cont]), ln=100, align='L')
        cont = cont + 1
    """
    Explicando as linhas de cima:
    pdf.cell() é para adicionar linhas (ou células) no nosso arquivo PDF.
    100 é a largura de cada linha,
    10 é a altura
    txt = str(mensagem[cont]) é para pegar a linha correspondente da variável mensagem e adicionar no pdf
    align='L' é para o texto ficar alinhado à esquerda (LEFT)
    Tente entender porque foi usado o WHILE e como?
    """
    pdf.image('outra_imagem.png', x = 70, y = None, w = 80, h = 30)
    #Na linha acima o que foi feito? Adicionado outra imagem depois do texto.
    pdf_name = "cupom.pdf" # aqui definimos o nome do arquivo que vai ser gerado
    pdf.output(pdf_name) #aqui o arquivo é criado na mesma pasta onde você está trabalhando.
    
    print(f'O pdf {pdf_name} foi criado com sucesso')
