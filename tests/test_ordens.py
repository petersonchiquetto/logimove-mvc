import pytest
from src.models.entities import LogisticaRepositoryModel, RegraNegocioError


@pytest.fixture
def repo():
    return LogisticaRepositoryModel()


def test_criar_ordem_sucesso(repo):
    ordem = repo.criar_ordem("  br-100 ", "Curitiba", "Blumenau", 500.0, id_veiculo=2)
    assert ordem.id_ordem == 1
    assert ordem.codigo_rastreio == "BR-100"
    assert ordem.status_ordem == "PENDENTE"
    assert repo.veiculos[2].status_operacional == "EM_USO"


def test_bloqueio_excesso_de_peso(repo):
    with pytest.raises(RegraNegocioError, match="Capacidade excedida"):
        repo.criar_ordem("BR-101", "Curitiba", "Joinville", 800.0, id_veiculo=2)


def test_bloqueio_veiculo_indisponivel(repo):
    repo.criar_ordem("BR-102", "Doca A", "Doca B", 200.0, id_veiculo=2)
    with pytest.raises(RegraNegocioError, match="nao esta disponivel"):
        repo.criar_ordem("BR-103", "Doca C", "Doca D", 100.0, id_veiculo=2)


def test_concluir_ordem_libera_veiculo(repo):
    ordem = repo.criar_ordem("BR-104", "Matriz", "Filial", 1200.0, id_veiculo=1)
    ordem_finalizada = repo.concluir_ordem(ordem.id_ordem)
    assert ordem_finalizada.status_ordem == "CONCLUIDA"
    assert repo.veiculos[1].status_operacional == "DISPONIVEL"