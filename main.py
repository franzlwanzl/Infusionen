import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#to-do test
#Sender überprüfen
#date überprüfen
#tage überprüfen
#anzahl_infusionen überprüfen
#noch vorhandene Infusionssachen eintragen


sender_email = 'franz@die-reichels.de'
sender_passwort = 'Gitarre2001:)ST'
empfänger_email = 'franz@die-reichels.de'


#'Julia.Schier@livica.de'
#'stefan.eign@livica.de'

smtp_server = "smtp.strato.de"
smtp_port = 587

date = "04.10.24"
tage = 11
anzahl_infusionen = 3

#noch vorhandene Infusionssachen
infusionssysteme_vorhanden = 22
spritzen_20ml_vorhanden = 44
magnesium_vorhanden = 36
gelbe_kanülen_vorhanden = 110
calzium_vorhanden = 28
nacl_vorhanden = 21
spülsets_vorhanden = 41
gelber_eimer = False
desinfektionsmittel_blau = False
desinfektionsmittel_spray = False

#für eine Infusion täglich
if anzahl_infusionen == 1:
    spülsets = (2 * tage) - spülsets_vorhanden
    if spülsets <= 0:
        spülsets = False
    infusionssysteme = (1 * tage) - infusionssysteme_vorhanden
    if infusionssysteme <= 0:
        infusionssysteme = False
    nacl = (1 * tage) - nacl_vorhanden
    if nacl <= 0:
        nacl = False
    calzium = ((1 * tage) - calzium_vorhanden)
    if calzium <= 0:
        calzium = False
    mg_ampullen = (2 * tage) - magnesium_vorhanden
    magnesium = int(mg_ampullen / 5) + (mg_ampullen % 5 > 0)
    if magnesium <= 0:
        magnesium = False
    spritzen_20ml = (2 * tage) - spritzen_20ml_vorhanden
    if spritzen_20ml <= 0:
        spritzen_20ml = False
    gelbe_kanülen = (2 * tage) - gelbe_kanülen_vorhanden
    if gelbe_kanülen < 100 and gelbe_kanülen > 0:
        gelbe_kanülen = "eine 100er Packung"
    elif gelbe_kanülen <= 0:
        gelbe_kanülen = False

#für zwei Infusion täglich
if anzahl_infusionen == 2:
    spülsets = (4 * tage) - spülsets_vorhanden
    if spülsets <= 0:
        spülsets = False
    infusionssysteme = (2 * tage) - infusionssysteme_vorhanden
    if infusionssysteme <= 0:
        infusionssysteme = False
    nacl = (2 * tage) - nacl_vorhanden
    if nacl <= 0:
        nacl = False
    calzium = ((2 * tage) - calzium_vorhanden)
    if calzium <= 0:
        calzium = False
    mg_ampullen = (4 * tage) - magnesium_vorhanden
    magnesium = int(mg_ampullen / 5) + (mg_ampullen % 5 > 0)
    if magnesium <= 0:
        magnesium = False
    spritzen_20ml = (4 * tage) - spritzen_20ml_vorhanden
    if spritzen_20ml <= 0:
        spritzen_20ml = False
    gelbe_kanülen = (4 * tage) - gelbe_kanülen_vorhanden
    if gelbe_kanülen < 100 and gelbe_kanülen > 0:
        gelbe_kanülen = "eine 100er Packung"
    elif gelbe_kanülen <= 0:
        gelbe_kanülen = False

