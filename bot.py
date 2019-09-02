import tweepy
import webscreenshot
import os
from key import consumer_key, consumer_secret, access_token, access_token_secret

ultima_id=None


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

class ElMeuEscoltador(tweepy.StreamListener):
    def on_status(self, status):
        global api
        #print(status.text)
        status_replied=api.get_status(status.in_reply_to_status_id)
        #print(status_replied.text)
        try:
            citat=api.get_status(status_replied.quoted_status_id)
        except:
            pass
        #print(citat.text)
        
        #Fem la captura
        ruta='./temp/'+citat.id_str
        os.mkdir(ruta)
        url="https://twitter.com/%s/status/%s"%(citat.user.screen_name,citat.id)
        os.system('webscreenshot %s -o %s'%(url,ruta))

        _,_,arxius = next(os.walk(ruta))
        print(arxius)
        foto=ruta+'/'+arxius[0]
        
        print(status.id_str)
        try:
            api.update_with_media(foto,status='@%s'%status.user.screen_name,in_reply_to_status_id=status.id_str)
        except Exception as e:
            print(e)
            print('No he pogut respondre al tweet')

        os.remove(foto)
        os.rmdir(ruta)






escoltador=ElMeuEscoltador()
stream=tweepy.Stream(auth=api.auth,listener=escoltador)
stream.filter(track=['CitatBot'])
