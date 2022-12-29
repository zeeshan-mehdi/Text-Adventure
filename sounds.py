from playsound import playsound
import os
import time

from enemies import RatHumanoid
class sounds():
         
    def __init__(self):      
        self.dirname = os.path.dirname(os.getcwd())
        pass

    def StrangeCreatureSound(self):
        wolfsoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/strange-creature.mp3'
        
        time.sleep(1)
        playsound(wolfsoundpath)

    def HellHoundSound(self):
        hellhoundsoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/dog.mp3'
        time.sleep(1)
        playsound(hellhoundsoundpath)

    def RatHumanoidSound(self):
        RatHumanoidsoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/rat-sound.mp3'
        time.sleep(1)
        playsound(RatHumanoidsoundpath)

    def BatSound(self):
        BatSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/bat-sound.mp3'
       
        time.sleep(1)        
        playsound(BatSoundpath)

    def ZombieSound(self):
        zombiesoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/zombie-sound.mp3'
        playsound(zombiesoundpath)

    def CrawlerSound(self):
        crawlersoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/crawling-sound.mp3'
        time.sleep(1)
        playsound(crawlersoundpath)

    def errorSound(self):
        errorsoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/error-sound.mp3'
        time.sleep(1)
        playsound(errorsoundpath)

    def drinkSound(self):
        drinksoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/drink-sound.mp3'
        time.sleep(1)
        playsound(drinksoundpath)
    
    def GiantSpiderSound(self):
        GiantSpiderSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/spider-sound.mp3'
        time.sleep(1)
        playsound(GiantSpiderSoundpath)
    def CameraDropSound(self):
        GiantSpiderSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/camera-drop.mp3'
        time.sleep(1)
        playsound(GiantSpiderSoundpath)
    def StrangeVoicesSound(self):
        GiantSpiderSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/strange-voices.mp3'
        time.sleep(1)
        playsound(GiantSpiderSoundpath)

    def TigerSound(self):
        TigerSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/tiger-sound.wav'
        time.sleep(1)
        playsound(TigerSoundpath)


    def ElephantSound(self):
        ElephantSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/elephant-sound.mp3'
        time.sleep(1)
        playsound(ElephantSoundpath)

    def SnakeSound(self):
        SnakeSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/snake-sound.mp3'
        time.sleep(1)
        playsound(SnakeSoundpath)
    
    def LionSound(self):
        LionSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/lion-sound.mp3'
        time.sleep(1)
        playsound(LionSoundpath)
    
    def DragonSound(self):
        DragonSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/dragon-sound.mp3'
        time.sleep(1)
        playsound(DragonSoundpath)

    def BearSound(self):
        BearSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/bear-sound.mp3'
        time.sleep(1)
        playsound(BearSoundpath)

    def HighwaySound(self):
        HighwaySoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/motorbike.mp3'
        time.sleep(1)
        playsound(HighwaySoundpath)

    def RiverSound(self):
        RiverSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/river.mp3'
        time.sleep(1)
        playsound(RiverSoundpath)

    def FootStepSound(self):
        FootStepSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/footsteps.mp3'
        time.sleep(1)
        playsound(FootStepSoundpath)

    def ImpactSound(self):
        ImpactSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/impact-sound.mp3'
        time.sleep(1)
        playsound(ImpactSoundpath)

    def ImpactTwoSound(self):
        ImpactTwoSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/impact-sound2.mp3'
        time.sleep(1)
        playsound(ImpactTwoSoundpath)
    
    def SirenSound(self):
        SirenSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/siren-sound.mp3'
        time.sleep(1)
        playsound(SirenSoundpath)

    def ScreamSound(self):
        ScreamSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/screm.mp3'
        time.sleep(1)
        playsound(ScreamSoundpath)
    
    def LabSound(self):
        LabSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/lab-sound.mp3'
        time.sleep(1)
        playsound(LabSoundpath)

    def FootStepTweSound(self):
        FootStepTweSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/footsteps.mp3'
        time.sleep(1)
        playsound(FootStepTweSoundpath)

    def PunchSound(self):
        PunchSoundSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/punch.mp3'
        time.sleep(1)
        playsound(PunchSoundSoundpath)
    
    def DaggerSound(self):
        DaggerSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/dagger.mp3'
        time.sleep(1)
        playsound(DaggerSoundpath)
    
    def PillowSound(self):
        PillowSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/pillow.mp3'
        time.sleep(1)
        playsound(PillowSoundpath)
    
    def ProjectileSound(self):
        ProjectileSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/projectiel.mp3'
        time.sleep(1)
        playsound(ProjectileSoundpath)
    
    def CrossbowSound(self):
        CrossbowSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/crosbow.mp3'
        time.sleep(1)
        playsound(CrossbowSoundpath)

    def MoltovSound(self):
        MoltovSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/moltovsund.wav'
        time.sleep(1)
        playsound(MoltovSoundpath)
    
    def RevolverSound(self):
        RevolverSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/revolver.mp3'
        time.sleep(1)
        playsound(RevolverSoundpath)
    
    def SlingshotSound(self):
        SlingshotSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/slingshot.mp3'
        time.sleep(1)
        playsound(SlingshotSoundpath)
    
    def SwordSound(self):
        SwordSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/sword.mp3'
        time.sleep(1)
        playsound(SwordSoundpath)

    def KillSound(self):
        KillSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/kill.mp3'
        time.sleep(1)
        playsound(KillSoundpath)
    
    def VictorySound(self):
        VictorySoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/victory.mp3'
        time.sleep(1)
        playsound(VictorySoundpath)
    
    def HitSound(self):
        HitSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/hit-sound.mp3'
        time.sleep(1)
        playsound(HitSoundpath)
    
    def GameBeginSound(self):
        GameBeginSoundpath=self.dirname.rstrip()+'/TextAdventure-master/sounds'+'/game-sound.mp3'
        #os.path.dirname(__file__) + '/_gamsund.wav'
        time.sleep(1)        
        playsound(GameBeginSoundpath)
