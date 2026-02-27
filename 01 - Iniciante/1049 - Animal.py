"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda
para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Vertebrado: - ave: carnivoro (aguia), onivoro (pomba)
            - mamifero: onivoro (homem), herbivoro (vaca)

Invertebrado: - inseto: hematofago (pulga), herbivoro (lagarta)
              - anelideo: hematofago (sanguessuga), onivoro (minhoca)

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima,
com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.

vertebrado
mamifero
onivoro
homem

vertebrado
ave
carnivo
aguia

invertebrado
anelideo
onivoro
minhoca
"""

animais = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'},  # fim ave
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'},  # fim mamifero
    },  # fim vertebrado
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'},  # fim inseto
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'}  # fim anelideo
    }  # fim invertebrado
}  # fim animais

vert_ou_invert = input()
ave_ou_mam_hem_ou_anel = input()
oni_ou_herb_hem_oniv = input()

print(animais[vert_ou_invert][ave_ou_mam_hem_ou_anel][oni_ou_herb_hem_oniv])
