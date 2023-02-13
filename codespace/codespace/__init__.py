from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "World")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

def main():
    web.run_app(app, port=8080)