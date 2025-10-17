# Guia de Contribuição

Contribuições são muito bem-vindas! Este projeto é mantido pela comunidade e quanto mais pessoas contribuírem, melhor ele ficará. Siga os passos abaixo para contribuir:

## 1. Faça um Fork do Projeto

1. Acesse o repositório no GitHub: https://github.com/flaviofilipe/grupy_landingpage
2. Clique no botão **"Fork"** no canto superior direito da página
3. Aguarde o GitHub criar uma cópia do repositório na sua conta

## 2. Clone o Fork para sua Máquina

```bash
# Substitua SEU_USUARIO pelo seu nome de usuário do GitHub
git clone https://github.com/SEU_USUARIO/landingpage.git
cd landingpage
```

## 3. Configure o Repositório Original como Upstream

Isso permite que você mantenha seu fork atualizado com as mudanças do repositório original:

```bash
git remote add upstream https://github.com/flaviofilipe/grupy_landingpage.git
```

## 4. Crie uma Branch para sua Contribuição

**Nunca trabalhe diretamente na branch `main`!** Sempre crie uma nova branch:

```bash
# Use um nome descritivo para sua branch
git checkout -b minha-contribuicao

# Exemplos de nomes de branches:
# git checkout -b adiciona-secao-contato
# git checkout -b corrige-bug-template
# git checkout -b atualiza-documentacao
```

## 5. Faça suas Alterações

1. Abra o projeto no seu editor de código favorito
2. Faça as alterações necessárias
3. Teste suas alterações executando o projeto:
   ```bash
   uv run uvicorn src.app:app --reload
   ```
4. Acesse http://localhost:8000 e verifique se está tudo funcionando

## 6. Commit das Alterações

```bash
# Adicione os arquivos modificados
git add .

# Faça o commit com uma mensagem clara e descritiva
git commit -m "Descrição clara do que foi alterado"

# Exemplos de mensagens de commit:
# git commit -m "Adiciona seção de contato no README"
# git commit -m "Corrige bug no template de GitHub"
# git commit -m "Atualiza instruções de instalação"
```

## 7. Envie suas Alterações para o GitHub

```bash
# Envie sua branch para o seu fork no GitHub
git push origin minha-contribuicao
```

## 8. Abra um Pull Request (PR)

