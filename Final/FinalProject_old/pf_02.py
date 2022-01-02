# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:59:08 2020

@author: Carlos Cano
@title: K-Means
@description: Where {𝑥⃗1, 𝑥⃗2, 𝑥⃗3, … , 𝑥⃗𝑁 } is a collection of documents/users without any label, where each
user is represented as a normalized vector 𝑥⃗𝑖 using tf-idf, N is the number of
document/users, and K is the desired number of clusters. The stopping criterion is when the
centroids does not change between iterations, or when a maximum number of iterations
has been reached (defined the maximum number of iterations as 50). k controls for the
cluster during iterations. 𝜇⃗𝑘 is the k centroid. There should be K centroids that indicate the
center of each cluster.

"""

from nltk.corpus import stopwords
import re
import math
import numpy as np
import matplotlib.pyplot as plt
 
def make_pd_voc(path_users,path_posts):
    s_w = stopwords.words('spanish')
    s_w.extend(['jajaja','jaja', 'jajajaja', 'Jajajaja','ajajja', 'this', 'and' 'the'])
    
    s_w = set(s_w)
    
    p_d = {}
    voc = []
    
    with open(path_users, encoding='UTF8') as users, \
         open(path_posts, encoding='UTF8') as posts:
             for p, u in zip(posts,users):
                 p = p.strip()
                 u = u.strip()
                 words = clean_text(p, s_w)
                 if u not in p_d:
                     p_d[u] = []
                 p_d[u].extend(words)
                 voc.extend(words)
    return p_d,voc

def clean_text(s, s_w):
    s = s.lower()
    words = re.findall('[a-záéíóúüñ]+', s)
    new_s = [w for w in words if ((not w in s_w) and len(w)>=3 and len(w)<=25)]
    return new_s

def tf_idf(p_d, voc):
    voc = set(voc)
    voc = list(voc)

    
    tdm = []
    for u in p_d:
        text = p_d[u]
        vector = []
        for word in voc:
                vector.append(text.count(word))
        tdm.append(vector)
    print(tdm)
    df = [0] * len(voc)
    for row in tdm:
        for i, column in enumerate(row):
            if column != 0:
                df[i] += 1
    nd = 1 + len(tdm)
    idf = []
    for val in df:
        idf.append(math.log(nd/(1+val)) + 1)
    
    tdm_tfidf = []
    for row in tdm:
        vector = []
        for i,column in enumerate(row):
            vector.append(column * idf[i])
        tdm_tfidf.append(vector)
        
    n_euc = normalizerVector(tdm_tfidf)
    
        
    return tdm_tfidf, n_euc

def normalizerVector(tdm_tfidf):
    n_euc = []
    for ren in tdm_tfidf:    
        norm = (sum([i**2 for i in ren])) ** (1/2)
        vec = [i/norm for i in ren]
        n_euc.append(vec)
    return n_euc
        
def di_euc(x,y):
    x = np.array(x)
    y = np.array(y)
    return np.sqrt(np.sum((x - y) ** 2)) 

#%%


# -----------------------------------------------------------
# -------------------- K MEANS ------------------------------
# -----------------------------------------------------------
def euclidian_dist(a, b):
    '''
        euclidian distance between two np.arrays
    '''
    return np.linalg.norm(a - b)

class KMeans:
    """KMeans implementation from scratch"""
    def __init__(self, K, iter_max=50, randomseeds=True, distance_metric=lambda a,b: np.linalg.norm(a-b)):
        self.K = K
        self.iter_max = iter_max
        self.randomseeds = randomseeds
        self.distances = None
        self.centroids = None
        self.clusters = None
        self.iteration = 0
        self.distances_sum = 1e9
        self.distance_metric = distance_metric
        
    def make_kmeans(self, data):
        '''
            make_kmeans(data) recibe como  entrada un arreglo numpy
            
            data(np.array) ->  Es un arreglo de puntos donde cada parte corresponde
            a un conjunto de puntos
            return status (bool)
        lambda: es una funcion cualquiera en este caso se regresa la distancia del centroide al punto
        '''
        N = len(data)
        if self.randomseeds:
            self.centroids = np.array([data[np.random.choice(N)] for i in range(self.K)])
        else:
            self.centroids = data[:self.K]
        # Crea una matriz del tamaño NUMBER_OF_CLUSTERS x NUMBER_OF_SAMPLES
        self.distances = np.zeros((self.K, N))
        
        # Crea un arreglo con  tamñaño de NUMBER_OF_SAMPLES 
        self.clusters = np.zeros(N)
        # inizializa las variables de paro 
        self.iteration = 0
        self.distances_sum = 1e9 #Error para que entre la primer vez 

        while self.iteration < self.iter_max:
            # Calculando las distancias entre los centroides y cada punto
            for k in range(self.K):
                # define la funcion que sera aplicada mientras 
                # los datos cambien en cada iteracion
                # el centroide sera la media de cada punto
                f = lambda x: self.distance_metric(x, self.centroids[k])
               #Aplica la función en cada punto de la data
                self.distances[k] = np.array(list(map(f, data)))
            # Si las nuevas distancias son iguales a las anteriores entonces sale del ciclo
            if self.distances_sum == self.distances.sum():
                break
            # Se guarda la nueva suma de distancias 
            self.distances_sum = self.distances.sum()    
            # Asigna a cada punto el cluster más cercano
            self.clusters = self.distances.T.argmin(axis=1)
            # Se recalculan los centroides
            for k in range(self.K):
                # Recalculan los centroides con la media de cada cluster
                self.centroids[k] = data[self.clusters == k].mean(axis=0)
            self.iteration += 1
            # A veces un error ocurre (no es error solamente los centroides asignados estan vacios
            # porque la matriz tiene demasiados ceros) aqui te lo puede decir.
            if self.distances_sum == np.nan:
                return False
        return True

W_D = 'D:/Mineria de Datos/data/'
path_users = W_D + 'users.txt'
path_posts = W_D + 'posts.txt'

p_d, voc = make_pd_voc(path_users, path_posts)


tf_idf, n_euc= tf_idf(p_d,voc)
tf_idf = np.array(tf_idf)
kmeans = KMeans(3, iter_max=50)
kmeans.make_kmeans(tf_idf)

print(kmeans.centroids)
print(kmeans.iteration)
print(kmeans.clusters)

"""
X =     np.array([[1, 2],
                  [1.5, 1.8],
                  [3, 8 ],
                  [8, 8],
                  [1, 0.6],
                  [9,11],
                  [1,9],
                  [12,18],
                 ])
kmeans = KMeans(3, iter_max=50)
kmeans.make_kmeans(X)
plt.scatter(X[:,0], X[:,1], s=150)
for point in kmeans.centroids:
    plt.scatter(point[0], point[1], marker='+')
plt.show()

"""

