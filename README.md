# capturaTweetCitat
Bot de twitter que rep un tweet i fa captura de pantalla del tweet citat
## Funcionament
El compte de twitter del bot és [@CitatBot](https://twitter.com/CitatBot)
Per fer-lo servir no cal seguir-lo, però és útil, ja que per etiquetar-lo et sortirà abans
### Veure tweet citat
La funcionalitat principal és veure el tweet citat per un tweet. 
Posem que hi ha un tweet X, que cita un tweet Y. Pots veure el tweet X, però l'autor del tweet Y et té bloquejat. 
Respon al tweet X etiquetant al bot (@CitatBot), i el bot s'encarregarà d'entrar-hi, fer captura i respondre't amb ella
### Veure tweet respost
Posem que tens un tweet X que respon a un tweet Y. Com abans, pots veure el tweet X, però no el tweet Y.
Respon al tweet X de la mateixa manera, i el bot farà el mateix
Nota: si el tweet X també té citat un tweet, això no funcionarà
### Privadesa
Actualment tothom pot veure com sol·licites el tweet i el bot et respon. Està en desenvolupament una opció que consistirà en passar-li el tweet per MD (missatge directe) i enviar la captura també per MD. 
No obstant, com que el bot el faig en estones lliures quan tinc ganes de programar, i a la vegada estic programant altres coses, pot trigar una mica
## Preguntes:
### Per què serveix?
Mai t'has trobat amb un tweet criticant un altre tweet, però no pots veure què diu perquè et té bloquejat?
Has hagut d'entrar amb finestra d'incògnit, o bé demanar captura de pantalla?
Aquest bot ho automatitza per tu
Respon a un tweet etiquetant al bot, i ell entrarà al tweet citat a fer captura

### Pot capturar qualsevol tweet?
No. No pot hackejar twitter :(
El seu funcionament és que entra al tweet sense haver iniciat sessió i li fa captura. Això vol dir que pot capturar qualsevol tweet d'un compte **públic**, mentre que els tweets privats no els podrà capturar

### I no poden bloquejar-lo?
Poden bloquejar el bot. Però seguirà funcionant, ja que la captura la fa sense haver iniciat sessió

### No és poc ètic això?
No. El bot només permet fer captures de pantalla a tweets públics. Són tweets que pots veure igualment si tanques la sessió, o si hi entres des d'un altre compte. El que fa aquest bot és automatitzar-ho, però no et dóna cap informació que no tinguis accessible

## Vull utilitzar el programa
El programa es troba sota la llicència GNU GPLv3 (Llicència Pública General de GNU, versió 3). Pots consultar-la [aquí](https://github.com/oriolmarti97/capturaTweetCitat/blob/master/LICENSE). Es tracta d'una llicència de [Software Lliure](https://www.gnu.org/philosophy/free-sw.ca.html) i [copyleft](https://www.gnu.org/licenses/copyleft.html). Fonamentalment, el que vol dir això és que pots utilitzar-lo, modificar-lo i redistribuir-lo (amb o sense modificacions), sempre que el codi conservi la mateixa llicència
No obliga a avisar a l'autor de cap mena de modificació o redistribució. No obstant, t'agrairé que si fas alguna millora contactis amb mi, de manera que jo també la pugui aplicar. 
### Com faig per executar-lo jo?
El primer és, lògicament, descarregar el codi font. 
El programa està pensat per correr en un servidor Ubuntu sense entorn gràfic, ja que és el que faig servir. No obstant, hauria de funcionar en qualsevol sistema basat en Unix que tingui instal·lats els programes **cutycapt** i **xvfp**, així com **python 3** i **pip**. Aquesta instal·lació, però, no cal fer-la a mà, sinó que la pots fer utilitzant el script [setup.sh](https://github.com/oriolmarti97/capturaTweetCitat/blob/master/setup.sh). Aquest script requereix tenir instal·lat apt, bash, wget i python 3, que són paquets que acostumen a estar instal·lats a tot arreu. Podeu modificar-lo si us cal
Executant-lo tindreu preparat l'entorn per executar el programa

Haureu de crear un arxiu **key.py**, que declari quatre variables que seran les claus per accedir al bot. Aquest arxiu ha sigut afegit conscientment al .gitignore, perquè no voldria que ningú accedís al bot sense permís. Les quatre variables es diran consumer_key, consumer_secret, access_token, access_token_secret, i te les proporciona Twitter

Finalment executeu l'arxiu [server.sh](https://github.com/oriolmarti97/capturaTweetCitat/blob/master/server.sh). Aquest arxiu executa infinitament el bot redirigint les seves sortides a dos arxius que faran de logs. Si en algun moment un error tanca el bot, tornarà a obrir-se automàticament gràcies a això
Per comoditat pots crear un servei utilitzant la comanda systemctl. Pots trobar-ne més informació a internet. Això permet que el bot arrenqui en arrencar la màquina
