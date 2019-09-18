#Bot de twitter per fer captura de pantalla al tweet citat
#(english license below)
#Copyright (C) 2019  Oriol Martí i Rodríguez

#Aquest programa és lliure; el podeu redistribuir i/o modificar
# d'acord amb els termes de la Llicència pública general de GNU tal 
# i com la publica la Free Software Foundation; tant se val la versió 3
# de la Llicència com (si ho preferiu) qualsevol versió posterior.


#Aquest programa es distribueix amb l'esperança que serà útil, 
#però SENSE CAP GARANTIA; ni tant sols amb la garantia de 
#COMERCIALITZABILITAT O APTITUD PER A PROPÒSITS DETERMINATS.  Vegeu
#la Llicència general pública de GNU per a més detalls. 


#Hauríeu d'haver rebut una còpia de la llicència pública general 
#de GNU amb aquest programa; si no, consulteu https://www.gnu.org/licenses/



#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
import tweepy
import webscreenshot
import os
#Per executar el bot cal tenir un arxiu key.py que declari les quatre variables amb els tokens donats per Twitter
from key import consumer_key, consumer_secret, access_token, access_token_secret


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

def baixaIResponTweet(tweetABaixar, tweetARespondre):
    #Fem la captura
    if not hasattr(tweetABaixar,'media') or tweetABaixar.media is None:
        alcada=600
    else:
        alcada=1200
    ruta='./temp/'+tweetABaixar.id_str+'.png'
    url="https://twitter.com/%s/status/%s"%(tweetABaixar.user.screen_name,tweetABaixar.id_str)
    os.system('xvfb-run cutycapt --url=%s --min-width=600 --min-height=%i --out=%s 2>&1 >/dev/null'%(url,alcada,ruta))
    
    try:
        api.update_with_media(ruta,status='@%s'%tweetARespondre.user.screen_name,in_reply_to_status_id=tweetARespondre.id_str)
    except Exception as e:
        print(e)
        print('No he pogut respondre al tweet')

    os.remove(ruta)

class ElMeuEscoltador(tweepy.StreamListener):
    def on_status(self, status):
        global api
        #Si té aquest atribut, vol dir que el tweet respon a gent no mencionada explícitament al tweet. Com que podria ser que el bot fos un d'ells, comprovem si ho és (si algú respon a un tweet del bot no hem de fer captura)
        if hasattr(status,'display_text_range'):
            if '@citatbot' not in status.text[status.display_text_range[0]:].lower():
                return
        if status.in_reply_to_status_id is None:
            #Ni tan sols respon a ningú
            api.update(status='@%s Hola :D'%status.user.screen_name,in_reply_to_status_id=status.id_str)
            return
        status_replied=api.get_status(status.in_reply_to_status_id)
        if not hasattr(status_replied,'quoted_status_id') or status_replied.quoted_status_id is None:
            if not hasattr(status_replied,'in_reply_to_status_id') or status_replied.in_reply_to_status_id is None:
                #El tweet al que respon no cita ni respon a ningú. Com que hi ha respost, el veu, de manera que no cal captura
                api.update(status='@%s :('%status.user.screen_name,in_reply_to_status_id=status.id_str)
                return
            citat=api.get_status(status_replied.in_reply_to_status_id)
        else:
            citat=api.get_status(status_replied.quoted_status_id)
        baixaIResponTweet(citat,status)

    def on_direct_message(self,status):
        print(status) #Falta implementar-ho. La idea és poder interactuar també per privat
        






escoltador=ElMeuEscoltador()
stream=tweepy.Stream(auth=api.auth,listener=escoltador)
stream.filter(track=['CitatBot'])
