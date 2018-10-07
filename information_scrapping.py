from urllib import urlopen
import AdvancedHTMLParser


def get_html_from_url(url):
    response = urlopen(url)
    html = response.read()
    html = html.decode('iso-8859-1')
    return html


url = "https://www.serebii.net/pokedex-rs/001.shtml"
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

pointer = parser.getElementsByTagName('p')[0].getChildren()[1].getChildren()[5].getChildren()

male_percent = pointer[0].innerText.strip()
pkm_data['male_percent'] = str(male_percent)

female_percent = pointer[1].innerText.strip()
pkm_data['female_percent'] = str(female_percent)


print(pkm_data)
