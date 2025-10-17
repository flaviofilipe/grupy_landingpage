# Dados da Comunidade

Este diretório contém os dados em JSON dos membros da comunidade GruPy VCA.

## Estrutura do arquivo `participantes.json`

Cada membro da comunidade deve ter os seguintes campos:

```json
{
  "id": 1,                    // ID único do membro (número inteiro)
  "nome": "Nome Completo",    // Nome completo do membro
  "cargo": "Cargo/Função",    // Cargo ou função na comunidade
  "github": "username",       // Username do GitHub (sem @)
  "linkedin": "username",     // Username do LinkedIn
  "instagram": "username",    // Username do Instagram (sem @)
  "foto": "nome-arquivo.jpg", // Nome do arquivo da foto em src/static/images/members/
  "bio": "Breve descrição"    // Biografia curta do membro
}
```

## Como adicionar um novo membro

1. **Adicione a foto do membro:**
   - Coloque a foto no diretório: `src/static/images/members/`
   - Use um nome descritivo: `nome-sobrenome.jpg`
   - Tamanho recomendado: 300x300px (quadrado)
   - Formato: JPG, PNG ou SVG

2. **Adicione os dados no JSON:**
   ```json
   {
     "id": 7,
     "nome": "Seu Nome",
     "cargo": "Desenvolvedor Python",
     "github": "seu-usuario",
     "linkedin": "seu-usuario-linkedin",
     "instagram": "seu.usuario",
     "foto": "seu-nome.jpg",
     "bio": "Sua biografia"
   }
   ```

3. **Campos opcionais:**
   - Todos os campos de redes sociais (github, linkedin, instagram) são opcionais
   - O campo `bio` também é opcional
   - Se não tiver foto própria, use `"foto": "placeholder.jpg"`

## Notas importantes

- Mantenha os IDs únicos e em ordem crescente
- O arquivo deve ser um JSON válido (use um validador se necessário)
- Certifique-se de que as imagens referenciadas existam no diretório correto
- Use encoding UTF-8 para suportar caracteres especiais

