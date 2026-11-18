from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


class RegraNegocioError(Exception):
    """Excecao de dominio para violacoes de regras de negocio."""
    pass


@dataclass
class Veiculo:
    id_veiculo: int
    placa: str
    modelo: str
    capacidade_kg: float
    status_operacional: str = "DISPONIVEL"


@dataclass
class OrdemTransporte:
    id_ordem: int
    codigo_rastreio: str
    origem: str
    destino: str
    peso_carga_kg: float
    id_veiculo: int
    id_usuario: int
    status_ordem: str = "PENDENTE"
    data_criacao: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class LogisticaRepositoryModel:
    """Camada Model responsavel pela persistencia e validacao de regras de negocio."""

    def __init__(self):
        self.veiculos: Dict[int, Veiculo] = {
            1: Veiculo(1, "ABC1D23", "VUC Mercedes-Benz Accelo", 3500.0, "DISPONIVEL"),
            2: Veiculo(2, "XYZ9K88", "Fiorino Furgao", 650.0, "DISPONIVEL"),
        }
        self.ordens: Dict[int, OrdemTransporte] = {}
        self._seq_ordem = 1

    def listar_veiculos(self) -> List[Veiculo]:
        return list(self.veiculos.values())

    def listar_ordens(self) -> List[OrdemTransporte]:
        return list(self.ordens.values())

    def criar_ordem(
        self,
        codigo_rastreio: str,
        origem: str,
        destino: str,
        peso_carga_kg: float,
        id_veiculo: int,
        id_usuario: int = 1,
    ) -> OrdemTransporte:
        if not codigo_rastreio or not origem or not destino:
            raise RegraNegocioError("Todos os campos obrigatorios devem ser preenchidos.")

        if peso_carga_kg <= 0:
            raise RegraNegocioError("O peso da carga deve ser maior que zero.")

        veiculo = self.veiculos.get(id_veiculo)
        if not veiculo:
            raise RegraNegocioError("Selecione um veiculo disponivel valido.")

        if veiculo.status_operacional != "DISPONIVEL":
            raise RegraNegocioError(f"O veiculo {veiculo.placa} nao esta disponivel no momento.")

        if peso_carga_kg > veiculo.capacidade_kg:
            raise RegraNegocioError(
                f"Capacidade excedida: carga de {peso_carga_kg}kg supera o limite de {veiculo.capacidade_kg}kg do veiculo {veiculo.placa}."
            )

        nova_ordem = OrdemTransporte(
            id_ordem=self._seq_ordem,
            codigo_rastreio=codigo_rastreio.strip().upper(),
            origem=origem.strip(),
            destino=destino.strip(),
            peso_carga_kg=peso_carga_kg,
            id_veiculo=id_veiculo,
            id_usuario=id_usuario,
        )
        self.ordens[self._seq_ordem] = nova_ordem
        veiculo.status_operacional = "EM_USO"
        self._seq_ordem += 1
        return nova_ordem

    def concluir_ordem(self, id_ordem: int) -> OrdemTransporte:
        ordem = self.ordens.get(id_ordem)
        if not ordem:
            raise RegraNegocioError("Ordem de transporte nao encontrada.")

        if ordem.status_ordem == "CONCLUIDA":
            raise RegraNegocioError("Esta ordem ja foi concluida anteriormente.")

        ordem.status_ordem = "CONCLUIDA"
        veiculo = self.veiculos.get(ordem.id_veiculo)
        if veiculo:
            veiculo.status_operacional = "DISPONIVEL"
        return ordem