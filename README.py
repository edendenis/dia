#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `dia` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `dia` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `dia` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `dia`
# 
# O Dia é um software de código aberto de gerenciamento de calendário e agenda que oferece uma maneira eficaz de organizar compromissos, eventos, tarefas e lembretes em sistemas operacionais Unix-like, incluindo Linux. Com uma interface de usuário simples e intuitiva, o Dia permite que os usuários criem e visualizem calendários personalizados, adicionem eventos recorrentes ou únicos, definam prioridades e categorias para tarefas e mantenham um controle organizado de suas atividades diárias. Além disso, o Dia suporta a exportação de calendários em diversos formatos, facilitando a sincronização com outras ferramentas de gerenciamento de tempo e dispositivos. É uma escolha popular para quem busca uma solução leve e funcional de calendário para suas necessidades pessoais ou de trabalho.

# ## 1. Como configurar/instalar o `dia` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar o `dia` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 1. **Instale o DIA:** Uma vez que os pacotes estejam atualizados, você pode instalar o DIA usando o gerenciador de pacotes apt. No terminal, digite: `sudo apt install dia -y`
# 
# 2. ***Confirmação e Uso:** Após a conclusão da instalação, você pode iniciar o DIA através do terminal com o comando `dia` ou encontrá-lo no menu de aplicações do seu Ubuntu.
# 
# Lembre-se de que, dependendo da sua versão do Ubuntu e das configurações do sistema, esses passos podem variar um pouco. Se você encontrar problemas durante a instalação, verifique se o DIA é compatível com a sua versão do Ubuntu.

# ### 1.1 Código completo para configurar/instalar
# 
# Para configurar/instalar o `dia` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update -y
#     sudo apt autoremove -y
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install dia -y
#     dia
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instale o programa dia no ubuntu:*** https://chat.openai.com/c/d9a2f2cc-d4a0-47cd-97d8-c7bf452a833c (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.
# 
# [3] OPENAI. ***Comandos de manutenção do ubuntu:*** https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830. ChatGPT. Acessado em: 29/12/2023 10:01.
