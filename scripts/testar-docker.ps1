$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Confirmar-Saida {
    param([string]$Saida, [string]$Trecho)
    if (-not $Saida.Contains($Trecho)) {
        throw "O teste não encontrou na saída: $Trecho`n$Saida"
    }
}

$pastaProjeto = Split-Path -Parent $PSScriptRoot
$projetoAnterior = [Environment]::GetEnvironmentVariable('COMPOSE_PROJECT_NAME')
$volumeAnterior = [Environment]::GetEnvironmentVariable('TASKTRACKER_VOLUME_NAME')
$env:COMPOSE_PROJECT_NAME = "tasktracker-smoke-$PID"
$env:TASKTRACKER_VOLUME_NAME = "tasktracker-smoke-data-$PID"

Push-Location $pastaProjeto
try {
    docker info --format '{{.ServerVersion}}' | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'Docker Desktop não está pronto.' }

    docker compose config --quiet
    if ($LASTEXITCODE -ne 0) { throw 'Configuração do Compose inválida.' }

    docker build -t tasktracker-app .
    if ($LASTEXITCODE -ne 0) { throw 'Build da imagem falhou.' }

    $saidaDocker = @(
        '1', '', 'Teste Docker', 'Descricao', 'Urgente', 'Alta',
        '31/10/2026', '2', '3'
    ) | docker run -i --rm tasktracker-app | Out-String
    if ($LASTEXITCODE -ne 0) { throw 'Execução direta falhou.' }
    Confirmar-Saida $saidaDocker 'O título é obrigatório'
    Confirmar-Saida $saidaDocker 'Prioridade inválida'
    Confirmar-Saida $saidaDocker 'Título: Teste Docker'
    Confirmar-Saida $saidaDocker 'Status: Pendente'

    $saidaCadastro = @(
        '1', 'Teste Compose Persistente', 'Descricao', 'Baixa',
        '01/11/2026', '3'
    ) | docker compose run --rm -T tasktracker | Out-String
    if ($LASTEXITCODE -ne 0) { throw 'Cadastro pelo Compose falhou.' }
    Confirmar-Saida $saidaCadastro 'Tarefa cadastrada com sucesso!'

    $saidaReabertura = @('2', '3') | docker compose run --rm -T tasktracker | Out-String
    if ($LASTEXITCODE -ne 0) { throw 'Reabertura pelo Compose falhou.' }
    Confirmar-Saida $saidaReabertura 'Título: Teste Compose Persistente'
    Confirmar-Saida $saidaReabertura 'Status: Pendente'

    $saidaDiretaPersistente = @('2', '3') |
        docker run -i --rm -v "$($env:TASKTRACKER_VOLUME_NAME):/app/data" tasktracker-app |
        Out-String
    if ($LASTEXITCODE -ne 0) { throw 'Leitura do volume pela execução direta falhou.' }
    Confirmar-Saida $saidaDiretaPersistente 'Título: Teste Compose Persistente'

    Write-Host 'OK: build, validações, cadastro, listagem e persistência no Compose e Docker direto.'
}
finally {
    docker compose down --volumes --remove-orphans | Out-Null
    Pop-Location
    if ($null -eq $projetoAnterior) { Remove-Item Env:COMPOSE_PROJECT_NAME -ErrorAction SilentlyContinue }
    else { $env:COMPOSE_PROJECT_NAME = $projetoAnterior }
    if ($null -eq $volumeAnterior) { Remove-Item Env:TASKTRACKER_VOLUME_NAME -ErrorAction SilentlyContinue }
    else { $env:TASKTRACKER_VOLUME_NAME = $volumeAnterior }
}
