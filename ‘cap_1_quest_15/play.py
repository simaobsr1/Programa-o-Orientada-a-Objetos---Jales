class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = [] 

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
        else:
            print(f"A música '{musica}' não está na playlist.")

    def listar_musicas(self):
        print(f"Músicas na playlist '{self.nome}':")
        for i, musica in enumerate(self.musicas, start=1):
            print(f"{i}. {musica}")

minha_playlist = Playlist("As Melhores ")

minha_playlist.adicionar_musica("musica A")
minha_playlist.adicionar_musica("musica B")
minha_playlist.adicionar_musica("música C")

minha_playlist.listar_musicas()

minha_playlist.remover_musica("musica B")
minha_playlist.listar_musicas()
