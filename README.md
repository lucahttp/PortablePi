
# Portable Pi

Is an Father Board witch can connect to the raspberry pi (currently compatible to this gpio configuration, orange pi thinkercard, an anothers) this aport an Screen and keyboard (in one board) then i will add more things like audio jack, ethernet port, hub USB and everything you can imagine and put in your pockets.

![alt text](https://github.com/lukaneco/PortablePi/blob/master/piportable%20v7/scheenshots/portablePi%20v7-brd.png)

## History
it started when i wanted to buy the newly released Pocket Chip (https://imgur.com/l437LvK 50 USD + taxes + shipping, something of 120 USD)the chip is a competitor of the raspberry pi but offered for 9 USD and for 40 USD more could you make this pocket.

everything looked like fine until the company that makes CHIP, declared bankrupt.
 
 
 
 # Search a compatible keyboard for the portable pi
 
 
 ## 1. Usb Bluetooth keyboard (cheaply)
 
the first option I thought (my father told me) was a bluetooth keyboard (is very cheaply opcion for those dont like the hardware) but i think isnt practical

<img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/bluetooth%20keyboard%20asdasd.png" alt="usb keyboard" width="500px" height="whatever">



 ## 2. Xbox ChatPad
 
the second opcion is a Xbox Chatpad but is missing keys like >< ,Ctrl , Alt, Command and others.
if you not need this keys is a good opcion for this project

the way to connect to the raspberry is a reprogram the Microchip PIC inside the keyboard, BenHacksShow show how do it [here](https://www.youtube.com/watch?v=Hjdj14C_jAI) and others examples [with raspberry](https://www.youtube.com/watch?v=2sVS-jMGD7w), [an brazilian](https://www.youtube.com/watch?v=Mo7BqMrNIDs) and [this](https://www.youtube.com/watch?v=I20lXAS_IJs)

it also can use directly like TX/RX but have to run aprogram to convert this signals in keyboard inputs and it slow down the limited resources of the computer. [here in reddit](https://www.reddit.com/r/raspberry_pi/comments/5t4xgy/raspberry_pi_xbox_chatpad_keyboard/)
 
<img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/xbox%20chatpad%20asdasd.jpg" alt="xbox chatpad" width="500px" height="whatever">


 ## 3. Arduino Usb Keyboard or Serial 
 
the third opcion that came my way that i was found are a Arduino Pro Micro as a USB keyboard like [teensy Thumb Keyboard](https://hackaday.io/project/162281-teensy-thumb-keyboard) but in this opcion i would have to conect via USB to the raspberry and this is not a good idea because isnt practical

but i dont discard the idea of adapt this opcion for use via GPIO


- the teensy Thumb Keyboard
  [teensy Thumb Keyboard](https://hackaday.io/project/162281-teensy-thumb-keyboard) 
  
<img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/1%20I2jlIVvAtG6rRXWzsqDOcA.jpeg" alt="teensy" width="400px" height="whatever"> <img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/1%20l0At8TJehMSu8sPScRZbhA.jpeg" alt="teensy" width="400px" height="whatever">


 - RC2014 keyboard
 
   The RC2014 [page](http://rc2014.co.uk/modules/universal-micro-keyboard/) shown a project but i dont have any idea of how to       
   adapt this to PortablePi
 
   <img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/Keyboard4.jpg" alt="rc2014" width="400px" height="whatever"> <img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/Keyboard5.jpg" alt="rc2014" width="400px" height="whatever">
      
   [Uinput: The New Hope]()
 ## 4. Usb keyboard (very cheaply)
 
 This opcion is better for those do not have a way to get electronic components but the layout and matrix config is not prepared to direct access in the keyboard but could be config these features via software
 
 <img src="https://github.com/lukaneco/USB-keyboard-Board-PCB-pinout-diagram/blob/master/cheaply%20usb%20keyboard%20PCB%20board%20.jpg" alt="rc2014" width="400px" height="whatever">
 
 [design of cheaply USB Keyboard opcion](https://github.com/lukaneco/USB-keyboard-Board-PCB-pinout-diagram)
 
 
 
 
 ## 5. the way most factible is TCA8418

I found that they use the other projects like PocketChip or qwertyPi and others better keyboards for raspberry pi (and others microcomputers) more professionals. the problem is that component isnt easyly to found in my country and is a smaller than otrer solutions (hard to solder to the board).

a good news is that the documentation in the [manufacturer page](http://www.ti.com/product/TCA8418)


https://e2e.ti.com/support/interface/f/138/t/202938



[Datasheet of TCA8418](www.ti.com/lit/ds/symlink/tca8418.pdf)

[Code for malti](https://hackaday.io/project/5081-malti/log/17068-it-lives)

- [Malti](https://hackaday.io/project/5081-malti) is a similar project but that dont have the idea of easy plug and play.

- [qwertyPi](https://mozzwald.com/articles/2017/12/01/qwertypi-a-handheld-raspberry-pi-qwerty-computer) is the more similar  project but that dont have the easy plug of the raspberry 

- [Ben Heck’s DIY Calculator](https://www.youtube.com/watch?v=lJu1ij_Emlk) is a similar project for other destiny

- [other font of information]() that guy have an project to make this way (the page is writed in german)

  - [video](https://www.youtube.com/watch?v=j4ymw0hWN1o)
  
  - [web page](https://5volt-junkie.net/i2c-keypad/)
  
- [pwav robot](https://twitter.com/pwavrobot) is other guy that make something with TCA8418

  - [link](https://twitter.com/pwavrobot/status/1075758165944385536)

  - [snaponair](http://www.snaponair.com/)

  - [lorawan pager](https://hackaday.io/project/22038-the-lorawan-pager)

  - [zerophone](https://hackaday.io/project/19035-zerophone-a-raspberry-pi-smartphone)
 
 
repeat, the problem is the shipping from US or China is very expensive and it takes a long time to get here.
i found an options to buy in [Aliexpress](https://es.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190210085412&SearchText=TCA8418) relatively cheap, Mouser, TI store and others sellers the shipping cost is more than aliexpress but more quickly (about 40 usd the shipping cost).


 
 # Search a display for the portable pi
 
 
 I'm still looking for better options for now i use the cheapest display quality/price, and that is 
 
- Pi Lcd 3.5 Touch 320x480
 [3.5inch RPi LCD 480x320](https://www.waveshare.com/3.5inch-rpi-lcd-a.htm)
 via GPIO (for female header, i will replaced with other connector smaller)
 
 <img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/3.5inch-rpi-lcd-a-2_3.jpg" alt="display" width="400px" height="whatever">  <img src="https://github.com/lukaneco/PortablePi/blob/master/re%20img/35i-tft-lcd-320x480-touch-display-raspberry-pi.jpg" alt="display" width="400px" height="whatever">
 
 
   the raspberry comunicate to the display via SPI, i dont think abaout others ways to gotcha it. 
   i know that the raspberry pi 2/3/other SBC have a DSI conector but i dont know how to use this
 
 
 
- via HDMI (i dont not recomend this opcion because it will discard the plug and plug metodology)


 
 
 


# Concept

the general idea is offer make portable the raspberry pi without discard the posibility of extract it, the purpose of this is debug projects anywhere without a desktop computer or notebook

https://imgur.com/8SMtQg4 


<img src="https://i.imgur.com/8SMtQg4.jpg" width="800px" height="whatever">

to make conceptual maps is a good tool [Cmap](https://cmapcloud.ihmc.us/)


# About Pocket Chip

is currently unavailable

https://www.pcworld.com/article/3094364/hardware/inside-the-pocketchip-a-49-portable-linux-computer.html

the page not found in the internet neither the documentation to make other similar

https://www.newmuseumstore.org/next-thing-co-pocket-chip


# Upgrade 09/02/2019
## investigating a new Keyboard IC - MSP430 is a very cheaply solution

estaba boludeando por internet cuando noticia salvaje aparece xdxd
encontre que hay un IC que se puede usar para la matris del keyboard y que ya esta desarrollado el codigo y los drivers tanto por usb como por I2C

http://www.ti.com/lit/ug/tidu521/tidu521.pdf

voy a investigar sobre como emplearlo en este proyecto

 
 


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









# Upgrade 11/02/2019
## investigating a new Keyboard software - Uinput is a very easy to use solution

i thinking about use uinput library of python, before dont considereded because CPU consumition but it would be minimal than the    
normal use, unless we care a lot about the performance issue would be a good option.

and matrix can be via atmega328 or some IC to do convert multiple inputs on less than, like pcf8574 or other I2C to parallel

http://www.ti.com/lit/ds/symlink/pcf8574.pdf

could also make atmega328 code to compatible for existing TCA8418 driver CODE or such any other similar


https://github.com/tuomasjjrasanen/python-uinput

https://pypi.org/project/python-uinput/

http://tjjr.fi/sw/python-uinput/

https://launchpad.net/python-uinput

this option is used for retro pi and other similar projects







voy a investigar sobre como emplearlo en este proyecto

