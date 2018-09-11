# ubicomp2018
Repositório para estudos 

Integração com Arduino

A biblioteca Javino foi incluída neste projeto para que fosse possível a comunicação via porta serial com o arquivo python que irá gerar os gráficos.

Instalação do sensor de temperatura no Arduino:
- Conecte o pino ground do sensor ao ground do arduino;
- Conecte o pino do meio do sensor na porta analógica a ser utilizada no arduino;
- Conecte o pino vcc do sensor na porta vcc equivalente a 5V do arduino;

Instalação do sensor de luminosidade no Arduino:
- Conecte um pino do sensor ao ground do arduino;
- Conecte o outro pino a porta analógica a ser utilizada no arduino, colocando entre o sensor e a porta uma resistência de 10k ohm a ser conectada a porta vcc de 5V do arduino;

Codificação do Arduino:
- Inclua e declare a biblioteca do Javino
  •  #include <Javino.h>
  •  Javino javino;
- leia os valores das portas analogicas instaladas através da funação "analogRead(ports)"
- transforme o valor de temperatura recebido em celsius atraves da operação: 
  •  (val)*0.00488*100) 
- Envie os dados recebidos através da função : 
  •  javino.sendmsg(dados);

Obs.: para que os valores das portas analogicas corretamente deve se colocar a seguinte função antes: 
  •  byte PORTA = analogRead(porta);

## CONFIGURAÇÕES PYTHON ##

Instalar no Python a versão oficial do matplotlib

python -mpip install -U pip
python -mpip install -U matplotlib

Em seguida instale o pyserial

python -mpip install -U pyserial

Especificar a porta de conexão de acordo com a que o equipamento foi conectado
Linhas 74 do arquivo ubicomp-grafico-1809.py

serial.Serial('COM7', 9600, timeout=0)

E pronto! 
O código está pronto para ser executado