1. Acesse seu fork no GitHub (https://github.com/SEU_USUARIO/landingpage)
2. Você verá uma mensagem sugerindo criar um Pull Request. Clique em **"Compare & pull request"**
3. Preencha o título do PR de forma clara e objetiva
4. Na descrição do PR, inclua:
   - **O que foi alterado**: Descreva claramente as mudanças realizadas
   - **Por que foi alterado**: Explique a motivação da mudança
   - **Como testar**: Instruções para testar as alterações
   - **Screenshots/Evidências**: Adicione imagens, GIFs ou vídeos mostrando as alterações (especialmente para mudanças visuais)
   - **Issues relacionadas**: Se sua contribuição resolve alguma issue, mencione com `Closes #NUMERO_DA_ISSUE`

5. Clique em **"Create pull request"**

## 9. Processo de Aprovação

Após enviar seu Pull Request:

1. **Revisão Automática**: O GitHub Actions executará testes automatizados (se configurados)

2. **Revisão por Mantenedores**: Um ou mais mantenedores do projeto irão:
   - Revisar seu código
   - Testar as alterações
   - Verificar se segue os padrões do projeto
   - Solicitar mudanças se necessário

3. **Feedback e Ajustes**: Se forem solicitadas alterações:
   - Faça as mudanças no seu código local
   - Faça commit e push na mesma branch:
     ```bash
     git add .
     git commit -m "Aplica sugestões da revisão"
     git push origin minha-contribuicao
     ```
   - O PR será atualizado automaticamente

4. **Aprovação e Merge**: 
   - Após aprovação de pelo menos um mantenedor, seu PR será mesclado ao projeto
   - Você receberá uma notificação
   - Parabéns! 🎉 Você é oficialmente um contribuidor do projeto

## Exemplo: Contribuindo com Alteração no README.md

Vamos supor que você quer adicionar uma nova seção de "Perguntas Frequentes (FAQ)" no README:

### Passo 1: Fork e Clone
```bash
# Faça o fork pelo GitHub (botão Fork)
git clone https://github.com/SEU_USUARIO/landingpage.git
cd landingpage
git remote add upstream https://github.com/flaviofilipe/grupy_landingpage.git
```

### Passo 2: Crie a Branch
```bash
git checkout -b adiciona-secao-faq
```

### Passo 3: Edite o README.md
Abra o arquivo `README.md` no seu editor e adicione a nova seção:

```markdown
## Perguntas Frequentes (FAQ)

### Qual a versão mínima do Python?
Python 3.12 ou superior.

### Posso usar outro gerenciador de pacotes?
Sim, mas recomendamos o UV pela velocidade e eficiência.
```

### Passo 4: Salve e Faça Commit
```bash
git add README.md
git commit -m "Adiciona seção de Perguntas Frequentes ao README"
```

### Passo 5: Envie para o GitHub
```bash
git push origin adiciona-secao-faq
```

### Passo 6: Crie o Pull Request

Vá até https://github.com/SEU_USUARIO/landingpage e clique em "Compare & pull request"

**Exemplo de descrição do PR:**

```
## 📝 Adiciona Seção de Perguntas Frequentes

### O que foi alterado
- Adicionada nova seção "Perguntas Frequentes (FAQ)" no README.md
- Incluídas 2 perguntas iniciais sobre versão do Python e gerenciador de pacotes

### Por que foi alterado
Percebi que algumas dúvidas são comuns entre iniciantes. Uma seção de FAQ ajudará novos 
contribuidores a encontrar respostas rapidamente sem precisar abrir issues.

### Como testar
1. Visualize o arquivo README.md renderizado no GitHub
2. Verifique se a formatação está correta
3. Confirme se as informações estão claras e corretas

### Screenshots

**Antes:**
[Imagem do README sem a seção FAQ]

**Depois:**
[Imagem do README com a nova seção FAQ]

### Checklist
- [x] Verifiquei a ortografia
- [x] Testei os links (se houver)
- [x] A formatação Markdown está correta
- [x] As informações são precisas e atualizadas
```

### Passo 7: Aguarde a Revisão

Os mantenedores irão revisar e podem:
- ✅ **Aprovar** imediatamente se está tudo certo
- 💬 **Comentar** com sugestões de melhoria
- 🔄 **Solicitar mudanças** específicas

**Exemplo de feedback:**
> "Ótima contribuição! Poderia adicionar mais uma pergunta sobre como reportar bugs?"

Você então faria a alteração e:
```bash
# Edite o README.md novamente
git add README.md
git commit -m "Adiciona pergunta sobre como reportar bugs"
git push origin adiciona-secao-faq
# O PR é atualizado automaticamente!
```

## Dicas para um Bom Pull Request

✅ **Faça:**
- Use títulos e descrições claros
- Inclua screenshots/GIFs para mudanças visuais
- Teste suas alterações antes de enviar
- Mantenha o PR focado em uma única funcionalidade/correção
- Responda aos comentários de forma educada e construtiva
- Forneça contexto e motivação para suas mudanças

❌ **Evite:**
- PRs muito grandes com muitas alterações não relacionadas
- Commits sem mensagens claras
- Ignorar o feedback dos revisores
- Fazer alterações diretamente na branch main
- Enviar código sem testar

## Mantendo seu Fork Atualizado

Periodicamente, sincronize seu fork com o repositório original:

```bash
# Busque as últimas alterações do repositório original
git fetch upstream

# Volte para a branch main
git checkout main

# Mescle as alterações
git merge upstream/main

# Envie para seu fork
git push origin main
```

---

**Obrigado por contribuir com a GruPy-VCA! 🐍💚**

Se tiver dúvidas, abra uma [issue](https://github.com/flaviofilipe/grupy_landingpage/issues) ou entre em contato com a comunidade.

