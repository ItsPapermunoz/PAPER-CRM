import iem

# Vars



# Classes

class Contact:
  '''
  Class Object which has a name, phone and email attributes. In this program its appended into Lead class objects as an attribute.

  name = str Contacts Name Attribute

  phone = Contacts Phone Number

  email = Contacts Email
  '''
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email
    
class Lead:
  '''
  Class object that has a name, status, forecast, deals, owner and a contact class object.
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
    '''
    Changes Status in Lead.
    '''
    i = 0
    for status in Lead.status_list:
      i += 1
      print('{}. {}'.format(i, status))
    status = int(input('Seleccione un estado: ')) - 1
    self.status = Lead.status_list(status)

  def card(self):
    print('/n--- {} ---'.format(self.name))
    print('Phone: {} Email: {}'.format(self.phone, self.email))

class Deal:
  def __init__(self, fcst, prob, status):
    self.fcst = fcst
    self.prob = prob
    self.status = status
    
# Functions

def contact_new(contacts):
  '''
  Function that creates a new Contact Class Object, appends it to contacts list and saves it to Backup.dat file

  contacts = Contacts list for backup

  Function Returns Contact Class Object
  '''
  print('/n--- Nuevo Contacto ---/n')
  name = input('Ingrese Nombre de contacto: ')
  phone = int(input('Ingrese Telefono: '))
  email = input('Ingrese correo: ')
  contact = Contact(name, phone, email)
  contacts.append(contact)
  iem.save_backup(backup)
  return contact

def lead_lookup(leads, search=None):
  '''
  Function designed to lookup for a specific lead in Leads List

  leads = Leads List

  search = None Will print out all of the leads in the list for you to select one.

  search = str(name) If search is specified, function will compare Search to the name in leads list, if found returns lead

  returns lead class object

  '''
  while True:
    if search:
      for lead in leads:
        if search == lead.name:
          return lead
        else:
          return None
    else:
      for lead in leads:
        lead.card()
        search = input('Ingrese Nombre de contacto o ingrese SALIR para salir: ')
  
def lead_new(leads, contacts):
  print('/n--- New Lead ---/n')
  name = input('Nombre: ')
  i = 0
  for status in Lead.status_list:
    i += 1
    print('{}. {}'.format(i, Lead.status_list[i - 1]))
  status = int(input('Seleccione un estado: ')) - 1
  status = Lead.status_list[status]
  fcst = int(input('Ingrese valor estimado: $'))
  owner = input('Ingrese nombre del dueño del lead: ')
  contact = contact_new(contacts)
  lead = Lead(name, status, fcst, owner, contact)
  leads.append(lead)
  iem.save_backup(backup)

def leads_menu(leads, contacts):
  while True:
    options = ("Nuevo Lead", "Cambiar estatus de Lead", "Salir")
    sel = iem.display_menu(options, "Leads")
    if sel == len(options):
      break
    elif sel == 1:
      lead_new(leads, contacts)

def main_menu(leads, contacts):
  while True:
    options = ("Leads", "Salir")
    sel = iem.display_menu(options, "PAPER CRM")
    if sel == len(options):
      print("Gracias por utilizar PAPER CRM...")
      break
    elif sel == 1:
      leads_menu(leads, contacts)

# Main
backup = iem.load_backup()
contacts = backup[0]
leads = backup[1]
deals = backup[2]
main_menu(leads, contacts)

