class Gerador_De_Log : 
    def info(self,mensagem):
        return f"[INFO]- {mensagem}"
    
    def alerta(self,mensagem):
        return  f" [ALERTA] - {mensagem}"
    
    def erro(self,mensagem):
        return f"[ERRO] - {mensagem}"

texto = Gerador_De_Log ()

print(texto.info(" Dados Salvos Com Sucesso"))
print(texto.alerta("Seu Armazenamento Esta Esgotando"))
print(texto.erro("Erro Tente Novamente"))