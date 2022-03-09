"""
Essentials Module
Containing basic functions

"""
import pickle as pkl

def display_menu(options, title):
  print('\n----- {} -----\n'.format(title))
  i = 0
  for option in options:
    i += 1
    print('{}. {}'.format(i, option))
  sel = int(input('Seleccione una opcion: '))
  return sel

def load_backup():
  try:
    with open("Backup.dat", "rb") as file:
      data = pkl.load(file)
  except FileNotFoundError:
    data = []
    for i in range(0, 5):
      i = []
      data.append(i)
    with open("Backup.dat", "wb") as file:
      pkl.dump(data, file)
  finally:
    return data

def save_backup(data):
  with open("Backup.dat", "wb") as file:
      pkl.dump(data, file)

def currency(amount):
  return '${:,.2f}'.format(amount)