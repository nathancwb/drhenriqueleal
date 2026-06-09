# Resumo da Conversa e Evolução da Landing Page VIP

Este documento serve como o registro consolidado de todas as interações, solicitações do usuário e implementações técnicas realizadas para a **Landing Page de Mentorias VIP do Dr. Henrique Leal** (`cursos-vip.html`), localizada na pasta do projeto `dr-henrique-leal`.

---

## 📅 Histórico de Solicitações e Soluções (Ordem Cronológica)

1. **Substituição de Imagens e Ajuste de Travamentos**:
   * *Solicitação*: Substituir por fotos novas e garantir que todas apareçam corretamente, resolvendo o travamento no final da seção.
   * *Solução*: Atualizamos as fotos de destaque de alta qualidade e removemos a altura fixa de `380vh` que gerava o vácuo preto no fim da seção, permitindo o destravamento suave da coluna assim que o último card é lido.

2. **Fade-out Cinemático entre Seções**:
   * *Solicitação*: Adicionar um efeito de fade-out suave para conectar e fundir uma seção com a outra de forma contínua.
   * *Solução*: Desenvolvemos equações de opacidade baseadas na colisão física das seções com o visor (`getBoundingClientRect`). As seções agora esmaecem gradualmente até `opacity: 0` antes de desatarraxar do topo da tela, fundindo-se de forma elegante e cinematográfica.

3. **Responsividade Mobile Completa**:
   * *Solicitação*: O layout mobile estava estranho e não responsivo.
   * *Solução*: Redesenhamos a folha de estilos mobile:
     * O fundo do Hero com a foto do Dr. Henrique foi fixado estaticamente em `position: fixed` com `opacity: 0.32`, evitando que a imagem se distorça.
     * Os textos subsequentes deslizam sobre a foto com fundos pretos sólidos luxuosos, garantindo legibilidade e alto contraste.

4. **Eliminação de CTAs Repetitivos no Mobile**:
   * *Solicitação*: O botão "Garantir Minha Vaga" aparecendo em cada card individual ficava muito repetitivo em celulares.
   * *Solução*: Ocultamos os botões individuais nos 4 cards de mentorias no mobile e adicionamos um **único botão centralizado de destaque no final do bloco** ("Quero me Candidatar a uma Vaga"), mantendo o design limpo e focado.

5. **Ajuste de Excesso de Informações no Mobile (Aba Horizontal)**:
   * *Solicitação*: A quantidade de texto acumulada nos 4 cards de mentorias gerava uma leitura cansativa em celulares (uma muralha de texto).
   * *Solução*: Criamos um **Seletor de Abas Horizontal Interativo** (`mentorias-mobile-tabs`). O usuário agora alterna dinamicamente entre as abas com toques suaves e visualiza apenas o card selecionado, mantendo 100% da informação de forma compacta e organizada.

6. **Fotos Cortadas no Mobile (Bug de Crop)**:
   * *Solicitação*: As fotos das mentorias estavam cortadas e sem enquadramento ideal.
   * *Solução*: Aumentamos a altura do contêiner da foto para `250px` e aplicamos a regra `object-position: top center !important;`. Isso forçou o alinhamento da imagem pelo topo, exibindo o rosto e os ombros do Dr. Henrique de forma impecável.

7. **Correção do Vazamento de Conteúdo no FAQ**:
   * *Solicitação*: O texto das respostas do FAQ estava vazando no rodapé mesmo quando os accordions estavam recolhidos.
   * *Solução*: Removemos o preenchimento inline de `.faq-answer` no HTML e o inserimos exclusivamente na classe interna `.faq-answer-inner`. O acordeão agora recolhe-se a exatamente `0px` de altura física, eliminando qualquer vazamento visual.

8. **Persistência da Foto no Desktop (Sem Fade-Out Precoce)**:
   * *Solicitação*: A foto de destaque na coluna esquerda começava a apagar e ficar muito escura antes que o usuário terminasse de passar totalmente para o próximo card ou seção.
   * *Solução*: Substituímos o espaçador final da seção de mentorias por uma classe responsiva `.mentorias-bottom-spacer` de `40vh` em desktop, permitindo que a seção permaneça perfeitamente presa no topo enquanto o card 4 é lido. Ajustamos a fórmula de fade-out do script (`exitProgress`) para dividir a base da seção por `(viewportHeight * 0.45)` em vez de `viewportHeight`. A foto agora permanece 100% nítida e totalmente opaca até que a seção de fato saia da tela.

9. **Fim do Esmaecimento Precoce de Todo o Site (Hero, Público, Metodologia e Candidatura)**:
   * *Solicitação*: O contêiner de várias seções (incluindo o segundo card do Hero e o formulário de Candidatura) estava sumindo antes mesmo de aparecer 100% visível na tela.
   * *Solução*: Substituímos a fórmula antiga de saída em todas as seções de scrollytelling (`#block-hero`, `#block-publico`, `#b4` e `#block-candidatura`) por `rect.bottom / (viewportHeight * 0.8)`. Agora, todos os blocos mantêm **100% de opacidade, legibilidade e nitidez absoluta** durante toda a sua fase ativa e interativa, iniciando o fade-out com suavidade apenas quando a seção é desfixada e começa a subir.

---

## 🛠️ Detalhes das Implementações Técnicas

*   **Arquitetura Unificada**: CSS específico e isolado no arquivo [`assets/css/cursos-vip.css`](file:///assets/css/cursos-vip.css) e lógica dinâmica no script [`assets/js/cursos-vip.js`](file:///assets/js/cursos-vip.js).
*   **Performance Gráfica**: Uso de `will-change: opacity;` para forçar a renderização das transições diretamente na GPU, garantindo estabilidade e fluidez a 60 FPS.
*   **Conversão Focada**: Eliminação de menus superiores ou laterais flutuantes redundantes, atuando como uma landing page de alta conversão.

*Documentação consolidada para futuras atualizações e reconstruções da Landing Page do Dr. Henrique Leal.*
