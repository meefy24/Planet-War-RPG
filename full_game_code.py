import time
import random
import sys

#SPAWN STATS
health = 100
total_health = 100 #print health: {health}/{total_health}
power = 20 
level = 1
stage = 0
inventory = ['elastic band']
monster = False
strawberry = 0


#SPAWN MESSAGE (Jeffrey's intro)
print("PLANET 0:")
print("UNKNOWN VOICE: Hey...you awake?")
time.sleep(2)
print("Oh, you are! Finally!")
time.sleep(1)
print("Welcome back, friend! You must've been knocked out when we landed on [PLANET 0].")
time.sleep(1)
print("I'm JEFFREY, your astronaut partner! And...you are?")
time.sleep(1)
print()
name = input(">> ").upper()
print()
print(f"JEFFREY: Welcome, traveller {name}! Get ready for an adventure!")
time.sleep(1)
print("A very long one. Ten planets long, to be exact. But lucky you! You've got a hidden talent, so I'm told. What is it?")
print()


#SELECT SUPER POWERS
while True:
    print('Select a talent:')
    power_choice = input("[SUPER STRENGTH] or [SHIELD]: ")
    if power_choice.lower() == 'super strength':
        print()
        print('~' * 40)
        print("Power boost gained!")
        power += 20
        print(f"Power = {power}")
        print('~' * 40)
        break
    elif power_choice.lower() == 'shield':
        print()
        print('~' * 40)
        print("Shield increases your max health!")
        health += 20
        total_health += 20
        print(f"Current health: {health}/{total_health}")
        print('~' * 40)
        break
    else:
        print("Hmm, I've never heard of that one. Come again?")
print()
time.sleep(1)
print("JEFFREY: Wow, that's amazing!")


#OPEN STATS INTRO
print("Mind if I view the rest of your stats?")
while True:
    stats_choice = input("Type [S] to view stats: ")
    if stats_choice.lower() == 's':
        print()
        print('~' * 40)
        print(f"Health: {health}/{total_health}")
        print(f"Strength: {power}")
        print(f"Traveller level: {level}")
        print('~' * 40)
        print()
        break
    else:
        print("JEFFREY: Uhh that's not it. Try typing [S].")

        
#INVENTORY INTRO
time.sleep(1)
print(f"Jeffrey: You seem to have spawned with a backpack, traveller {name}! Might I take a peek inside?")
inv = input("Type [I] to open inventory: ")
if inv.lower() == 'i':
    print()                 
    print('~' * 40)
    print(f"inventory contents: {inventory}")
    print('~' * 40)
    print()

time.sleep(1)
print("...Huh. Not a very useful weapon, but I'm sure we'll find something better.")
time.sleep(2)
print()
print("Jeffrey: The stars will be setting soon, traveller. I think we should get going!")
print("Open your menu anytime by typing [MENU]!")
print()
time.sleep(2)


#ACTUAL GAME LOOP
while True:
    #ACTION
    print()
    print(f"What would you like to do next,  traveller {name}?")
    action = input()
    time.sleep(1)
    
    if action.lower() == 'menu':
        print()
        print('~' * 40)
        print('Open inventory: [I]')
        print('View stats: [S]')
        print('Move on to the next planet: [M]')
        print('~' * 40)
        print()
    elif action.lower() == 's':
        print()
        print('~' * 40)
        print("CURRENT STATS:")
        print(f"Health: {health}/{total_health}")
        print(f"Strength: {power}")
        print(f"Traveller level: {level}")
        print('~' * 40)
        print()
    elif action.lower() == 'i':
        print()
        print('~' * 40)
        print(f"Current inventory: {inventory}")
        print('~' * 40)
        print()
    elif action.lower() == 'm':
        print()
        stage += 1


