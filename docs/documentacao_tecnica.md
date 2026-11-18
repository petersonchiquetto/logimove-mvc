# Documentação Técnica — Sistema LogiMove (PIT II)

## 1. Escopo e Melhoria Contínua (Kaizen)
Aplicação web baseada no padrão arquitetural MVC para controle de ordens de transporte, alocação de veículos e validação de capacidade máxima de carga.

## 2. Dicionário de Dados (3ª Forma Normal - PostgreSQL)

### Tabela: `usuarios`
- `id_usuario`: SERIAL (PK, NOT NULL) — Identificador único do usuário.
- `nome`: VARCHAR(100) (NOT NULL) — Nome completo do operador ou gestor.
- `email`: VARCHAR(120) (UNIQUE, NOT NULL) — E-mail corporativo.
- `perfil`: VARCHAR(20) (NOT NULL) — Domínio: `'OPERADOR'`, `'GESTOR'`.

### Tabela: `veiculos`
- `id_veiculo`: SERIAL (PK, NOT NULL) — Identificador único do veículo.
- `placa`: VARCHAR(10) (UNIQUE, NOT NULL) — Placa veicular.
- `modelo`: VARCHAR(80) (NOT NULL) — Modelo da frota.
- `capacidade_kg`: NUMERIC(10,2) (NOT NULL) — Capacidade máxima em kg (> 0).
- `status_operacional`: VARCHAR(20) (NOT NULL) — Domínio: `'DISPONIVEL'`, `'EM_USO'`, `'MANUTENCAO'`.

### Tabela: `ordens_transporte`
- `id_ordem`: SERIAL (PK, NOT NULL) — Identificador único da ordem.
- `codigo_rastreio`: VARCHAR(30) (UNIQUE, NOT NULL) — Código alfanumérico padronizado.
- `origem`: VARCHAR(100) (NOT NULL) — Local de origem.
- `destino`: VARCHAR(100) (NOT NULL) — Local de destino.
- `peso_carga_kg`: NUMERIC(10,2) (NOT NULL) — Peso aferido da carga em kg (> 0).
- `status_ordem`: VARCHAR(20) (NOT NULL) — Domínio: `'PENDENTE'`, `'EM_TRANSITO'`, `'CONCLUIDA'`, `'CANCELADA'`.
- `data_criacao`: TIMESTAMP (NOT NULL) — Data e hora do registro.
- `id_veiculo`: INTEGER (FK `veiculos.id_veiculo`, NOT NULL) — Veículo alocado.
- `id_usuario`: INTEGER (FK `usuarios.id_usuario`, NOT NULL) — Usuário responsável.

## 3. Resumo dos Testes por Pares e Refatorações
1. **Rodrigo Pegoli (10/11/2026):** Padronização de código de rastreio com `.strip().upper()`.
2. **Sarah Bueno Pinheiro (11/11/2026):** Desabilitação do botão de envio quando não há veículos disponíveis.
3. **Guilherme (12/11/2026):** Validação estrita de peso positivo (`peso_carga_kg > 0`) no Model.
4. **Thalita Bonani (13/11/2026):** Limpeza automática do formulário (`form.reset()`) após cadastro.
5. **Kelmer (14/11/2026):** Destaque tipográfico em negrito (`<strong>`) na coluna de rastreamento.