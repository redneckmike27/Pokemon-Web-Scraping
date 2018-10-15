from urllib import urlopen
import AdvancedHTMLParser


def get_html_from_url(url):
    response = urlopen(url)
    html = response.read()
    html = html.decode('iso-8859-1')
    return html


url = "https://www.serebii.net/pokedex-rs/143.shtml"
pkm_html = get_html_from_url(url)
pkm_data = {}

parser = AdvancedHTMLParser.AdvancedHTMLParser()
parser.parseStr(pkm_html)

pointer = parser.getElementsByTagName('p')[0].getChildren()[1].getChildren()[1].getChildren()

nat_num = pointer[1].innerText.strip()
pkm_data['national_number'] = int(nat_num)

hoenn_num = pointer[2].innerText.strip()
pkm_data['hoenn_num'] = int(hoenn_num)

pkm_name = pointer[3].innerText.strip()
pkm_data['pokemon_name'] = str(pkm_name)

#def
#ability = {}

pointer = parser.getElementsByTagName('p')[0].getChildren()[1].getChildren()[5].getChildren()

male_percent = pointer[0].innerText.strip().strip("Male: ").strip(" %")
pkm_data['male_percent'] = str(male_percent)

female_percent = pointer[1].innerText.strip().strip("Female: ").strip(" %")
pkm_data['female_percent'] = str(female_percent)

pointer = parser.getElementsByTagName('p')[0].getChildren()[1].getChildren()[7].getChildren()

classification = pointer[0].innerText.strip().strip(" Pok&eacute;mon")
pkm_data['classification'] = str(classification)

type_1 = pointer[1].getChildren()[0].getChildren()[0]
pkm_data['type_1'] = str(type_1)

type_2 = pointer[2].getChildren()[0].getChildren()[0]
pkm_data['type_2'] = str(type_2)

height = pointer[3].innerText.strip()
pkm_data['height'] = str(height)

weight = pointer[4].innerText.strip()
pkm_data['weight'] = str(weight)

next_pkm = parser.getElementsByTagName('p')[0].getChildren()[1].getChildren()[9].getChildren()[0].getChildren()[0].getChildren()[1]
pkm_data['next pokemon'] = str(next_pkm)[21:24]
    #if next_pkm = false
     #   next_pkm = "none"

pointer = parser.getElementsByTagName('p')[1].getChildren()[0].getChildren()[1].getChildren()

hold_item = pointer[0].innerText.strip()
pkm_data['wild hold item'] = str(hold_item)

dex_cat = pointer[1]
pkm_data['dex category'] = str(dex_cat)

color_cat = pointer[2].innerText.strip()
pkm_data['colour category'] = str(color_cat)

footprint = pointer[3]
pkm_data['footprint'] = str(footprint)

description =parser.getElementsByTagName('p')[2].getChildren()[0].getChildren()[3].getChildren()[1].innerText.strip()
pkm_data['description'] = str(description)

location = parser.getElementsByTagName('p')[3].getChildren()[1].getChildren()[4].getChildren()[2].innerText.strip()
pkm_data['location'] = str(location)

#def
#rse_lvl_up_att = {}

#def
#tm_hm = {}

#def
#tutor_att = {}

egg_steps = parser.getElementsByTagName('p')[11].getChildren()[0].getChildren()[1].getChildren()[0].innerText.strip()
pkm_data['egg steps'] = str(egg_steps)

effort_points = parser.getElementsByTagName('p')[11].getChildren()[0].getChildren()[1].getChildren()[1].innerText.strip()
pkm_data['effort_points'] = str(effort_points)

catch_rate = parser.getElementsByTagName('p')[11].getChildren()[0].getChildren()[1].getChildren()[2].innerText.strip()
pkm_data['catch rate'] = str(catch_rate)

egg1 = parser.getElementsByTagName('p')[12].getChildren()[0].getChildren()[2].getChildren()[1].innerText.strip()
pkm_data['egg group 1'] = str(egg1)

egg_groups_table_length = len(parser.getElementsByTagName('p')[12].getChildren()[0].getChildren())
table_lenght = int(egg_groups_table_length)
print(egg_groups_table_length)

if table_lenght == 4:
    egg2 =  parser.getElementsByTagName('p')[12].getChildren()[0].getChildren()[3].getChildren()[1].innerText.strip()
    pkm_data['egg group 2'] = str(egg2)


pointer = parser.getElementsByTagName('p')[13].getChildren()[1].getChildren()[2].getChildren()

base_hp = pointer[1].innerText
pkm_data['base hp'] = int(base_hp)

base_att = pointer[2].innerText
pkm_data['base attack'] = int(base_att)

base_def = pointer[3].innerText
pkm_data['base defense'] = int(base_def)

base_sp_att = pointer[4].innerText
pkm_data['base sp. attack'] = int(base_sp_att)

base_sp_def = pointer[5].innerText
pkm_data['base sp. defense'] = int(base_sp_def)

base_speed = pointer[6].innerText
pkm_data['base speed'] = int(base_speed)




print(pkm_data)
