def read_file():
        trueJobList = []
        with open("C:/Projetos/scrappers/ScrapyCesar/validacao/validacao.txt", 'r',encoding='utf-8') as f:
            jobList = f.read().split(',')
            for i in jobList:
                trueJobList.append(i.strip('\n'))
            return trueJobList
