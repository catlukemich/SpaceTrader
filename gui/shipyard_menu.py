from modes.mode import *
from game.carrier import *
from gui.gui import *
from gui.animated_icon import *

class ShipyardMenu(MouseListener):


    def __init__(self):
        self.prototypes = [SmallCarrier(), MediumCarrier(), BigCarrier()]
        self.widgets = []

        x = 40
        y = 40
        for prototype in self.prototypes:
            panel_widgets = self.createSpaceShipPanel(x, y, prototype)
            self.widgets.extend(panel_widgets)
            y += 160


    def createSpaceShipPanel(self, x, y, prototype):
        widgets = []

        panel = Panel()
        panel.setPosition(x, y)
        panel.setSize(700, 150)
        widgets.append(panel)

        images = prototype.getImages()
        animated_icon = AnimatedIcon(30, images)
        animated_icon.addListener(self)
        animated_icon.setPosition(x + 10, y + 10)
        widgets.append(animated_icon)


        small_font = pygame.font.Font("assets/gui/LCD14.ttf", 12)
        big_font   = pygame.font.Font("assets/gui/LCD14.ttf", 20)

        embark_button = Text(big_font, "Embark")
        embark_button.setName("Embark button")
        embark_button.data = prototype
        embark_button.setPosition(x + 25, y + 60)
        embark_button.visible = False
        embark_button.addListener(self)
        widgets.append(embark_button)

        description_text = Text(small_font, prototype.getDescription())
        description_text.setPosition(x + 140, y + 20)
        widgets.append(description_text)

        price_text = Text(big_font, "Price: " + str(prototype.getPrice()))
        price_text.setPosition(x + 140, y + 45)
        widgets.append(price_text)

        owned = self.calcAmountOfOwned(prototype)
        if owned > 0:
            owned_text = Text(small_font, "Owned: YES")
        else:
            owned_text = Text(small_font, "Owned: NO")

        owned_text.setName("Amount")
        owned_text.data = prototype
        owned_text.setPosition(x + 140, y + 90)
        widgets.append(owned_text)

        sell_button = Button(assets.loadImage("assets/gui/sell.png"))
        sell_button.setName("Sell button")
        sell_button.addListener(self)
        sell_button.data = prototype
        sell_button.setPosition(x + 645, y + 60)
        widgets.append(sell_button)

        buy_button = Button(assets.loadImage("assets/gui/buy.png"))
        buy_button.setName("Buy button")
        buy_button.addListener(self)
        buy_button.data = prototype
        buy_button.setPosition(x + 645, y + 100)
        widgets.append(buy_button)


        return widgets


    def show(self):
        for widget in self.widgets:
            globvars.gui.addWidget(widget)


    def hide(self):
        for widget in self.widgets:
            globvars.gui.removeWidget(widget)

    def onMouseUp(self, widget):
        widget_name = widget.getName()
        if widget_name == "Buy button":
            prototype = widget.data
            spaceship = self.getSpaceshipOfType(prototype)
            if spaceship == None:
                if globvars.credits >= prototype.getPrice():
                    new_spaceship = prototype.clone()
                    globvars.spaceships.append(new_spaceship)
                    globvars.credits -= prototype.getPrice()

        elif widget_name == "Sell button":
            prototype = widget.data
            spaceship = self.getSpaceshipOfType(prototype)
            if spaceship != None:
                globvars.spaceships.remove(spaceship)
                globvars.credits += spaceship.getPrice()

        self.updateOwnedAmounts()

        # Embark the clicked ship if it's owned by the player:
        if widget.getName() == "Embark button":
            prototype = widget.data
            old_ship = globvars.player
            target_ship = self.getSpaceshipOfType(prototype)
            if target_ship != None:
                globvars.scene.removeSprite(old_ship)
                globvars.scene.addSprite(target_ship)
                position = old_ship.getPosition()
                target_ship.setPosition(position)
                globvars.player = target_ship
                setMode(globvars.fly_mode)
            else:
                globvars.messenger.putMessage("You do not own this spaceship!")


    def onMouseOver(self, widget):
        if widget.getName() == "Embark button":
            widget.visible = True

    def onMouseOut(self,widget):
        if widget.getName() == "Embark button":
            widget.visible = False

    def getSpaceshipOfType(self, prototype):
        for spaceship in globvars.spaceships:
            if prototype.getType() == spaceship.getType():  # Spaceship of the same type found
                return spaceship
        return None


    def updateOwnedAmounts(self):
        for widget in self.widgets:
            if widget.getName() == "Amount":
                prototype = widget.data
                owned_amount = self.calcAmountOfOwned(prototype)
                if owned_amount > 0:
                    widget.setText("Owned: YES")
                else:
                    widget.setText("Owned: NO")


    def calcAmountOfOwned(self, prototype):
        amount = 0
        for spaceship in globvars.spaceships:
            if spaceship.getType() == prototype.getType():
                amount += 1
        return amount