# Portable Pi

Es una "Placa Padre" la cual se conecta a la Raspberry (y compatible con otras placas) la cual le brinda de una pantalla y un teclado (por ahora, luego la voy a poner mas cosas)




todo comenzo cuando queria comprarme la Pocket Chip (https://imgur.com/l437LvK 65 USD +-, es una computadora portable basada en ARM), como vivo en argentina comprarla me iba a salir alrededor de 6000 ars o 150 USD por lo que preferi intentar construirme una parecida basada en la conocida raspberry Pi , no estoy seguro si en la Pi3 o Pi Zero por un tema de ergonomia en la mano y consumo energetico.


el diseño al estar basado en la pocket chip la raspberry pi seria insertada con sus GPIOs machos desde atras del PortablePi (todavia nose si esta al estar solamente sujeta con los gpios va a quedar bien agarrada, pero como la idea es que la raspberry sea de facil acceso para poder sacarla del "Expansion Board" y usarla como cualquier Raspberry pi)


## Compabilitys with Others Single Board Computers

Este diseño tambien se podria adaptar a las otras placas como a Orange Pi, Pine64, LattePanda , y otras placas, hasta las que no tiene salida de video ya que esta pantalla es via SPI.

seria tanto como hacer espacio en el diseño del PortablePi para que entre el conector para otra placa en caso de que no comparta la distribucion de pines con la raspberry 



//para ver los pines y sus valores dejo una pagina que te los muestra y explica que hacen
https://pinout.xyz

## Compabilitys with Operatives Systems

el proyecto esta pensado para que funcione en una raspberry pi zero con raspbian o alguna distribucion que soporte tan poca RAM pero la verdad no conozco la forma de comunicar el display via SPI a otros sistemas operativos o a otras arquitecturas de procesadores ya que los drivers del fabricante solo estan pensados para la raspberry pi con raspbian o alguna distro parecida.

Tambien el teclado de la Pocket pi y otros proyectos parecidos como la qwertyPi hacen uso del TC8418 pero esto es dificil de conseguir en donde me ubico, quizas lo podria conseguir via aliexpress que me saldria algo de 10 USD pero anda a saber cuando va a llegar 


hace varios años me compre la raspberry pi zero w por lo que actualmente el diseño esta pensado en esta pero en un futuro no muy lejano (si llego a conseguir una raspberry pi 3 o 2 del modelo B) pienso adaptarla a esta ya que posee 4 USB nativos, ethernet y un hdmi completo (un problema en esto es que pensaba poner la parte de los USB y el ethernet que sobresalga un poco por la parte superior pero si esta centrada en la parte superior el HDMI, Jack de video y el pin de carga quedan dentro del diseño y sin un facil acceso desde el costado del dispositivo por lo que una opcion seria poner esta en un costado, el izquierdo para tener el acceso a los puertos pero quedaria desentrado)






https://imgur.com/PwzQMJI
![alt text](https://imgur.com/PwzQMJI)

![alt text](https://github.com/lukaneco/PortablePi/blob/master/piportable%20v7/scheenshots/portablePi%20v7-brd.png)








# Upgrade 09/02/2019
## investigating a new Keyboard IC - MSP430 is a very cheaply solution

estaba boludeando por internet cuando noticia salvaje aparece xdxd
encontre que hay un IC que se puede usar para la matris del keyboard y que ya esta desarrollado el codigo y los drivers tanto por usb como por I2C

http://www.ti.com/lit/ug/tidu521/tidu521.pdf

voy a investigar sobre como emplearlo en este proyecto