#für drei Infusionen täglich
if anzahl_infusionen == 3:
    spülsets = (4 * tage) - spülsets_vorhanden
    if spülsets <= 0:
        spülsets = False
    infusionssysteme = (3 * tage) - infusionssysteme_vorhanden
    if infusionssysteme <= 0:
        infusionssysteme = False
    nacl = (3 * tage) - nacl_vorhanden
    if nacl <= 0:
        nacl = False
    calzium = ((2 * tage) - calzium_vorhanden)
    if calzium <= 0:
        calzium = False
    mg_ampullen = (6 * tage) - magnesium_vorhanden
    magnesium = int(mg_ampullen / 5) + (mg_ampullen % 5 > 0)
    if magnesium <= 0:
        magnesium = False
    spritzen_20ml = (6 * tage) - spritzen_20ml_vorhanden
    if spritzen_20ml <= 0:
        spritzen_20ml = False
    gelbe_kanülen = (6 * tage) - gelbe_kanülen_vorhanden
    if gelbe_kanülen < 100 and gelbe_kanülen > 0:
        gelbe_kanülen = "eine 100er Packung"
    elif gelbe_kanülen <= 0:
        gelbe_kanülen = False

#für vier Infusionen täglich
if anzahl_infusionen == 4:
    spülsets = (6 * tage) - spülsets_vorhanden
    if spülsets <= 0:
        spülsets = False
    infusionssysteme = (4 * tage) - infusionssysteme_vorhanden
    if infusionssysteme <= 0:
        infusionssysteme = False
    nacl = (4 * tage) - nacl_vorhanden
    if nacl <= 0:
        nacl = False
    calzium = ((4 * tage) - calzium_vorhanden)
    if calzium <= 0:
        calzium = False
    mg_ampullen = (8 * tage) - magnesium_vorhanden
    magnesium = int(mg_ampullen / 5) + (mg_ampullen % 5 > 0)
    if magnesium <= 0:
        magnesium = False
    spritzen_20ml = (7 * tage) - spritzen_20ml_vorhanden
    if spritzen_20ml <= 0:
        spritzen_20ml = False
    gelbe_kanülen = (7 * tage) - gelbe_kanülen_vorhanden
    if gelbe_kanülen < 100 and gelbe_kanülen > 0:
        gelbe_kanülen = "eine 100er Packung"
    elif gelbe_kanülen <= 0:
        gelbe_kanülen = False


subject = "Infusionsbestellung Reichel für den " + date
anrede = "Hallo Herr Eign,\n\n"
vorgeplenkel = "Ich melde ich mich wieder, um Infusionssachen für Freitag den " + date + " bei Ihnen zu bestellen." + "\nIch bräuchte:\n"
bestellung = ""
if spülsets:
    bestellung += "\n- Spülsets: " + str(spülsets)

if infusionssysteme:
    bestellung += "\n- Infusionssysteme: " + str(infusionssysteme)

if gelbe_kanülen:
    bestellung += "\n- gelbe Kanülen: " + str(gelbe_kanülen)

if nacl:
    bestellung += "\n- NaCl: " + str(nacl)

if calzium:
    bestellung += "\n- Calzium: " + str(calzium) + " Ampullen"

if magnesium:
    bestellung += "\n- Magnesium: " + str(magnesium) + " Packungen"

if spritzen_20ml:
    bestellung += "\n- 20ml Spritzen: " + str(spritzen_20ml)

if gelber_eimer:
    bestellung += "\n- gelber Eimer für Kanülen und Glas"

if desinfektionsmittel_blau:
    bestellung = bestellung + "\n- Blaues Handdesinfektionsmittel"

if desinfektionsmittel_spray:
    bestellung = bestellung + "\n- normales Sprüh-Desinfektionsmittel"

verabschiedung = "\n\nVielen Dank!\n"
abrede = ("\nGrüße,\n" +
          "Franz Reichel")

body = (anrede + vorgeplenkel+ bestellung + verabschiedung + abrede)

nachricht = MIMEMultipart()
nachricht['From'] = sender_email
nachricht['To'] = empfänger_email
nachricht['Subject'] = subject
part_body = MIMEText(body, 'plain')
nachricht.attach(part_body)

server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(1)
server.starttls()
server.login(sender_email, sender_passwort)
server.sendmail(sender_email, empfänger_email, nachricht.as_string())
server.quit()
print("ERFOOLG")