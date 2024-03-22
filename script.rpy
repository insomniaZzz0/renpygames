
# personagens
define p = Character("Pisquinha")
define h = Character("Husk")
define k = Character("Kai")


# o Jogo começa aqui

label start:

    scene cena1
    with fade
    #play music "/audio/normar.mp3"

    #"Dois irmãos Pisquinha e Husk lutam pela liderança do clã dos lobos"
    show goujo at right
    with dissolve

    p "Não quero brigar com você irmão"
    
    p "Esta luta não faz sentido pra mim"
    hide goujo
    
    show lobo at left
    with dissolve

    h "Deixa de conversa mole Pisquinha"

    h "Isto pra mim tem outro nome"

    h "Covardia!"  

    hide lobo

    "Pisquinha deve enfrentar o irmão Husk?"

menu:

    "Sim":
        jump game

    "Não":
        jump book

label game:
    show goujo at right
    with dissolve

    p "Se não outra escolha, eu estou pronto irmão"
   
    hide goujo
   
    show lobo at left
    with dissolve
    h "Farei o que deve ser feito"
   
    hide lobo
   
    jump marry

label book:
    show lobo at left
    with dissolve
   
    h "Você não tem escolha, lembre-se a força vem do seu interior"
   
    hide lobo
   
    #show goujo at right
    with dissolve
   
    p "Eu não queria, mas é o unico jeito"
   
    hide goujo
    jump marry

label marry:

    "Os irmão batalham"  
    stop music
    return
