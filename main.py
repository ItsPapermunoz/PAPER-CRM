import iem

# Vars



# Classes

class Contact:
  '''
  Class Object which has a name, phone and email attributes. In this program its appended into Lead class objects as an attribute.
  '''
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email
    
class Lead:
  '''
  Class object that has a name, status, forecast, owner and a contact class object.
  '''
  status_list = {1: 'NUEVO', 2: 'ASIGNADO', 3: 'EN PROCESO', 4: 'CALIFICADO', 5: 'NO CALIFICADO'}
  def __init__(self, name, status, fcst, owner, contact):
    self.name = name
    self.status = status
    self.fcst = fcst
    self.owner = owner
    self.deals = []
    self.contact = contact

  def update_status(self):
    i = 0
    for status in Lead.status_list:
      i += 1
      print('{}. {}'.format(i, status))
    status = int(input('Seleccione un estado: ')) - 1
    self.status = Lead.status_list(status)
class Deal:
  def __init__(self, fcst, prob, status):
    self.fcst = fcst
    self.prob = prob
    self.status = status
    
# Functions

def lead_new(leads):
  print('/n--- New Lead ---/n')
  name = input('Nombre: ')
  i = 0
  for status in Lead.status_list:
    i += 1
    print('{}. {}'.format(i, status))
  status = int(input('Seleccione un estado: ')) - 1
  status = Lead.status_list(status)
  fcst = int(input('Ingrese valor estimado: $'))
  owner = input('Ingrese nombre del dueño del lead: ')
  contact = None
  lead = Lead(name, status, fcst, owner, contact)
  leads.append(lead)
  iem.save_backup(backup)

def leads_menu(leads):
  while True:
    options = ("Nuevo Lead", "Cambiar estatus de Lead", "Salir")
    sel = iem.display_menu(options, "Leads")
    if sel == len(options):
      break
    elif sel == 1:
      lead_new(leads)

  
def main_menu(leads):
  while True:
    options = ("Leads", "Salir")
    sel = iem.display_menu(options, "PAPER CRM")
    if sel == len(options):
      print("Gracias por utilizar PAPER CRM...")
      break
    elif sel == 1:
      leads_menu(leads)

# Main
backup = iem.load_backup()
contacts = backup[0]
leads = backup[1]
deals = backup[2]
main_menu(leads)

