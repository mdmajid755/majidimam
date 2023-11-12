# This is the site logic file


import web

urls = (
    '/', 'index',
    '/gb(.*)', 'goodBye',  # (.*) is regex that accepts anything 
    '/gb/(.*)', 'goodBye',
    '/NandA/(.*)/(.*)', 'nameAge',
    '/NandA(.*)(.*)', 'nameAge'
)

#define where templates to render are
render = web.template.render("templates")
#render = web.template.render("templates", base="MainLayout")

class index:
    def GET(self):
        return "Hello, world!"

class goodBye:
    def GET(self, name):  # name is the regex match from the route associated with goodBye function
        return "Goodbye " + name + "!"    

class nameAge:
    def GET(self, name, age): 
        i = web.input(name=name, age=age)
        return render.NandA(i.name, i.age)




if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
