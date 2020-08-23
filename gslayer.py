# Feel free to change any stats within the classes

import os, sys, random, time

class gslayer():
  def __init__(self):
    self.name = 'Goblin S'
    self.lvl = 1
    self.exp = 0
    self.maxexp = 12
    self.hp = 100
    self.maxhp = 100
    self.mana = 25
    self.maxmana = 25
    self.baseattack = 10
    self.hppotamt = 0
    self.manapotamt = 0

class gslayerskills():
	def __init__(self):
		self.smitedmg = 50
		self.assassinatedmg = 999
		self.stabdmg = 25
		self.blockamt = 10

class goblin():
  def __init__(self):
    self.basehp = 20
    self.name = 'Goblin'
    self.hp = 20
    self.maxhp = 20
    self.baseattack = 5 
    self.lvl = 0

class goblinshaman():
  def __init__(self):
    self.basehp = 40
    self.name = 'Goblin Shaman'
    self.hp = 40
    self.maxhp = 40
    self.baseattack = 10
    self.lvl = 0

class goblinchampion():
  def __init__(self):
    self.basehp = 100
    self.name = 'Goblin Champion'
    self.hp = 100
    self.maxhp = 100
    self.baseattack = 20
    self.lvl = 0

class goblinlord():
  def __init__(self):
    self.basehp = 200
    self.name = 'Goblin Lord'
    self.hp = 500
    self.maxhp = 200
    self.baseattack = 30
    self.lvl = 0

############################################

# Start Menu
def start(title):
  os.system('clear')
  print('{}'.format('=' * (len(title) + 4) ))
  print('{:^17}'.format(title))
  print('{}'.format('=' * (len(title) + 4) ))
  print('{:^17}'.format('- Help -'))
  print('{:^17}'.format('- Enter to Play -'))
  option = input('')
  if option == 'help':
    help()

# Help Menu
def help():
  os.system('clear')
  print('{:^28}'.format('=' * 10))
  print('{:^28}'.format('Help'))
  print('{:^28}'.format('=' * 10))
  print('Use numbers 1 to 4 and Enter')
  print('-'*30)
  input('\nEnter to go back... ')
  start('Goblin Slayer')

# Potion Menu
def potions(): 
  global hppotused, healamt, manapotused, manaamt
	
  os.system('clear')
  print('{:^15}'.format('='*11))
  print('{:^15}'.format('Potions'))
  print('{:^15}'.format('='*11))
  print()
  print('1. {}: {}'.format('HP Potion', gslayer.hppotamt))
  print('2. {}: {}'.format('Mana Potion', gslayer.manapotamt))
  print('3. Back')
  option = input('\n> ')
  if option in ['1','2'] and (gslayer.hppotamt or gslayer.manapotamt) > 0:
    gslayer.attack = 0
    enemy.attack = random.randint(enemy.baseattack - 4, enemy.baseattack)
    gslayer.hp -= enemy.attack
    os.system('clear')

  if option == '1' and gslayer.hppotamt > 0 and gslayer.hp != gslayer.maxhp:
    hppotused = True
    healamt = int(gslayer.maxhp/4)
    gslayer.hppotamt -= 1
    gslayer.hp += healamt - enemy.attack
    if gslayer.hp > gslayer.maxhp:
      gslayer.hp = gslayer.maxhp

  elif option == '2' and gslayer.manapotamt > 0 and gslayer.mana != gslayer.maxmana:
    manapotused = True
    manaamt = gslayer.maxmana
    gslayer.manapotamt -= 1
    gslayer.mana += manaamt
    if gslayer.mana > gslayer.maxmana:
      gslayer.mana = gslayer.maxmana

  elif option.lower() == '3':
    battle()
  
  else:
    potions()

  battle()

