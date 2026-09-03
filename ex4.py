pedido = {
"cliente": "João Silva",
"prato": "Hambúrguer Artesanal",
"status": "em preparo"
}

pedido["status"] = "saiu para entrega"

print(f'Cliente: {pedido["cliente"]}\nPedido: {pedido["prato"]}\nStatus: {pedido["status"]}')