from flet import *
import google.generativeai as genai
import asyncio
import os
import dotenv

dotenv.load_dotenv()

#configure google
genai.configure(api_key=os.environ["APIKEY"])
model = genai.GenerativeModel("gemini-1.5-flash-002")

class Chatbot(Column):
    def __init__(self):
        super().__init__()
        self.horizontal_alignment = CrossAxisAlignment.CENTER
        self.scroll = ScrollMode.ALWAYS
        self.expand = True

        self.enterbutton = ElevatedButton(text="Enter", icon=icons.ARROW_RIGHT, on_click=self.getprompt)
        self.promptinput = TextField(
            value="Enter prompt here...",
            width=500,
            border='2',
            on_focus=self.removeplaceholder,
            border_color="#36618E",
            suffix=self.enterbutton,
            on_submit=self.getprompt
        )

        self.promptparent = Container(padding=padding.only(0,100,0,0),content=self.promptinput)

        self.controls.insert(3,self.promptparent) 

        self.chats = Column(horizontal_alignment=CrossAxisAlignment.CENTER)
        self.controls.insert(0,self.chats)

    def removeplaceholder(self,e):
        if self.promptinput.value == "Enter prompt here...":
           self.promptinput.value = None
    
        self.promptinput.update()
    
    def getprompt(self, e):
        self.loading = ProgressRing(width=50, height=50)
        self.loadcontainer = Container(margin=margin.only(0, 30, 0, 0), content=self.loading)
        self.controls.insert(1,self.loadcontainer)
        self.update()

        async def fetch_response():
            data = await asyncio.to_thread(model.generate_content, self.promptinput.value)
            self.controls.remove(self.loadcontainer)
        
            user = Text(self.promptinput.value, weight="bold", size="15")
            bot = Text(data.text, size="15")
            self.chat = Container(margin=margin.only(0,30,0,0),content=Column(horizontal_alignment=CrossAxisAlignment.CENTER, controls=[user,bot],))

            self.chats.controls.append(self.chat)

            self.promptinput.value = "Enter prompt here..."
            self.update()

        asyncio.run(fetch_response())

def main(page:Page):
    page.title = "My chatbot 2.0"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def changetheme(e):
        if navbar.actions[0].icon == icons.WB_SUNNY_OUTLINED:
            navbar.actions[0].icon = icons.DARK_MODE_OUTLINED
            page.theme_mode = ThemeMode.DARK
        else:
             navbar.actions[0].icon = icons.WB_SUNNY_OUTLINED
             page.theme_mode = ThemeMode.LIGHT
        page.update()

    navbar = AppBar(
        leading=Icon(icons.CHAT_BUBBLE_OUTLINE_ROUNDED),
        leading_width=40,
        title=Text("My chat bot 2.0"),
        center_title=True,
        bgcolor=colors.SURFACE_VARIANT,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED, on_click=changetheme),
            PopupMenuButton(
            items=[
                PopupMenuItem(text="Item 1"),
                PopupMenuItem(),  # divider
                PopupMenuItem(
                    text="Checked item", checked=False,
                    ),
                    ]
                ),
            ],)
    
    page.add(navbar, Chatbot())
    

app(target=main,)