# Skills Menu
def skills():
  options = ''
  os.system('clear')
  print('{:^15}'.format('='*10))
  print('{:^15}'.format('Skills'))
  print('{:^15}'.format('='*10))
  num = ['1','2','3','4']
  for skill, numbers in zip(skillslist, num):
    print('{}. {}'.format(numbers, skill))
  options = input('\n> ')
  if options in ['1','2','3'] and 'Not Learned' not in (skillslist[0] or skillslist[1] or skillslist[2]):
    enemy.attack = random.randint(enemy.baseattack - 4, enemy.baseattack)
    gslayer.hp -= enemy.attack
  
  if options == '1' and skillslist[0] != 'Not Learned' and gslayer.mana >= 5:
    global stabbed
    stabbed = True
    gslayer.mana -= 5
    gslayer.attack = gslayerskills.stabdmg
    enemy.hp -= gslayer.attack
    
  elif options == '2' and skillslist[1] != 'Not Learned' and gslayer.mana >= 10:
    global smited
    smited = True
    gslayer.mana -= 5
    gslayer.attack = gslayerskills.smitedmg
    enemy.hp -= gslayer.attack
	
  elif options == '3' and skillslist[2] != 'Not Learned' and gslayer.mana == gslayer.maxmana:
    global assassinated
    assassinated = True
    gslayer.mana -= 10
    gslayer.attack = gslayerskills.assassinatedmg
    enemy.hp -= gslayer.attack

  elif options == '4':
    battle()
  else:
    skills()
  
  battle()
  
# Battle Interface
def battle():
  global stabbed, assassinated, smited, hppotused, manapotused

  os.system('clear')
  print('Floor: {}\n'.format(floor))
  print('Lv. {}{:15}Lv. {}'.format(gslayer.lvl , '', enemy.lvl))
  print('{:20}{:20}'.format(gslayer.name, enemy.name))
  print('HP:{:3}/{:<3}{:10}HP:{:3}/{:<3}'.format(gslayer.hp, gslayer.maxhp, '', enemy.hp, enemy.maxhp))
  print('Mana: {}/{}'.format(gslayer.mana,gslayer.maxmana))
  print('{}'.format('-'*40))
  print('1. Attack')
  print('2. Skills')
  print('3. Potion')
  print('4. Run')
  
  scenarios = ['slapped', 'hit', 'punched', 'kicked']
  randomattack = random.choice(scenarios)
  
  if (hppotused or manapotused) == True:
  	
    if hppotused == True:
      hppotused = False
      print('\nYou healed for {} HP but the {} {} you for {} dmg'.format(healamt, enemy.name, randomattack, enemy.attack))

    elif manapotused == True:
      manapotused = False
      print('\nYou restored for {} Mana but the {} {} you for {} dmg'.format(manaamt, enemy.name, randomattack, enemy.attack))

  elif (stabbed or assassinated or smited) == True:
    if stabbed == True:
      print('\nYou stabbed the {} for {} dmg'.format(enemy.name, gslayerskills.stabdmg))
      print('The {} {} you for {} dmg'.format(enemy.name, randomattack, enemy.attack))
        
    elif smited == True:
      print("\nYou smited the {} for {} dmg".format(enemy.name, gslayerskills.smitedmg))
      print('The {} {} you for {} dmg'.format(enemy.name, randomattack, enemy.attack))
        
    elif assassinated == True:
      print('\nYou assassinated the {} for {} dmg'.format(enemy.name, gslayerskills.assassinatedmg))
      print('The {} {} you for {} dmg'.format(enemy.name, randomattack, enemy.attack))


    stabbed = False
    assassinated = False
    smited = False
  
  elif enemy.hp != enemy.maxhp and (stabbed and assassinated and smited) == False and (hppotused and manapotused) == False:
    print('\nYou dealt {} dmg to the {}'.format(gslayer.attack, enemy.name))
    print('The {} {} you for {} dmg'.format(enemy.name, randomattack, enemy.attack))
	
  postbattle()

