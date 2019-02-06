## This is based off of Happy Death Day.
## You have to try and solve you're own death and find out who killed you.
## Goodluck

## Scene

from textwrap import dedent
from sys import exit


class Scene(object):

    def enter(self):
        exit(1)

class Bedroom(Scene):

    def enter(self):
        print(dedent("""
            You wake up after being killed by someone who has been stalking your every move. It has happened time after time again, and now you're fed up with it. Now is the time to solve you're own murder and kill this son of a... You know what I meant to say. Make the right choices, don't get killed again or you will wake up again re-living everything over again. Have fun, goodluck, and HAPPY DEATH DAY!

            *************************************************************

            The last thing you remember was going home from a frat party and decided it was a WONDERFUL idea to walk through the very cloudy park. Someone with a baby-face mask stabs you in the chest a steak knife. You finally wake up scared for your safety. Only way to stop this loop is to find out who keeps killing you, and kill them. With this informaton at hand, what do you want to do?

            1. Walk to the kitchen and grab the sharp knife from the sink for protection.
            2. Go to the living room and call your friends.


        """))

        insert = input(">> ")


        if insert == '1':
            print(dedent("""
                Not a bad choice. Just hope you got some sick skills with that thing unless you're dunzo.
            """))
            ParkScene.enter(self)

        elif insert == '2':
            print(dedent("""
                I mean it's not a bad idea but, it wasn't the correct thing to do. You're power got cut off when you tried to call your friends. It's very dark and you can't see a thing. Footsteps start to come closer and closer. The maniac comes from behind you and slits your throat and you bleed to death.
            """))
            return 'Bedroom'
        else:
            print(dedent("""
                Not in choices!
            """))
            return 'Bedroom'


class ParkScene(Scene):

    def enter(self):
        print(dedent("""
            This should be familiar... I mean you did die here before so be careful.

            ***************************************************************

            You go back to the park and take the same path you took the night you got murdered. As you get closer to the exact location to where you got stabbed, you see the baby-face mask on the floor near the trash bin and a trail of muddy footsteps towards the statue in the middle of the park.

            1. Pick up the mask and follow the muddy trail
            2. Leave the park and run home
            3. Yell for help (for some reason.)
        """))

        insert = input(">> ")

        if insert == '1':
            print(dedent("""
                As you get closer to the Statue, you see some of the bushes moving. Is it a squirrel? Raccoon? Your Aunt Nancy? Nah, it was just a raccoon don't be scared. After realizing there is nothing else to worry about, you head over to the apartment building across the street in hope to find out anymore clues.
            """))

            ApptBuilding.enter(self)

        elif insert == '2':
            print(dedent("""
                As you get closer to the exit, the Maniac comes out from hiding behind a tree and trips you then suffocates you until you die.
            """))

            return 'Bedroom'

        elif insert == '3':
            print(dedent("""
                After yelling for 30 seconds the Maniac shoots you in the mouth with a silence pistol to shut you up.
            """))

            return 'Bedroom'

        else:
            print(dedent("""
                Not in Choices. Now start over.
            """))

            return 'Bedroom'

class ApptBuilding(Scene):

    def enter(self):
        print(dedent("""
            As you approach the apartment building, you see a note on the glass door. It says, "Building will be under construction from 02/11 - 02/23 from 9:00am-8:30pm." It's 02/13 today and the time is 5:00pm. You see the work vehicles in the area, but no construction noises coming from within the building? You decide to enter and see two apartment rooms slighly open, A3 & B2. The building has been evacuated due to the construction, why are people still in their rooms?

            1. Go through B2
            2. Go through A3
        """))

        insert = input(">> ")

        if insert == '2':
            print(dedent("""
                The tv is on, sink is on, and the shower is running. You start to head into the bathroom and see a trail of blood leading into it. You open the door and see the baby-face mask Maniac washing his bloody hands. You grab your steak knife and stab him in the neck. Once he bleeds to death you take off his mask, it was one of your friends from the frat party you went to.
            """))

            Solved.enter(self)

        elif insert == '1':
            print(dedent("""
                As you get closer to the door, you can see the room is really misty and hard to see through. YOu start to enter the room and trip over claymore mine and explode into pieces.
            """))

            return 'Bedroom'

class Solved(object):

    def enter(self):
        print(dedent("""
            You solved it congrats!
        """))


Bedroom.enter(Scene)
