# Como configurar/instalar/usar o `dia` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `dia` no `Linux Ubuntu`.

## _Abstract_

_In this document are contained the main commands and settings to set up/install/use the `dia` on `Linux Ubuntu`._

## Descrição [2]

### `dia`

O `Dia` é um _software_ de código aberto de gerenciamento de calendário e agenda que oferece uma maneira eficaz de organizar compromissos, eventos, tarefas e lembretes em sistemas operacionais `Unix-like`, incluindo `Linux`. Com uma interface de usuário simples e intuitiva, o Dia permite que os usuários criem e visualizem calendários personalizados, adicionem eventos recorrentes ou únicos, definam prioridades e categorias para tarefas e mantenham um controle organizado de suas atividades diárias. Além disso, o Dia suporta a exportação de calendários em diversos formatos, facilitando a sincronização com outras ferramentas de gerenciamento de tempo e dispositivos. É uma escolha popular para quem busca uma solução leve e funcional de calendário para suas necessidades pessoais ou de trabalho.

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
    
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    
    ```bash
    sudo apt clean
    ``` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
    
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    
    ```bash
    sudo apt full-upgrade -y
    ```

1. **Instale o `DIA`:** Uma vez que os pacotes estejam atualizados, você pode instalar o `DIA` usando o gerenciador de pacotes apt. No terminal, digite: `sudo apt install dia -y`

2. **Confirmação e Uso:** Após a conclusão da instalação, você pode iniciar o `DIA` através do terminal com o comando `dia` ou encontrá-lo no menu de aplicações do seu `Linux Ubuntu`.

Lembre-se de que, dependendo da sua versão do `Linux Ubuntu` e das configurações do sistema, esses passos podem variar um pouco. Se você encontrar problemas durante a instalação, verifique se o `DIA` é compatível com a sua versão do `Linux Ubuntu`.


### 1.1 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `dia` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo apt install dia -y
    dia
    ```



## 2. Código Red, Green e Blue (RGB) das cores

Segue as 10 cores mais claras com seus códigos RGB, ideais para uso em gráficos BPMN, para que o diagrama não fique muito escuro:

| Cor                | Red | Green | Blue |
|--------------------|-----|-------|------|
| **Azul Claro**     | 173 | 216   | 230  |
| **Verde Claro**    | 144 | 238   | 144  |
| **Rosa Claro**     | 255 | 182   | 193  |
| **Amarelo Claro**  | 255 | 255   | 224  |
| **Laranja Claro**  | 255 | 228   | 181  |
| **Lavanda (Roxo Claro)** | 230 | 230 | 250  |
| **Ciano Claro**    | 224 | 255   | 255  |
| **Verde Menta**    | 189 | 252   | 201  |
| **Pêssego**        | 255 | 218   | 185  |
| **Coral Claro**    | 240 | 128   | 128  |

Essas cores são mais suaves e garantirão que seu gráfico tenha uma aparência leve e agradável, evitando que fique muito escuro ou pesado.


## Referências

[1] OPENAI. ***Instale o programa dia no ubuntu.*** Disponível em: <https://chat.openai.com/c/d9a2f2cc-d4a0-47cd-97d8-c7bf452a833c> (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.

[3] OPENAI. ***Comandos de manutenção do ubuntu.*** Disponível em: <https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830> (texto adaptado). ChatGPT. Acessado em: 29/12/2023 10:01.

