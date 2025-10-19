from pydantic import BaseModel
from typing import Literal, Optional
from datetime import date, time


# Classe referente aos jogadores
class Jogador(BaseModel):
    id_number: Optional[int] = None
    nome: str
    idade: int
    sexo: Literal['Masculino', 'Feminino', 'Não Informar']
    categoria: Literal['Novato', 'Amador', 'Profissional']
    email: Optional[str]
    avaliacoes: Optional[int] = 0


# Classe referente as partidas (de vôlei)
class Partida(BaseModel):
    id_number: Optional[int] = None
    id_organizador: int
    local: str
    data: date
    hora: time
    jogadores: list[int] = []
    tipo: Literal['2x2', '4x4', '6x6']
    nivel_minino: Literal['Novato', 'Amador', 'Profissional']
    status: Literal['Em Espera', 'Em Andamento', 'Terminada']


# Classe referente a adesão em uma partida
class Adesao(BaseModel):
    id_number: Optional[int] = None
    id_jogador: int
    id_partida: int
    data_adesao: date
    hora_adesao: time
    status: Literal['Aceita', 'Recusada', 'Em Espera']
    observacao: Optional[str] = None


# Classe referente as avaliações para as partidas e/ou aos jogadores que estiveram nela
class Avaliacao(BaseModel):
    id_number: int
    id_avaliador: int
    id_avaliado: int
    id_partida: int
    nota: int
    comentario: Optional[str] = None
