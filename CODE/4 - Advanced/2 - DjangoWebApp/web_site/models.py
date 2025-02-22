from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): # -> Stiamo descrivendo il singolo oggetto, il post, con diversi attributi
    ### attributi ###
    
    title = models.CharField(max_length=100) # -> campo letterale con lunghezza massima di 100 caratteri
    content = models.TextField() # -> campo di scrittura del testo
    date_post = models.DateTimeField(auto_now_add=True) # -> data di pubblicazione
                                    # -> auto_now_add = la data è data quando il post è creatp
                                    # -> auto_now = la data è data quando il post viene aggiornato
    last_update = models.DateTimeField(auto_now=True)
                                    # -> de voglio poter mettere tutte e due le possibilita, modificando il tempo di pubblicazione, posso usare default                                
    now_date = models.DateTimeField(default=timezone.now) # -> No parantesi, valori default di time zone
    
    # ->  tutto questo serve per creare, importato user dal modulo django, chi è lautore del post
    #    se dovesse essere cancellato, l'utente, allora anche i post ad esso correlati lo saranno
    #    se vogliamo modifiicare tale cosa, basta modificare l0attributo on_delete
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    ### TUTTO QUETSO VERRAI POI SALVATO NEL NOSTRO DATABASE ### 
    
class User(models.Model):
    pass                          