# Post Battle Rewards/Death/Diaogue
def postbattle():
  if gslayer.hp <= 0:
    os.system('clear')
    print('You got Goblined!')
    print('Game Over!')
    sys.exit()

  elif enemy.hp <= 0:
    if enemy == goblin and floor == 1:
      gslayer.exp += gslayer.maxexp
    elif enemy == goblin:
      gslayer.exp += int(gslayer.maxexp/3)
    elif enemy == goblinshaman:
      gslayer.exp += int(gslayer.maxexp/2)
      chance = random.randint(1,4)
      if 1 <= chance <= 3:
        potname = 'HP'
        lootchance = random.randint(1,3)
        if lootchance == 1:
          potlooted = 1
        elif lootchance == 2:
          potlooted = 2
        elif lootchance == 3:
          potlooted = 3
        gslayer.hppotamt += potlooted
      else:
        potname = 'Mana'
        lootchance = random.randint(1,3)
        if lootchance == 1:
          potlooted = 1
        elif lootchance == 2:
          potlooted = 2
        elif lootchance == 3:
          potlooted = 3
        gslayer.manapotamt += potlooted
    elif enemy == goblinchampion:
      gslayer.exp = gslayer.maxexp
      

    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    
    if enemy == goblinshaman:
      print('You looted {} {} potion from the {}'.format(potlooted, potname, enemy.name))
    
    print('+{}/{} EXP'.format(gslayer.exp, gslayer.maxexp))
    input('\nEnter to continue..')
    levelup()

  option()

# Options to Attack/Potion/Skills/Run
def option():
  options = ''
  while options not in ['1','2','3','4']:
    options = input('> ')
    if options == '1':
      gslayer.attack = random.randint(gslayer.baseattack - 4, gslayer.baseattack)
      enemy.attack = random.randint(enemy.baseattack - 4, enemy.baseattack)
      enemy.hp -= gslayer.attack
      gslayer.hp -= enemy.attack

      battle()

    elif options == '2':
      skills()
    elif options == '3':
      potions()
    elif options == '4':
      chance = random.randint(1,4)
      if 1 <= chance <= 3:
        os.system('clear')
        print('You fled from the {}'.format(enemy.name))
        levels()
      else:
        os.system('clear')
        print('The {} killed you from behind while you were trying to run away'.format(enemy.name))
        print('You died!')
        sys.exit()
    else:
      sys.stdout.write(CURSOR_UP_ONE)
      sys.stdout.write(ERASE_LINE)
  
  option()

# Leveling Up
def levelup():
  if gslayer.exp >= gslayer.maxexp:
    gslayer.lvl += 1
    gslayer.exp = 0
    gslayer.mana = gslayer.maxmana
    gslayer.hp = gslayer.maxhp
    
    os.system('clear')
    print('You leveled up!')
    if gslayer.lvl == 2:
      skillslist[0] = 'Stab'
      print("You learned 'Stab'!")
    elif gslayer.lvl == 4:
      skillslist[1] = 'Smite'
      print("You learned 'Smite'!")
    elif gslayer.lvl == 5:
      skillslist[2] = 'Assassinate'
      print("You learned 'Assassinate'!")
    print('Current floor: {}'.format(gslayer.lvl))
    input('\nEnter to continue...')

  levels()

# Levels 1-15
def levels():
  global enemy 
  global floor
  floor += 1

  if 1 <= floor <= 3:
    enemy = goblin
  elif 4 <= floor <= 6:
    randomenemy = random.randint(1,4) 
    if 1 <= randomenemy <= 3:
      enemy = goblinshaman
    else:
      enemy = goblin 
  elif 7 <= floor <= 9:
    enemy = goblinchampion
  elif floor == 10:
    enemy = goblinlord
  elif floor > 10:
  	os.system('clear')  
  	print('Victory!')
  	exit()
  
  if (1 or 4 or 7 or 10) == floor: 
    enemy.lvl = 1
  
  elif (1 or 4 or 7) != floor:
    chance = random.randint(1,2)
    enemy.hp = enemy.basehp
    enemy.maxhp = enemy.hp
    
    if chance == 1:
      enemy.lvl = 1

    elif chance == 2:
      enemy.lvl = 2
      if enemy.lvl == 2:
        enemy.maxhp += int(enemy.basehp * .25)
        enemy.hp = enemy.maxhp

  battle()

gslayer = gslayer()
gslayerskills = gslayerskills()
goblin = goblin()
goblinshaman = goblinshaman()
goblinchampion = goblinchampion()
goblinlord = goblinlord()

# Pre-Defined Variables
global CURSOR_UP_ONE
global ERASE_LINE
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

skillslist = ['Not Learned', 'Not learned', 'Not Learned', 'Back']
floor = 0

stabbed, assassinated, smited = False, False, False
hppotused, manapotused = False, False

# Start
start('Goblin Slayer')
levels()
