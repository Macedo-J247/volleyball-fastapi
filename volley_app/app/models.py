from pydantic import BaseModel

# Classe referente aos jogadores
class Jogador(BaseModel):
    id_number: int
    nome: str
    email: str
    sexo: str
    idade: int
    categoria: str['Novato', 'Amador', 'Profissional'] | None = None


# Classe referente as partidas (de vôlei)
class Partida(BaseModel):
    id_number: int
    id_jogador_organizador: int
    local: str
    data: str
    hora: str
    categoria: str
    tipo: str
    status: bool


# Classe referente as avaliações para as partidas e/ou aos jogadores que estiveram nela
class Avaliacao(BaseModel):
    id_avaliador: int
    id_avaliado: int
    id_partida: int
    nota: int
    comentario: str
