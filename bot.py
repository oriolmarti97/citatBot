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
        if status.in_reply_to_status_id is None:
            #Ni tan sols respon a ningú
            api.update(status='@%s :('%status.user.screen_name,in_reply_to_status_id=status.id_str)
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
