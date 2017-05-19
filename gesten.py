def initialize():
    # set_servo_pulse(0,in_kopf_drehen)  #Kopf (drehen)
    set_servo_pulse(1,in_kopf_neigen)  #Kopf (seitlich neigen)
    set_servo_pulse(2,in_kopf_nicken)    #Kopf (nicken)
    set_servo_pulse(3,in_augen_seitlich)  #Augen (seitlich)
    set_servo_pulse(4,in_augen_hoch)  #Augen (hoch/runter)

def augen_obenrechts():
    initialize()
    set_servo_pulse(3,in_augen_seitlich-0.1)  #Augen (seitlich)
    set_servo_pulse(4,in_augen_hoch-0.3)  #Augen (hoch/runter)
    time.sleep(0.5)
    set_servo_pulse(3,in_augen_seitlich)  #Augen (seitlich)
    set_servo_pulse(4,in_augen_hoch)  #Augen (hoch/runter)

def nicken():
    initialize()
    zwischenschritte = 20 #Feinheit der Bewegung
    dauer = 0.3       # dauer der bewegung
    kopf_nicken_tmp = in_kopf_nicken #aktuelle position kopf_nicken
    kopf_neigen_tmp = in_kopf_neigen #aktuelle position kopf_neigen
    kopf_nicken_schritt = ((in_kopf_nicken - kopf_nicken_unten) / zwischenschritte) #positionsaenderung pro Schritt kopf_nicken
    kopf_neigen_schritt = ((in_kopf_neigen - (in_kopf_neigen + 0.2)) / zwischenschritte) # positionsaenderung pro Schritt kopf_neigen 
    zeit_schritt = ((dauer / 2) / zwischenschritte) # dauer jedes einzelnen Schrittes
    while kopf_nicken_tmp > kopf_nicken_unten:  #kopf runter
        kopf_nicken_tmp = (kopf_nicken_tmp - kopf_nicken_schritt)
        kopf_neigen_tmp = (kopf_neigen_tmp + kopf_neigen_schritt)
        set_servo_pulse(kopf_nicken, kopf_nicken_tmp)
        set_servo_pulse(kopf_neigen, kopf_neigen_tmp)
        time.sleep(zeit_schritt)
    time.sleep(0.3)
    while kopf_nicken_tmp < in_kopf_nicken: #kopf hoch
        kopf_nicken_tmp = (kopf_nicken_tmp + kopf_nicken_schritt)
        kopf_neigen_tmp = (kopf_neigen_tmp - kopf_neigen_schritt)
        set_servo_pulse(kopf_nicken, kopf_nicken_tmp)
        set_servo_pulse(kopf_neigen, kopf_neigen_tmp)
        time.sleep(zeit_schritt)
