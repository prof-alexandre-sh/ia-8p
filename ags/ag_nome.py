# -*- coding: utf-8 -*-
"""

@author: Alexandre

"""

import random
#import matplotlib.pyplot as pt
        
class Individuo():
    def __init__(self, geracao=0):
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []
        
        ## Inicializa indivíduos
        for i in range(len(target)):
            self.cromossomo.append(random.choice(chars))
            
    ## Avalia o fitness dos indivíduos
    def avaliacao(self):
        valor = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == target[i]:
                valor +=1
        self.nota_avaliacao = valor
        ## Restrições vão aqui no fitness??
    
    ## Recombinação
    ## Função de 1 indivíduo, por isso passamos outro como parâmetro
    def crossover(self, outro_individuo):
        # Random retorna aleatório entre 0 e 1
        ponto_corte = round(random.random() * len(self.cromossomo))
        
        ## Recombinação das partes dos genitores
        ## [o:ponto_corte] - Do início até o ponto de corte. Intervalo fechado no ponto de corte
        ## [ponto_corte::] - Do ponto de corte até o final. Intervalo aberto no ponto de corte
        filho1 = outro_individuo.cromossomo[0:ponto_corte] + self.cromossomo[ponto_corte::]
        filho2 = self.cromossomo[0:ponto_corte] + outro_individuo.cromossomo[ponto_corte::]
        
        ## Indivíduos da próxima gereção
        filhos = [Individuo(self.geracao + 1),
                  Individuo(self.geracao + 1)]
        
        ## Setando cromossomo dos novos indivíduos
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    
    def mutacao(self, taxa_mutacao):
        #print("Antes %s" % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random.random() < taxa_mutacao:
                self.cromossomo[i] = random.choice(chars)
        
        #print("Depois %s" % self.cromossomo)
        return self
                

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0 ## Vai armazenar a melhor solução de todas
        self.lista_solucoes = []
        
    def inicializaPopulacao(self):
        for i in range(self.tamanho_populacao):
            ## Insere os indivíduos na lista a medida que eles forem gerados
            ## Contrutor do Individuo inicializa ele aleatoriamente
            self.populacao.append(Individuo())
        
        ## Apenas inicializa
        self.melhor_solucao = self.populacao[0]
        self.melhor_pai = self.populacao[0]
    
    def ordenaPop(self):
        ## Função que ordena. Passa a lista, função para percorrer população e pegar note, e qual método de ordenação
        ## Usamos lambda (função que não precisa definir) para percorrer a população e pegar as notas e usar como key para a ordenação
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
    
    # OPCIONAL
    def elitismo(self, num):
        tamanho_individuo = len(self.populacao)
        for x in range(num):
            if self.populacao[0].geracao == 1:
                self.populacao[tamanho_individuo-(x+1)].cromossomo = self.melhor_solucao.cromossomo
                self.populacao[tamanho_individuo-(x+1)].nota_avaliacao = self.melhor_solucao.nota_avaliacao
            else:
                self.populacao[tamanho_individuo-(x+1)].cromossomo = self.melhor_pai.cromossomo
                self.populacao[tamanho_individuo-(x+1)].nota_avaliacao = self.melhor_pai.nota_avaliacao
    
    # Sempre mantém o melhor indivíduo nessa variável. Atualiza variável
    def melhorIndividuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
    
    ## Usado na roleta
    ## Fitness total da população
    def somaAvaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
    ## Simula roleta
    def selecionaPai(self, somaAvaliacoes):
        pai = -1
        valor_sorteado = random.random() * somaAvaliacoes
        soma = 0
        i = 0
        '''
        Iteramos sobre os indivíduos somando a variável "soma" seus valores de fitness.
        Aqueles com maior fitness possuem mais chances de parar o loop
        '''
        while i < len(self.populacao) and soma < valor_sorteado: # Se um é falso, encerra
            soma += self.populacao[i].nota_avaliacao # Incremente com fitness de cada indivíduo
            pai += 1 # Incremente para saber qual índice do pai
            i +=1
        return pai
    
    def visualizaGeracao(self):
        ## Melhor sempre vai estar nessa posição
        melhor = self.populacao[0]
        print("Geração: %s -> Valor: %s Cromossomo: %s" % (self.populacao[0].geracao,
                                                                     melhor.nota_avaliacao,                                                              
                                                                     ''.join(melhor.cromossomo)))
    # Executa AG
    def resolver(self, taxa_mutacao, numero_geracoes):
        self.inicializaPopulacao()
        
        for individuo in self.populacao:
            individuo.avaliacao()
            
        self.ordenaPop()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
        
        self.visualizaGeracao()
        
        while self.melhor_solucao.nota_avaliacao != len(target):
        #for geracao in range(numero_geracoes): #<- Critério de parada sendo o número de gerações
            soma_avaliacao = self.somaAvaliacoes()
            nova_pop = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.selecionaPai(soma_avaliacao)
                pai2 = self.selecionaPai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_pop.append(filhos[0].mutacao(taxa_mutacao))
                nova_pop.append(filhos[1].mutacao(taxa_mutacao))

            ## Substitui pela população nova  
            self.populacao = list(nova_pop)
            
            ## Calcula fitness dos novos indivíduos. Variável do objeto
            for individuo in self.populacao:
                individuo.avaliacao()
                
            ## Ordena pelo fitness. Maior para o menor
            self.ordenaPop()
            
            #Elitismo - Opcional
            #self.elitismo(2)
            
            # Melhor solução da geração atual que será usado no elitismo da geração seguinte
            #self.melhor_pai = self.populacao[0]
            
            self.visualizaGeracao()
            
            melhor_encontrada = self.populacao[0]
            self.lista_solucoes.append(melhor_encontrada.nota_avaliacao)
            '''#Verifica se a melhor solução da geração atual é melhor que a self.melhor_solucao.
               #O objetivo é manter sempre a melhor solução em self.melhor_solução para printá-la no final 
            '''
            self.melhorIndividuo(melhor_encontrada)

        print("Melhor solução -> Geração: %s Valor: %s Cromossomo: %s" % 
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.cromossomo))
        print(f"Nome final: {''.join(self.melhor_solucao.cromossomo)}")


if __name__ == '__main__':
    #random.seed(2)
    target = "nome sobrenome terceiro nome"
    chars = "abcdefghijklmnopqrstyvxzyw "
    taxa_mutacao = 0.01
    numero_geracoes = 100
    tamanho_populacao = 150
    ag = AlgoritmoGenetico(tamanho_populacao)
    
    ag.resolver(taxa_mutacao, numero_geracoes)
    