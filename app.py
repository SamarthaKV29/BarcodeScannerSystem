import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        indx = 10
        return render.index(i = indx)

if __name__ == "__main__":
    app.run()
