import grpc 
import calc_pb2, calc_pb2_grpc

SERVER_IP = "192.168.0.50"

def main():
	channel = grpc.insecure_channel(f"{SERVER_IP}:50051")
	stub = calc_pb2_grpc.CalculatorStub(channel)
	
	a = int(input("digite um numero: "))
	b = int(input("digite um numero: "))
	
	print("\nsomando...")
	print(stub.Somar(calc_pb2.CalcRequest(num1=a, num2=b)).result)
	
	print("\nsubtraindo...")
	print(stub.Subtrair(calc_pb2.CalcRequest(num1=a, num2=b)).result)
	
	print("\nmultiplicando...")
	print(stub.Multiplicar(calc_pb2.CalcRequest(num1=a, num2=b)).result)
	
	print("\ndividindo...")
	print(stub.Dividir(calc_pb2.CalcRequest(num1=a, num2=b)).result)
	
if __name__=="__main__":
	main()  