###INDIVIDUAL PLANETS###
    
    if stage == 1: #CAILEIGH
        print("PLANET 1:")
        print("JEFFREY: Look out, traveller! Our first monster!")
        print("You have found a GIANT WORM!")
        print()
        wormfight = input("Will you [FIGHT] or [RUN]?: ")
        
        #fight loop
        while True:
            if wormfight.lower() == 'fight':
                #giant worm's attack (30 damage)
                time.sleep(1)
                print()
                print("GIANT WORM attacks first!")
                print("You have lost 30 health points")
                health -= 30
                print(f"Current health: {health}/{total_health}")
                print()
                time.sleep(2)
                #Player attack (kills worm)
                print(f"You attack the GIANT WORM with the ELASTIC BAND in your inventory, and deal {power} damage!")
                time.sleep(1)
                print("Attack successful! GIANT WORM has been defeated!")
                time.sleep(1)
                #Rewards
                print()
                print("JEFFREY: Nice shot! And look- here's your rewards!")
                print()
                time.sleep(1)
                print(">>You have leveled up!")
                level += 1
                print(">>Player level: 2")
                print(">>New weapon unlocked: WOODEN SWORD")
                inventory.append("Wooden Sword")
                power += 30
                time.sleep(1)
                break
    
            elif wormfight.lower() == 'run':
                print()
                print("You have successfully escaped!")
                break
    
            else:
                print()
                print("Sorry traveller, that's not a valid action.")
                print()
        
        #When fight/run is done
        print()
        print("JEFFREY: Nice work! Jump to the next planet whenever you're ready.")
            


    elif stage == 2: #ANDY
        print("PLANET 2:")
        print("JEFFREY:Congratulations!You found the armor here.")
        print("JEFFREY:I have automatically equipped it for you.")
        health += 20
        inventory.append("armor")

    
    elif stage == 3: #LEO
        print("PLANET 3:")
        print("A giant dragon appears before your very eyes.")
        print("JEFFERY: AHH!")
        print("Dragon: Hello, traveller! You have something I want. But I'm not here to fight, I'm here to TRADE.")
        print(f"JEFFERY: Oh thank god {name}! I thought we had to fight that thing!")
        print("Dragon: I want that elastic band of yours ... I'll offer you to pick 1 of 2 mystery boxes for it. Which one do you want?")
        print(f"JEFFERY: Maybe the second one? I don't know. It's up to you, {name}.")
        mystery_box = input("(1 or 2) >> ")
        trade = random.randrange(1,3)
        if mystery_box == trade:
            print("Dragon: You got to trade your elastic band for an upgraded weapon!")
            inventory.append("Metal Sword")
            inventory.remove("Elastic Band")
        else:
            print("Dragon: You picked a power curse ... No take backs, I'm keeping your elastic band.")
            print("AW HECK NO!")
            inventory.remove("elastic band")
            power = power - (power * 0.25)


            
    elif stage == 4: #ANDY
        print("PLANET 4:")
         

        #loop to repeat the question if typed wrong
        while True:
            choice_4=input("small monster appears to be minding its own business.Do you wanna to kill or leave?: ")
            
            if choice_4 == "kill":
                level += 1
                monster = True
                break #exits loop because typed correctly
            elif choice_4 == "leave":
                strawberry += 1
                print("JEFFERY: You are a good person, here is a strawberry for you!")
                break
            else:
                print("Didn't get that ... Come again?")
      




    elif stage == 5: #LEO
        print("PLANET 5:")
        print("JEFFERY: We came across a space pod!")
        user_input = input("JEFFERY: Do you want to open the space pod?")
        if user_input.lower() == ("yes"):
            print("JEFFERY: You found a space tomato inside!")
            inventory.append("space tomato")
        else:
            print("JEFFERY: Okay...")

        
    elif stage == 6: #TARA
        print("PLANET 6:")
        time.sleep(1)
        print(f"{name} there is a galaxy medicine over there that might heal you or be poisonous")
        print("Do you want to drink the magical GALAXY drink?")
        galaxy=input()
        if galaxy=="yes" or galaxy=="Yes":
            print("curse is healed, you got your ELASTIC BAND back:>")
            inventory.append("Elastic Band")  
        if galaxy=="No" or galaxy=="no":
             print("OH NO, GALAXY drink was not poisonous")
            

    elif stage == 7: #CAILEIGH
        print("PLANET 7:")
        #dialogue
        time.sleep(1)
        print()
        print("You have encountered an ALIEN OCTOPUS!")
        print()
        time.sleep(1)
        print("JEFFREY: Um...hello?")
        time.sleep(1)
        print("ALIEN OCTOPUS: Skwrrr...SHRII!!!")
        print("JEFFREY: AAHHH!!")
        print()
        time.sleep(2)
        print("Traveller JEFFREY has been captured by ALIEN OCTOPUS!")
        time.sleep(1)
        print("ALIEN OCTOPUS: Skwillrll!")
        time.sleep(1)
        print(f"JEFFREY: Help, {name}! It says it's...fallen in love with me?? It's trying to take me home!")
        time.sleep(1)
        print("ALIEN OCTOPUS: Shwrr! Sklrwler!")
        time.sleep(2)
        print("JEFFREY: It says it loves me...almost as much as it loves space tomatoes! Do we have a space tomato???")
        time.sleep(3)
        print()

        #check for space tomato
        if 'space tomato' in inventory: 
            print("You check your inventory, and pull out a space tomato!")
            print()
            
            #give or eat space tomato loop
            while True:
                tomato_choice = input("Do you choose to [GIVE] the space tomato to JEFFREY, or [EAT] the space tomato?: ")
                print()
                if tomato_choice.lower() == 'give':
                    print("You give your space tomato to the alien octopus, and they release JEFFREY!")
                    time.sleep(1)
                    print()
                    print(f"JEFFREY: Phew, that could've been bad! Thanks, {name}! I'm ready to get out of here ASAP if you are.")
                    jeffrey_saved = True
                    break
    
                elif tomato_choice.lower() == 'eat':
                    print("You eat your tomato in front of the alien, who becomes angry!")
                    time.sleep(1)
                    print("The alien charges away with JEFFREY trapped in their arms!")
                    time.sleep(1.5)
                    print(f"JEFFREY: AAAHHHH!! {name}!!!")
                    time.sleep(1)
                    print()
                    print("You have lost traveller JEFFREY to the ALIEN OCTOPUS!")
                    jeffrey_saved = False
                    break
                else:
                    print("Sorry traveller, that wasn't a valid command!")

        else:
            print("You check your inventory...")
            time.sleep(1)
            print("There was a space tomato back on PLANET 5, but you left it there!")
            time.sleep(1)
            print("The ALIEN OCTOPUS is in love, and JEFFREY cannot be saved...")
            print(f"JEFFREY: Help, {name}! I'm being stolen!")
            time.sleep(1)
            print()
            print("You have lost traveller JEFFREY to the ALIEN OCTOPUS!")
            print()
            jeffrey_saved = False

    

    elif stage == 8: #TARA
       print("PLANET 8:")
       time.sleep(1)
       print("Wow! look at those monkeys")
       print(f"Hey, {name} will you fight or run?")
       monkeysfight=input()
       if monkeysfight=="fight" or monkeysfight=="Fight":
            print("Congratulation you got the mana banana:>")
            print("Your power increasing...")
            power+=10
            print(f"current power: {power}")
            if monkeysfight=="Run"or monkeysfight=="run":
                print("Oh no, you missed the chance to win the mana banana")
             
        

    elif stage == 9: #TARA
        print("PLANET 9:")
        time.sleep(1)
        print(f"Welcome to the next planet {name}")
        print("look there is a map over there that might help you")
        time.sleep(1)
        print("Here you go")
        time.sleep(1)
        print(f"{name} do you want to check the map?")
        map=input()
        if map=="yes" or map=="Yes":
              print("Looks like that a giant octopus is on the next planet, GOOD LUCK!")
        if map=="no" or map=="No":
             print(f"Emmm, ok {name} GOOD LUCK!")

    
    elif stage == 10: #CAILEIGH
        print("PLANET 10:")
        time.sleep(1)
        octo_health = 200
        print("Skwreee!!")
        time.sleep(1)
        print()

        #ENDING 1: IF JEFFREY WAS LOST IN STAGE 7
        if jeffrey_saved == False:
            #dialogue
            print("You spot the GIANT OCTOPUS in the distance...with JEFFREY in its arms!")
            time.sleep(1)
            print(f"JEFFREY: {name}...it's you. You who failed to save me. Well, lucky that I managed to tame this octopus...it's time to EXACT REVENGE!!")
            print()
            time.sleep(1)

            #fight loop
            while True:
                jeffrey_fight = input("Do you choose to [FIGHT] JEFFREY, or [RUN]?: ")
                print()

                #octopus' attack & player attack
                if jeffrey_fight.lower() == 'fight':
                    print("You draw your sword and prepare to fight!")
                    time.sleep(.5)
                    print(f"You attack with your sword, dealing {power} damage!")
                    time.sleep(.5)
                    octo_health -= power
                    print(f"OCTOPUS HEALTH: {octo_health}/200")
                    print()
                    time.sleep(1)
                    print("JEFFREY commands the octopus to attack, and you lose 60 HP!")
                    health -= 60
                    time.sleep(.5)
                    print()

                    #death
                    if health <= 0:
                        print("You have died.")
                        print("[ENDING VOYAGE...]")
                        sys.exit()

                    #print health if not dead
                    print(f"Current Health: {health}/{total_health}")
                    
                elif jeffrey_fight.lower() == 'run':
                    print()
                    print("JEFFREY: Don't think you can get away so easily, you sacrificed me to this monster!")
                    print()
                    time.sleep(1)
                    print("You were unable to escape!")
                    print("JEFFREY commands the monster to attack, and you lose 60 HP!")
                    health -= 60
                    time.sleep(.5)
                    print(f"Current Health:{health}/{total_health}")

                    #death
                    if health <= 0:
                        print("You have died.")
                        print("[ENDING VOYAGE...]")
                        sys.exit()

        #ENDING 2: IF JEFFREY WAS SAVED IN STAGE 7
        elif jeffrey_saved == True:
            #dialogue
            print(f"JEFFREY: Oh HELL no...the ALIEN OCTOPUS is back! Save me, {name}!")
            print()
            time.sleep(1)

            #loop question to fight or run
            while True:
                octo_fight = input("Do you choose to [FIGHT] the octopus, or [RUN]?: ")
                print()
    
                if octo_fight.lower() == 'fight':
                    print("JEFFREY: Hey, I'll get in on this one too. No way is this octopus taking me again!")
                    time.sleep(1)
                    print("You prepare to fight the ALIEN OCTOPUS with traveller JEFFREY...")
                    print()
                    time.sleep(1.5)
                    print("Traveller JEFFREY increases the power of your attack!")
                    power += 80
                    print(f"Current power: {power}")
                    time.sleep(1)
                    print()
    
                    #fight loop
                    while True:
                        print(f"You attack the octopus with your sword, dealing {power} damage!")
                        time.sleep(1)
                        octo_health -= power
                        print(f"Octopus health: {octo_health}")
                        time.sleep(1.5)
                        print()
                        
                        #if killed octopus (success ending)
                        if octo_health <= 0:
                            print('~' * 40)
                            print("ALIEN OCTOPUS has been defeated!")
                            print('~' * 40)
                            print()
                            time.sleep(1)
                            print("JEFFREY: Hah...AHAH! Take that, you three-hearted blob of slime!!")
                            time.sleep(1)
                            print(f"Thanks, traveller {name}. As a reward, I found quite a few of these for you. To...remind you of our adventures?")
                            print()
                            time.sleep(2)
                            print("Traveller JEFFREY has gifted you...")
                            time.sleep(.5)
                            print("Ten thousand space tomatoes!")
                            print()
                            time.sleep(1)
                            print(f"Heh...I hope these serve you well in your future adventures, traveller {name}. Until the next journey!")
                            sys.exit()
    
                        #continue fighting if octopus not dead
                        print("The ALIEN OCTOPUS returns the attack, and you lose 60 HP!")
                        health -= 60
                        print()
                        time.sleep(1)
    
                        #stop if death (failure ending)
                        if health <= 0:
                            print("You have died.")
                            print("[ENDING VOYAGE...]")
                            sys.exit()
                        
                        #print health & continue fighting if no one dies
                        print(f"Current health: {health}/{total_health}")
                        print("JEFFREY:We got this...Attack!!!")
                        print()

              #if choose to run or mistype
              else:
                  print("JEFFREY: No way am I running away! This octopus kidnapped the wrong astronaut!")
                  print()
                    
                    
           
        
        
   
