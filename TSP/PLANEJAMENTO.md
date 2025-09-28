# Algoritmos Genéticos em C++ para o Problema do Caixeiro Viajante

Este repositório implementa **Algoritmos Genéticos (AG)** em **C++** para resolver o **Problema do Caixeiro Viajante (TSP)**, com foco em otimizar rotas de entrega para lojas virtuais.  
A abordagem segue o **TDD (Test-Driven Development)** para garantir que cada componente seja testado antes de ser implementado.

---

## Funcionalidades

- [ ] Representação de cidades e distâncias
- [ ] Criação de população inicial
- [ ] Seleção de indivíduos
- [ ] Operadores genéticos: crossover e mutação
- [ ] Avaliação de fitness (distância total da rota)
- [ ] Evolução da população ao longo de gerações
- [ ] Exportação da rota otimizada

---

## Estrutura do Projeto

- **src/**  
  - `main.cpp` – Entrada do programa  
  - `city.h/cpp` – Estrutura de cidade e cálculo de distância  
  - `population.h/cpp` – Estrutura da população e manipulação  
  - `genetic.h/cpp` – Operadores genéticos e evolução  

- **tests/**  
  - `test_city.cpp` – Testes unitários para cidade e distâncias  
  - `test_population.cpp` – Testes para população  
  - `test_genetic.cpp` – Testes de crossover, mutação e fitness  

---

## Passos de Desenvolvimento (TDD)

- [ ] **Teste: Representação da Cidade**  
  - Criar cidades com coordenadas X e Y  
  - Calcular distância entre duas cidades corretamente  

- [ ] **Implementação: Cidade**  
  - Struct/class `City` com atributos X e Y  
  - Função `distanceTo(const City &other)`  

- [ ] **Teste: População Inicial**  
  - Garantir que a população seja gerada com indivíduos válidos  
  - Cada indivíduo deve conter todas as cidades sem repetição  

- [ ] **Implementação: População Inicial**  
  - Criar vetor de rotas aleatórias  
  - População de tamanho definido  

- [ ] **Teste: Função de Fitness**  
  - Avaliar se a distância total da rota é calculada corretamente  

- [ ] **Implementação: Fitness**  
  - Somar distâncias entre todas as cidades na rota  
  - Armazenar valor do fitness em cada indivíduo  

- [ ] **Teste: Seleção de Pais**  
  - Verificar se indivíduos com melhor fitness têm maior chance de serem selecionados  

- [ ] **Implementação: Seleção**  
  - Métodos: roleta, torneio ou ranking  
  - Retornar pares de pais para crossover  

- [ ] **Teste: Crossover**  
  - Garantir que filhos herdam corretamente partes dos pais  
  - Não repetir cidades  

- [ ] **Implementação: Crossover**  
  - Order Crossover (OX) ou similar  
  - Criar novos indivíduos combinando genes dos pais  

- [ ] **Teste: Mutação**  
  - Verificar se a mutação troca posições de cidades corretamente  
  - Não gerar rotas inválidas  

- [ ] **Implementação: Mutação**  
  - Troca aleatória de duas cidades  
  - Probabilidade de mutação configurável  

- [ ] **Teste: Evolução da População**  
  - Garantir que fitness médio melhore ao longo das gerações  
  - Verificar substituição de indivíduos corretamente  

- [ ] **Implementação: Loop de Evolução**  
  - Seleção → Crossover → Mutação → Substituição  
  - Atualizar população por número definido de gerações  

- [ ] **Teste: Exportação da Rota Otimizada**  
  - Rota final completa e válida  
  - Distância total coerente com cálculo de fitness  

- [ ] **Implementação: Exportação de Rota**  
  - Imprimir rota no terminal ou salvar em arquivo `.txt` ou `.csv`  

---

# Como Testar e Executar

## Executar e Testar em Diferentes Compiladores

### GCC / G++ (Linux, macOS)

```bash
g++ -std=c++17 src/*.cpp -o tsp
./tsp
```

### Clang++ (Linux, macOS)

```bash
clang++ -std=c++17 src/*.cpp -o tsp
./tsp
```

### MSVC / Visual Studio (Windows)

```powershell
# Abrir Developer Command Prompt
cl /EHsc /std:c++17 src\*.cpp /Fe:tsp.exe
tsp.exe
```

### MinGW (Windows)

```bash
g++ -std=c++17 src/*.cpp -o tsp.exe
./tsp.exe
```

### Usando CMake (multi-plataforma)

```bash
mkdir build
cd build
cmake ..
cmake --build .
./tsp    # ou tsp.exe no Windows
```

## Testar

Para compilar e executar os testes unitários:

### GCC / Clang++

```bash
g++ -std=c++17 tests/*.cpp src/*.cpp -o tests
./tests
```

### MSVC / MinGW

```powershell
cl /EHsc /std:c++17 tests\*.cpp src\*.cpp /Fe:tests.exe
tests.exe
```

```
g++ -std=c++17 tests/*.cpp src/*.cpp -o tests && ./tests
OU
clang++ -std=c++17 src/*.cpp -o tsp
```
