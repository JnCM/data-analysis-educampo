import os, sys, base64
import pandas as pd
import matplotlib.pyplot as plt
from mdutils import MdUtils

if __name__ == "__main__": 
    columns = [
        "6. Área em produção (hectare)",
        "16. Idade média das lavouras  (anos)",
        "17. Número de plantas/área plantada (plantas/hectare)",
        "18. Produtividade  (sacas/hectare)",
        "41. Margem líquida (R$/período)",
        "42. Lucro (R$/período)",
        "59. Preço médio de venda (R$/saca)",
        "70. Margem Líquida/saca (R$/saca)",
        "71. Lucro/saca (R$/saca)"
    ]
    group_column = "Região"

    path = os.path.dirname(os.path.abspath(__file__))
    data_filename = sys.argv[1]
    md_filename = sys.argv[2]
    try:
        opt = int(sys.argv[3])
    except:
        opt = None

    df = pd.read_excel(data_filename)
    mdFile = MdUtils(file_name=md_filename, title='Análise Exploratória do Café')
    
    index = 0
    for column in columns:
        mdFile.new_header(2, column.split(". ")[1], add_table_of_contents="n")
        df_boxplot = df[[group_column, column]]
        boxplot = df_boxplot.boxplot(by=group_column, return_type='dict', showmeans=True)
        
        bp_data = boxplot[column]
        means = [mean.get_ydata().tolist()[0] for mean in bp_data["means"]]
        medians = [median.get_ydata().tolist()[0] for median in bp_data["medians"]]
        whiskers = [whiskers.get_ydata().tolist() for whiskers in bp_data["whiskers"]]
        quartis = []
        limits = []
        for i in range(0, len(whiskers)-1, 2):
            q1 = whiskers[i][0]
            min_value = whiskers[i][1]
            q2 = whiskers[i+1][0]
            max_value = whiskers[i+1][1]
            quartis.append((q1, q2))
            limits.append((min_value, max_value))
        
        table = ["", "Cerrado", "Matas", "Sul"]
        line_min = ["Min."]
        line_max = ["Máx."]
        for pair in limits:
            line_min.append(str(round(pair[0],4)))
            line_max.append(str(round(pair[1],4)))
        line_q1 = ["Q1"]
        line_q3 = ["Q3"]
        for quartil in quartis:
            line_q1.append(str(round(quartil[0],4)))
            line_q3.append(str(round(quartil[1],4)))
        line_median = ["Mediana"]
        for median in medians:
            line_median.append(str(round(median,4)))
        line_mean = ["Média"]
        for mean in means:
            line_mean.append(str(round(mean,4)))
        
        table.extend(line_min)
        table.extend(line_max)
        table.extend(line_q1)
        table.extend(line_q3)
        table.extend(line_median)
        table.extend(line_mean)
        mdFile.new_table(columns=4, rows=7, text=table, text_align='center')
        
        img_name = os.path.join(path, "markdown\\imgs\\graph{}.png".format(index))
        plt.savefig(img_name)
        if opt == 1:
            img_path = "./imgs/graph{}.png".format(index)
        else:
            image_file = open(img_name, "rb")
            img_bytes = base64.b64encode(image_file.read()).decode("utf-8")
            img_path = "data:image/png;base64," + img_bytes
        mdFile.new_line(mdFile.new_inline_image(text="Boxplot por Região", path=img_path))
        
        index += 1

    mdFile.create_md_file()
