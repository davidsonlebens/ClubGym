from gym.models import Abonnement
def run():
    for i in range(1,10):
        abonnement=Abonnement()
        abonnement.title="Abonnement No #%d" % i 
        abonnement.desc="Description abonnement No #%d" % i
        abonnement.image="http://default" 
        abonnement.save()
print("Operation réussi") 