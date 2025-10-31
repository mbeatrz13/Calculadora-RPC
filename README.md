🚀 Projeto RPC - Calculadora Distribuída (gRPC)Este projeto implementa um sistema de Chamada de Procedimento Remoto (RPC) utilizando o framework gRPC (Google Remote Procedure Call) para criar uma calculadora distribuída entre duas Máquinas Virtuais (VMs) isoladas.
O projeto demonstra a configuração de uma rede Bridge (Ponte) estável e a comunicação de baixo nível entre o Servidor (que executa as operações matemáticas) e o Cliente (que requisita os cálculos).

🗺️ Visão Geral da Arquitetura: O sistema é composto por duas Máquinas Virtuais em rede Bridge, permitindo que ambas se comuniquem diretamente com a rede do hospedeiro, garantindo um endereço IP fixo e estável para a comunicação RPC.
  VM Servidor192.168.0.50 | Implementa os métodos da calculadora (Somar, Subtrair, etc.) e escuta na porta 50051.
  Cliente192.168.0.60 | Chama remotamente os métodos do Servidor e exibe os resultados.

⚙️ Desafios e Soluções de Infraestrutura - A parte mais crítica do projeto foi garantir a conectividade estável entre as VMs e a rede física. Resolvido após usar a Bridge e inserir um IP estático em ambas as VMs. 

💻 Configuração do Ambiente e gRPCEm ambas as VMs, foi criado um ambiente virtual Python (venv) para isolar as dependências e evitar conflitos de versão.
1. Dependências e Setup Inicial executado nas VMs Servidor e Cliente:
_Bash _
sudo apt update
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install grpcio grpcio-tools
3. Definição do Contrato (RPC)O arquivo calc.proto define as mensagens (CalcRequest, CalcResponse) e o serviço Calculator com os métodos RPC (Somar, Subtrair, etc.).
4. Compilação do Protocolo  .proto foi compilado em ambas as VMs para gerar os stubs Python necessários para o Servidor e Cliente:
_Bash_
python3 -m grpc_tools.protoc -I=rpc_calc/proto --python_out=rpc_calc/client --grpc_python_out=rpc_calc/client rpc_calc/proto/calc.proto

🚀 Como Executar o Projeto - 
Iniciar o Servidor (VM 192.168.0.50):
_Bash_ 
cd /home/server
source venv/bin/activate
python3 rpc_calc/server/server.py
(O Servidor permanecerá ativo, esperando conexões.)
Executar o Cliente (VM 192.168.0.60):
_Bash_
cd /home/client
source venv/bin/activate
python3 rpc_calc/client/client.py
(O Cliente enviará requisições para o IP 192.168.0.50:50051 e imprimirá os resultados.)

