
# Portable Pi

Is an Father Board witch can connect to the raspberry pi (currently compatible to this gpio configuration, orange pi thinkercard, an anothers) this aport an Screen and keyboard (in one board) then i will add more things like audio jack, ethernet port, hub USB and everything you can imagine and put in your pockets.


## History
it started when i wanted to buy the newly released Pocket Chip (https://imgur.com/l437LvK 50 USD + taxes + shipping, something of 120 USD)the chip is a competitor of the raspberry pi but offered for 9 USD and for 40 USD more could you make this pocket.

everything looked like fine until the company that makes CHIP, declared bankrupt.
 
 
 
 # Search a compatible keyboard for the portable pi
 
 
 ## 1. Usb keyboard cheaply
 
the first option I thought (my father told me) was a bluetooth keyboard (is very cheaply opcion for those dont like the hardware) but i think isnt practical

<img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/bluetooth%20keyboard%20asdasd.png" alt="usb keyboard" width="500px" height="whatever">

[design of cheaply USB Keyboard opcion](https://github.com/lukaneco/USB-keyboard-Board-PCB-pinout-diagram)


 ## 2. Xbox ChatPad
 
the second opcion is a Xbox Chatpad but is missing keys like >< ,Ctrl , Alt, Command and others.
if you not need this keys is a good opcion for this project

the way to connect to the raspberry is a reprogram the Microchip PIC inside the keyboard, BenHacksShow show how do it [here](https://www.youtube.com/watch?v=Hjdj14C_jAI) and others examples [with raspberry](https://www.youtube.com/watch?v=2sVS-jMGD7w), [an brazilian](https://www.youtube.com/watch?v=Mo7BqMrNIDs) and [this](https://www.youtube.com/watch?v=I20lXAS_IJs)

it also can use directly like TX/RX but have to run aprogram to convert this signals in keyboard inputs and it slow down the limited resources of the computer. [here in reddit](https://www.reddit.com/r/raspberry_pi/comments/5t4xgy/raspberry_pi_xbox_chatpad_keyboard/)
 
<img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/xbox%20chatpad%20asdasd.jpg" alt="xbox chatpad" width="500px" height="whatever">


 ## 3. Arduino Usb Keyboard or Serial 
 
the third opcion that came my way that i was found are a Arduino Pro Micro as a USB keyboard like [teensy Thumb Keyboard](https://hackaday.io/project/162281-teensy-thumb-keyboard) but in this opcion i would have to conect via USB to the raspberry and this is not a good idea because isnt practical

but i dont discard the idea of adapt this opcion for use via GPIO
 
 
 
 
 



# Español

# Portable Pi

Es una "Placa Padre" la cual se conecta a la Raspberry (y compatible con otras placas) esta le brinda una pantalla y un teclado (en una sola placa) luego la voy a poner mas cosas como un jack de audio, un puerto ethernet, un hub usb y todo lo que puedas imaginar o poner en tus bolsillos.


 
 esta era una competidora de la raspberry pi pero de un

## History

todo comenzo cuando queria comprarme la Pocket Chip (https://imgur.com/l437LvK 65 USD +-, es una computadora portable basada en ARM), como vivo en argentina comprarla me iba a salir alrededor de 6000 ars o 150 USD por lo que preferi intentar construirme una parecida basada en la conocida raspberry Pi , no estoy seguro si en la Pi3 o Pi Zero por un tema de ergonomia en la mano y consumo energetico.


el diseño al estar basado en la pocket chip la raspberry pi seria insertada con sus GPIOs machos desde atras del PortablePi (todavia nose si esta al estar solamente sujeta con los gpios va a quedar bien agarrada, pero como la idea es que la raspberry sea de facil acceso para poder sacarla del "Expansion Board" y usarla como cualquier Raspberry pi)


## Compabilitys with Others Single Board Computers

Este diseño tambien se podria adaptar a las otras placas como a Orange Pi, Pine64, LattePanda , y otras placas, hasta las que no tiene salida de video ya que esta pantalla es via SPI.

seria tanto como hacer espacio en el diseño del PortablePi para que entre el conector para otra placa en caso de que no comparta la distribucion de pines con la raspberry 



//para ver los pines y sus valores dejo una pagina que te los muestra y explica que hace cada uno

https://pinout.xyz

## Compabilitys with Operatives Systems

el proyecto esta pensado para que funcione en una raspberry pi zero con raspbian o alguna distribucion que soporte tan poca RAM pero la verdad no conozco la forma de comunicar el display via SPI a otros sistemas operativos o a otras arquitecturas de procesadores ya que los drivers del fabricante solo estan pensados para la raspberry pi con raspbian o alguna distro parecida.

## Keyboard

El teclado de la Pocket pi inicialmente lo iba a hacer via USB reutilizando la placa logica de un teclado comun que sale alrededor de 2 USD o uno roto que podramos conseguir, pero me puse a pensar que no seria comodo para sacar la raspberry de y otros proyectos parecidos como la qwertyPi hacen uso del TC8418 pero esto es dificil de conseguir en donde me ubico, quizas lo podria conseguir via aliexpress que me saldria algo de 10 USD pero anda a saber cuando va a llegar 


hace varios años me compre la raspberry pi zero w por lo que actualmente el diseño esta pensado en esta pero en un futuro no muy lejano (si llego a conseguir una raspberry pi 3 o 2 del modelo B) pienso adaptarla a esta ya que posee 4 USB nativos, ethernet y un hdmi completo (un problema en esto es que pensaba poner la parte de los USB y el ethernet que sobresalga un poco por la parte superior pero si esta centrada en la parte superior el HDMI, Jack de video y el pin de carga quedan dentro del diseño y sin un facil acceso desde el costado del dispositivo por lo que una opcion seria poner esta en un costado, el izquierdo para tener el acceso a los puertos pero quedaria desentrado)






https://imgur.com/PwzQMJI
![alt text](https://imgur.com/PwzQMJI)

![alt text](https://github.com/lukaneco/PortablePi/blob/master/piportable%20v7/scheenshots/portablePi%20v7-brd.png)


# Concept

https://imgur.com/8SMtQg4


<img src="https://i.imgur.com/8SMtQg4.jpg" width="800px" height="whatever">

https://cmapcloud.ihmc.us/

# About Pocket Chip

is currently unavailable
https://www.pcworld.com/article/3094364/hardware/inside-the-pocketchip-a-49-portable-linux-computer.html

https://www.newmuseumstore.org/next-thing-co-pocket-chip


# Upgrade 09/02/2019
## investigating a new Keyboard IC - MSP430 is a very cheaply solution

estaba boludeando por internet cuando noticia salvaje aparece xdxd
encontre que hay un IC que se puede usar para la matris del keyboard y que ya esta desarrollado el codigo y los drivers tanto por usb como por I2C

http://www.ti.com/lit/ug/tidu521/tidu521.pdf

voy a investigar sobre como emplearlo en este proyecto

