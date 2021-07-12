from conta import Conta
from cliente import Cliente

c = Conta(123, "Nico", 55.0, 1000.0)
print(c.extrato())
print(Conta.codigo_banco())

clt = Cliente("Nico")
print(clt.nome)
clt.nome = "Nico 2"
print(clt.nome)