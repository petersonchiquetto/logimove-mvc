from dataclasses import asdict
from flask import Flask, jsonify, render_template, request
from src.models.entities import LogisticaRepositoryModel, RegraNegocioError

app = Flask(__name__, template_folder="../views")
model = LogisticaRepositoryModel()


@app.route("/", methods=["GET"])
def index_view():
    return render_template("index.html")


@app.route("/api/dados", methods=["GET"])
def obter_dados():
    return jsonify({
        "veiculos": [asdict(v) for v in model.listar_veiculos()],
        "ordens": [asdict(o) for o in model.listar_ordens()],
    }), 200


@app.route("/api/ordens", methods=["POST"])
def registrar_ordem():
    dados = request.get_json() or {}
    try:
        nova_ordem = model.criar_ordem(
            codigo_rastreio=dados.get("codigo_rastreio", ""),
            origem=dados.get("origem", ""),
            destino=dados.get("destino", ""),
            peso_carga_kg=float(dados.get("peso_carga_kg", 0)),
            id_veiculo=int(dados.get("id_veiculo", 0)),
        )
        return jsonify({"mensagem": "Ordem registrada com sucesso!", "ordem": asdict(nova_ordem)}), 201
    except (RegraNegocioError, ValueError) as err:
        return jsonify({"erro": str(err)}), 400


@app.route("/api/ordens/<int:id_ordem>/concluir", methods=["PATCH"])
def finalizar_ordem(id_ordem: int):
    try:
        ordem = model.concluir_ordem(id_ordem)
        return jsonify({"mensagem": "Entrega concluida e veiculo liberado!", "ordem": asdict(ordem)}), 200
    except RegraNegocioError as err:
        return jsonify({"erro": str(err)}), 400