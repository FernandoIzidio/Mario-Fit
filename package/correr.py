def correrFrente(maoDireita_x,cotoveloDireito_x,dist_maoDireita_cintura):
    if maoDireita_x < cotoveloDireito_x and dist_maoDireita_cintura > 110:
        print("Correndo Frente")

def correrTras(maoEsquerda_x,cotoveloEsquerdo_x,dist_maoEsquerda_cintura):
    if maoEsquerda_x > cotoveloEsquerdo_x and dist_maoEsquerda_cintura > 110:
        print("Correndo Tras")