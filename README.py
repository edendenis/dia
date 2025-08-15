#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `mermaid` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `mermaid` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/use the `mermaid` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `mermaid`
# 
# O `mermaid` é uma ferramenta de criação de diagramas e gráficos a partir de texto simples. Integrado com diversas plataformas e editores, como o Visual Studio Code e o GitHub, ele permite gerar visualizações como diagramas de fluxo, gráficos de Gantt e diagramas de sequência usando uma linguagem de marcação fácil de aprender. O `mermaid` é especialmente útil para desenvolvedores e analistas que desejam incluir diagramas e documentação técnica de forma eficiente e programática em suas documentações e projetos de código. Ele proporciona uma maneira ágil de criar representações visuais complexas sem a necessidade de _software_ gráfico avançado.
# 

# ## 1. Como configurar/instalar/usar o `dia` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `mermaid` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para instalar o `mermaid` no `Linux Ubuntu` pelo `Terminal Emulator`, você pode seguir estas etapas:
# 
# 1. **Instalar o `Node.js` e o `npm`**: O `mermaid` é uma ferramenta baseada em `JavaScript`, e é instalado via `npm`, que faz parte do `Node.js`. Primeiramente, atualize a lista de pacotes e instale o `Node.js` e o `npm`: `sudo apt install nodejs npm`
# 
# 2. **Instalar o `mermaid`**: Agora, com o `npm` instalado, você pode instalar o `mermaid-cli` (a ferramenta de linha de comando do mermaid) utilizando o seguinte comando: `sudo npm install -g @mermaid-js/mermaid-cli`
# 
#     O argumento `-g` significa que ele será instalado globalmente, para que você possa usar o `mermaid` em qualquer lugar do sistema.
# 
# 3. Verificar a instalação: Após a instalação, você pode verificar se o `mermaid-cli` foi instalado corretamente executando: `mmdc -h`
# 
#     Isso deve exibir a ajuda da ferramenta `mermaid-cli`, confirmando que a instalação foi bem-sucedida.
# 
# Agora você está pronto para gerar diagramas usando o `mermaid` via linha de comando no seu sistema `Linux Ubuntu`.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `dia` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install nodejs npm
#     sudo npm install -g @mermaid-js/mermaid-cli
#     mmdc -h
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instale o programa dia no ubuntu.*** Disponível em: <https://chatgpt.com/c/66e36f58-9048-8002-bd67-d2e746e319b6> (texto adaptado). ChatGPT. Acessado em: 12/09/2024 22:22.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 12/09/2024 22:22.
# 
