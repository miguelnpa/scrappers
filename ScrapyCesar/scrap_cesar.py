from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import os
import sys


class CesarSpider:

    url_link = 'https://cesar.breezy.hr/'

    def open_html(self):

        url = urlopen(self.url_link)
        bs = BeautifulSoup(url, 'html.parser')
        return bs

    def read_html(self):

        jobList = []
        a = self.open_html().find_all('a', title='Apply')
        for e in a:
            title = e.find('h2').text
            location = e.find('span').text.strip(', BR')
            jobList.append([title, location])
        return jobList

    def message_to_warning(self, message, message_lines):
        with open('warning.txt', "w") as f:
            f.write(message)
            f.writelines(message_lines)

    def send_warning(self):
        os.system('warning.txt')

    def run(self):
        try:
            message = "PROCESSOS DISPONÍVEIS NO CESAR, CONFERIR!!!" + '\n'
            message_lines = []
            for i in self.read_html():
                if "estágio" in i[0].lower() and "manaus" in i[1].lower():
                    message_lines.append(
                        "Job Title: " + i[0] + '\n' + 'Location: ' + i[1] + '\n')
            self.message_to_warning(message, message_lines)
            self.send_warning()

        except urllib.error.URLError as e:
            sys.exit()

        except AttributeError as e:
            sys.exit()

        except TypeError as e:
            sys.exit()

CesarSpider().run()