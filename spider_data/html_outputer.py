#coding:utf8

class HtmlOutputer(object):

    def __init__(self):
        # equal list
        self.datas=[]

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        #w mean write
        fout=open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

       # ascii is python default encode , so we need change into utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()