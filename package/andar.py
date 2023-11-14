def andarFrente(maoDireita_x,cotoveloDireito_x,dist_maoDireita_ombro,dist_entreMaos):
    if (maoDireita_x > cotoveloDireito_x) and (dist_maoDireita_ombro < 100) and (dist_entreMaos > 100):
        print("Andando Pra Frente")

def andarTras(maoEsquerda_x,cotoveloEsquerdo_x,dist_maoEsquerda_ombro,dist_entreMaos):
    if (maoEsquerda_x < cotoveloEsquerdo_x) and (dist_maoEsquerda_ombro < 100) and (dist_entreMaos > 100):
        print("Andando Pra Trás")