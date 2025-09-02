class FormatadorDeTexto: 
    def para_caixa_alta(self,texto):
        return texto.upper ()
    
    def  para_caixa_baixa(self,texto):
        return texto.lower()
    
formato = FormatadorDeTexto ()

print(formato.para_caixa_alta("Simão"))
print(formato.para_caixa_baixa("Freires"))