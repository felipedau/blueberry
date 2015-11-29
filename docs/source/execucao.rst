Execução
========
As seções à seguir explicarão como executar um servidor e clientes
para formarem uma rede sem fio *Bluetooth* de sensores de
luminosidade.

blueberrywsn (*Raspberry Pi*)
-----------------------------
Tendo o pacote **blueberrywsn** instalado, basta executar os comandos
descritos a seguir.

Servidor
''''''''
O servidor deve ser executado pelo seguinte comando::

    blueberrywsn server

O servidor passará a aguardar por conexões realizadas pelos
clientes que informarão os níveis de luminosidade de seus respectivos
sensores e exibirá uma interface gráfica com os dispositivos
conectados e o último nível lido de cada.

Cliente
'''''''
O cliente deve ser executado pelo seguinte comando::

    blueberrywsn client

Com o servidor em execução, o *Raspberry Pi* passará a enviar o nível
de luminosidade lido pelo *UNO* periodicamente.

Pressione ``enter`` ou ``ctrl + c`` para parar.

TrabalhoFaculSDAppAndroidBT (*Android*)
---------------------------------------
Com o servidor em execução e o aplicativo instalado, basta iniciá-lo
para que o dispositivo comece a procurar por dispositivos *Bluetooth*
ativos por perto, exibindo uma lista. Apenas toque no servidor e o
dispositivo passará a enviar a leitura do sensor de luminosidade para
o servidor periodicamente.
